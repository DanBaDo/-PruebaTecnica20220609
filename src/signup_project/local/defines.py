from typing import Literal, get_args, Tuple, Iterable

VERIFIABLE_FIELDS = Literal["email", "phone"]

VERIFIABLE_FIELDS_FLAGS = Literal["validated_email", "validated_phone"]

verifiable_fields_flags = dict(zip(get_args(VERIFIABLE_FIELDS), get_args(VERIFIABLE_FIELDS_FLAGS)))

TOKEN_CLAIMS = {
    "ISS": "address_verification",
    "AUD": "address_verification",
}

class MissingRequiredSecretException(Exception):
    """Raise when no secret provided by env nor parameter on instantiation."""
    pass

TOKEN_DELIVERY_DATA = Iterable[Tuple[str, VERIFIABLE_FIELDS, str]]