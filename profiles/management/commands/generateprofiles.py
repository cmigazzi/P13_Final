import random

from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model

from .profiles import (SCHOOL_TYPES, PHONES, SCHOOL_NAMES,
                       FIRST_NAMES, LAST_NAMES)
from profiles.models import School, Teacher

User = get_user_model()


class Command(BaseCommand):
    """Generates profiles fixtures."""

    help = "Generates profiles fixtures in /profiles/fixtures/profiles.json"

    def handle(self, *args, **kwargs):
        """Handle command."""
        users = User.objects.all()
        for user in users:
            if user.is_school:
                profile = School(user=user,
                                 name=random.choice(SCHOOL_NAMES),
                                 phone=random.choice(PHONES),
                                 school_type=random.choice(SCHOOL_TYPES))
            elif user.is_teacher:
                profile = Teacher(user=user,
                                  first_name=random.choice(FIRST_NAMES),
                                  last_name=random.choice(LAST_NAMES),
                                  phone=random.choice(PHONES),
                                  )
            else:
                continue
            profile.save()
        call_command("dumpdata",
                     "profiles.School",
                     indent=2,
                     output="profiles/fixtures/profiles.json")
