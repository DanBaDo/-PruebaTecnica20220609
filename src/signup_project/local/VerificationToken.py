from typing import Any, get_args

from django.conf import settings
import jwt

from profiles_api.models import Profile
from .defines import TOKEN_CLAIMS, VERIFIABLE_FIELDS, VERIFIABLE_FIELDS_FLAGS, verifiable_fields_flags, MissingRequiredSecretException

class VerificationResponse:
    valid: bool
    verify_property: VERIFIABLE_FIELDS
    change_flag: VERIFIABLE_FIELDS_FLAGS
    property_spected_value: str
    profile_id: int

class VerificationToken:
    """
    Provides and validates JSON Web Token for verifiying profiles e-mail, phones, etc.

    All information for validation is included in the token on creation.

    Params:
        secret: str (optional)
    
    Usage:
        profile = Profiles.objects.get(pk=1)

        validator = VerificationToken()

        jwt = validator.new_token(profile, "email")

        validation = validator.parse_token(jwt)

        print(validation.valid)

    Methods:

        new_token(profile: Profile, verify_property: VERIFIABLE_FIELDS) -> str

        parse_token(token: str) -> dict[str, Any]

    Exceptions:

        MissingRequiredSecretException        

    """
        
    def __init__( self, **kwargs ) -> None:

        if not kwargs.get("secret") and not settings.SECRET_KEY:
            raise MissingRequiredSecretException
        else:
            self.__secret: str = kwargs.get("secret", settings.SECRET_KEY)
    
    def new_token(self, profile: Profile, verify_property: VERIFIABLE_FIELDS) -> str:
        return jwt.encode(
            {
                "iss": TOKEN_CLAIMS["ISS"],
                "aud": TOKEN_CLAIMS["AUD"],
                "sub": profile.id,
                "verify_property": verify_property,
                "property_spected_value": getattr(profile, verify_property),
            },
            self.__secret,
        )

    def parse_token(self, token: str) -> VerificationResponse:

        payload = jwt.decode(
            jwt = token,
            key = self.__secret,
            algorithms = ["HS256"],
            options = {
                "require": [
                    "verify_property",
                    "property_spected_value",
                    "sub",
                    "iss"
                ],
                "verify_iss": True,
                "verify_aud": True,
            },
            issuer = TOKEN_CLAIMS["ISS"],
            audience = TOKEN_CLAIMS["AUD"],
        )

        response = VerificationResponse()
        response.valid = (
            "verify_property" in payload and payload["verify_property"] in get_args(VERIFIABLE_FIELDS)
            and
            "property_spected_value" in payload and type(payload["property_spected_value"]) == str
            and
            "sub" in payload and type(payload["sub"]) == int
        )
        # TODO: Search for a best type hinting fit
        response.verify_property = payload["verify_property"],  # type: ignore
        response.change_flag = verifiable_fields_flags[payload["verify_property"]],  # type: ignore
        response.property_spected_value = payload["property_spected_value"],  # type: ignore
        response.profile_id =  payload["sub"], # type: ignore
        return response
