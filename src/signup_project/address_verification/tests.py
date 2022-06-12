from django.test import TestCase

from .local.VerificationToken import Profile
from .local.VerificationToken import VerificationToken

class VerificationTokenTestCase(TestCase):
    def setUp(self) -> None:
        Profile.objects.create(
            name = "Daniel",
            surname = "Bañobre Dopico",
            email = "cosas@proton.me",
            phone = "+34616656123",
        )
    def test_token_creation(self) -> None:
        profile = Profile.objects.get(name="Daniel")
        token = VerificationToken(secret = "Not a good secret")
        token.profile = profile
        token.verify_property = "phone"
        token.property_spected_value = profile.phone
        self.assertIs(type(token.jwt), str )
    def test_parse_token(self) -> None:
        pass
    def test_parse_bad_token(self) -> None:
        pass
    def test_validate_data(self) -> None:
        pass


