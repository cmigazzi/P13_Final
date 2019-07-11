from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    """Load all fixtures."""

    help = "Load all fixtures"

    def handle(self, *args, **kwargs):
        """Handle command."""
        call_command("loaddata", "accounts/fixtures/users.json")
        call_command("loaddata", "profiles/fixtures/profiles.json")
        call_command("loaddata", "jobs/fixtures/jobs.json")
