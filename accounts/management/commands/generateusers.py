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
            school["is_school"] = True
            school["is_active"] = True

            user = User(**school)
            user.save()

        for teacher in TEACHERS:
            teacher["is_teacher"] = True
            teacher["is_active"] = True

            user = User(**teacher)
            user.save()

        for superuser in SUPERUSER:
            superuser["is_admin"] = True
            superuser["is_active"] = True

            user = User(**superuser)
            user.save()

        call_command("dumpdata",
                     "accounts.User",
                     output="accounts/fixtures/users.json")
