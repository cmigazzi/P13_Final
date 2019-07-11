import random

from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model

from .profiles import SCHOOL_TYPES
from profiles.models import School

User = get_user_model()


class Command(BaseCommand):
    """Generates profiles fixtures."""

    help = "Generates profiles fixtures in /profiles/fixtures/profiles.json"

    def handle(self, *args, **kwargs):
        """Handle command."""
        users = User.objects.filter(is_school=True)
        for user in users:
            profile = School(user=user,
                             school_type=random.choice(SCHOOL_TYPES))
            profile.save()
        call_command("dumpdata",
                     "profiles.School",
                     output="profiles/fixtures/profiles.json")
