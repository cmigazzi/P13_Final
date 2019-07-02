"""Contains unit tests for token generator."""
import datetime
import re

from django.contrib.auth.tokens import PasswordResetTokenGenerator

from accounts.tokens import TokenGenerator


class TestTokenGenerator:

    user_pk = 12
    timestamp = str(datetime.datetime.now().timestamp())

    cleaned_timestamp = "".join(re.findall(r"\d", timestamp))

    def test_is_subclass(self):
        assert issubclass(TokenGenerator, PasswordResetTokenGenerator)

    def test_make_hash_value(self):
        generator = TokenGenerator()
        token = generator._make_hash_value(self.user_pk,
                                           self.cleaned_timestamp)
        expected_token = str(self.user_pk) + str(self.cleaned_timestamp)
        assert token == expected_token
