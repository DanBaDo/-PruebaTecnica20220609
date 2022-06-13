from typing import Literal

VERIFIABLE_FIELDS = Literal["email", "phone"]

VERIFIABLE_FIELDS_FLAGS = {
    "email": "validated_email",
    "phones": "validated_phone"
}

TOKEN_CLAIMS = {
    "ISS": "address_verification",
    "AUD": "address_verification",
}

class MissingRequiredSecretException(Exception):
    """Raise when no secret provided by env nor parameter on instantiation."""
    pass
