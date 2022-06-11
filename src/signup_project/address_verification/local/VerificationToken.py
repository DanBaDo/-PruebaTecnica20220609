import os

import jwt

from signup_project.profiles_api.models import Profile
from .defines import VERIFIABLE_FIELDS, TOKEN_CLAIMS

class VerificationToken:
    """
    Provides and validates JSON Web Token for verifiying profiles e-mail, phones, etc.

    All information for validation is included in the token on creation.
    
    Usage:
        `VerificationToken( token: str = "", secret: str = os.environ.get('DJANGO_SECRET_KEY'))`

    Properties:
        jwt: str

            * Getter for build new JWT based in current properties values.
            * Setter for object properties basis JWT provided.
        
        verify_property: VERIFIABLE_FIELDS

            Name of Profile file for being verificated.
        
        property_spected_value: str

            Spected value for virified property.

        profile: Profile

            Verification related Profile object

    Methods:

        verify_object_data() -> bool

            Compares value for verified property on token and object


    Exceptions

    """
        
    verify_property: VERIFIABLE_FIELDS
    property_spected_value: str
    profile: Profile

    def __init__( self, **kwargs ) -> None:


        if not kwargs.get("secret") and not os.environ.get('DJANGO_SECRET_KEY'):
            raise Exception('"secret" option or DJANGO_SECRET_KEY environment variable is required')
        else:
            self.__secret: str = kwargs.get("secret", os.environ.get('DJANGO_SECRET_KEY'))

        if type(kwargs.get("token")) == str:
            payload: dict = jwt.decode(
                kwargs.get("token", ""),
                os.environ.get('DJANGO_SECRET_KEY', ""),
                options={
                    """
                    https://www.rfc-editor.org/rfc/rfc7519.html#page-9
                    field: verified field label
                    value: spected veried field value
                    """
                    "require": ["iss", "aud", "sub", "field", "value"],
                    "verify_aud": True,
                    "audience": TOKEN_CLAIMS.AUDIENCE,
                    "verify_iss": True,
                    "issuer": TOKEN_CLAIMS.ISSUER,
                }
            )
            self.verify_property = payload["field"]
            self.property_spected_value = payload["value"]
            self.profile = Profile.objects.get(payload["sub"])
    
    @property
    def jwt(self) -> str:
        if self.profile and self.verify_property and self.property_spected_value:
            return jwt.encode(
                {
                    "iss": TOKEN_CLAIMS.ISSUER,
                    "aud": TOKEN_CLAIMS.AUDIENCE,
                    "sub": self.profile.id,
                    "field": self.verify_property,
                    "value": self.property_spected_value,
                },
                os.environ.get('DJANGO_SECRET_KEY', "")
            )
        else:
            raise Exception("There's not profile, field and value to verify.")

    @jwt.setter
    def jwt(self, **kwargs):
        self.__init__( **kwargs)

    def verify_object_data(self) -> bool:
        return self.property_spected_value == getattr(self.profile, str(self.verify_property))