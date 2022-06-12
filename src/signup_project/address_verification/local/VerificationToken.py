import os

import jwt

from profiles_api.models import Profile
from .defines import VERIFIABLE_FIELDS, TOKEN_CLAIMS, MissingRequiredPropertiesException, MissingRequiredSecretException

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

        MissingRequiredSecret

        MissingRequiredProperties
        
        PyJWT exceptions:
            https://pyjwt.readthedocs.io/en/stable/api.html#exceptions


    """
        
    verify_property: VERIFIABLE_FIELDS
    property_spected_value: str
    profile: Profile

    def __init__( self, **kwargs ) -> None:

        if not kwargs.get("secret") and not os.environ.get('DJANGO_SECRET_KEY'):
            raise MissingRequiredSecretException
        else:
            self.__secret: str = kwargs.get("secret", os.environ.get('DJANGO_SECRET_KEY'))

        if type(kwargs.get("token")) == str:
            payload: dict = jwt.decode(
                jwt = kwargs.get("token", ""),
                key = self.__secret,
                algorithms = ["HS256"]
            )
            print(Profile.objects.get(payload["sub"]))
            self.verify_property = payload["field"]
            self.property_spected_value = payload["value"]
            self.profile = Profile.objects.get(payload["sub"])

    def __str__(self) -> str:
        return f"Profile: {self.profile.name} - Property: {self.verify_property} - Value: {self.property_spected_value}"
    
    @property
    def jwt(self) -> str:

        try:
            self.profile and self.verify_property and self.property_spected_value
        except AttributeError:
            raise MissingRequiredPropertiesException

        return jwt.encode(
            {
                #"iss": TOKEN_CLAIMS.ISSUER.value[0],
                #"aud": TOKEN_CLAIMS.AUDIENCE.value[0],
                "sub": self.profile.id,
                "field": self.verify_property,
                "value": self.property_spected_value,
            },
            self.__secret,
        )

    @jwt.setter
    def jwt(self, **kwargs):
        self.__init__( **kwargs)

    def verify_object_data(self) -> bool:
        return self.property_spected_value == getattr(self.profile, str(self.verify_property))