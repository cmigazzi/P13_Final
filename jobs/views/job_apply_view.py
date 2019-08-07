from django.views.generic import FormView
from django.shortcuts import redirect, reverse
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

from jobs.forms import JobApplyForm
from jobs.models import JobOffer


class JobApplyView(FormView):
    """Return view and handle form validation for job apply."""

    form_class = JobApplyForm
    template_name = "jobs/apply-form.html"
    success_url = "/dashboard/"
    mail_to_school_template = "emails/job-to-school.html"

    def get_context_data(self, **kwargs):
        """Add job_offer to the context object."""
        context = super().get_context_data(**kwargs)
        context["job_offer"] = self.job_offer
        return context

    def get(self, request, *args, **kwargs):
        """Handle GET method and redirect if user is school."""
        self.job_offer = JobOffer.objects.get(id=kwargs["offer"])
        if request.user.is_teacher:
            return self.render_to_response(self.get_context_data())
        return redirect(reverse("dashboard:index"))

    def post(self, request, *args, **kwargs):
        """Handle POST requests and redirect if user is school."""
        if request.user.is_teacher:
            self.teacher = request.user.teacher
            form = self.get_form()
            self.job_offer = JobOffer.objects.get(id=kwargs["offer"])
            if form.is_valid():
                self.cv_file = request.FILES["curriculum"]
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        return redirect("dashboard:index")

    def form_valid(self, form):
        """Send mails if form is valid."""
        fs = FileSystemStorage()
        cv_name = fs.save(self.cv_file.name, self.cv_file)
        cv_url = fs.url(cv_name)
        self.send_mail_to_school(form, cv_url)
        return HttpResponseRedirect(self.get_success_url())

    def send_mail_to_school(self, form, cv_url):
        """Create the mail that will be send to school."""
        mail_context = {"teacher": self.teacher,
                        "motivations": form.cleaned_data["motivation"],
                        "cv_url": cv_url}
        mail = EmailMessage(
            "Melomnia: Un candidat a postulé !",
            render_to_string(self.mail_to_school_template,
                             context=mail_context),
            'candidature@melomnia.fr',
            [self.job_offer.school.user.email]
        )
        mail.content_subtype = "html"
        mail.send()
