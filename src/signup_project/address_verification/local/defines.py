from enum import Enum

# TODO: apply to VerificationToken
class VERIFIABLE_FIELDS(Enum):
    EMAIL = 'email',
    PHONE = 'phone',

# TODO: apply to VerificationToken
class TOKEN_CLAIMS(Enum):
    AUDIENCE = "address_verification",
    ISSUER = "address_verification",

class MissingRequiredSecretException(Exception):
    """Raise when no secret provided by env nor parameter on instantiation."""
    pass

class MissingRequiredPropertiesException(Exception):
    """Raise when trying to get a JWT whitout provide all required data."""
    pass