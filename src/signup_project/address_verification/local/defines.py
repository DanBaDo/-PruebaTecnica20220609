from enum import Enum

class VERIFIABLE_FIELDS(Enum):
    EMAIL = 'email',
    PHONE = 'phone',

class TOKEN_CLAIMS(Enum):
    AUDIENCE = "address_verification",
    ISSUER = "address_verification",
