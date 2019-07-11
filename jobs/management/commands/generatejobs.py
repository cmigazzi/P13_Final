import random


from django.core.management.base import BaseCommand
from django.core.management import call_command

from profiles.models import School
from jobs.models import JobOffer
from .jobs import POSITIONS, CONTRACT_TYPES, LIMIT_DATES


class Command(BaseCommand):
    """Generates users fixtures."""

    help = "Generates users fixtures in /accounts/fixtures/users.json"

    def handle(self, *args, **kwargs):
        """Handle command."""
        schools = School.objects.all()
        details = ("Lorem ipsum dolor sit amet, consectetur adipiscing "
                   "elit, sed do eiusmod tempor incididunt ut "
                   "labore et dolore magna aliqua. Ut enim ad minim "
                   "veniam, quis nostrud exercitation ullamco "
                   "laboris nisi ut aliquip ex ea commodo consequat. "
                   "Duis aute irure dolor in reprehenderit in "
                   "voluptate velit esse cillum dolore eu fugiat nulla "
                   "pariatur. Excepteur sint occaecat "
                   "cupidatat non proident, sunt in culpa qui officia "
                   "deserunt mollit anim id est laborum."),

        for school in schools:
            for i in range(1, random.randrange(3, 7)):
                job_offer = JobOffer(
                    school=school,
                    position=random.choice(POSITIONS),
                    half_hour_count=random.randint(4, 35),
                    contract_type=random.choice(CONTRACT_TYPES),
                    details=details,
                    apply_email="direction@ecole.fr",
                    limit_date=random.choice(LIMIT_DATES)
                                     )
                job_offer.save()

        call_command("dumpdata",
                     "jobs.JobOffer",
                     indent=2,
                     output="jobs/fixtures/jobs.json")
