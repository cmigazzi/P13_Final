from django.core.management.base import BaseCommand
from django.core.management import call_command

from .users import SCHOOLS, TEACHERS, SUPERUSER
from accounts.models import User


class Command(BaseCommand):
    """Generates users fixtures."""

    help = "Generates users fixtures in /accounts/fixtures/users.json"

    def handle(self, *args, **kwargs):
        """Handle command."""
        for school in SCHOOLS:
            school_user = User.objects.create_user(
                        school["email"],
                        school["password"],
                        is_school=True)
            school_user.is_active = True
            school_user.save()

        for teacher in TEACHERS:
            teacher_user = User.objects.create_user(
                        teacher["email"],
                        teacher["password"],
                        is_teacher=True)
            teacher_user.is_active = True
            teacher_user.save()

        for superuser in SUPERUSER:
            super_user = User.objects.create_superuser(
                            superuser["email"],
                            superuser["password"])
            super_user.save()

        call_command("dumpdata",
                     "accounts.User",
                     output="accounts/fixtures/users.json")
