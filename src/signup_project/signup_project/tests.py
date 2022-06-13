from django.test import TestCase

from local.VerificationToken import Profile
from local.VerificationToken import VerificationToken

SECRET = "Not a good secret"

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

        validator = VerificationToken(secret = SECRET)
        token = validator.new_token(profile, "email")
        self.assertEqual(type(token), str)

    def test_parse_token(self) -> None:

        profile = Profile.objects.get(name="Daniel")

        validator = VerificationToken(secret = SECRET)
        token = validator.new_token(profile, "email")

        validation = validator.parse_token(token)

        self.assertEquals(validation["valid"], True)
        self.assertEquals(validation["verify_property"], "email")
        self.assertEquals(validation["property_spected_value"], profile.email)

    def test_parse_bad_token(self) -> None:
        # TODO
        pass
    
    def test_validate_data(self) -> None:
        # TODO
        pass


