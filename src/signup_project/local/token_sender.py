import time
from random import random

from local.defines import VERIFIABLE_FIELDS

def token_sender(address: str, type: VERIFIABLE_FIELDS, token: str) -> None:
    time.sleep(random()*2)
    print(f"Sent {type} to {address}: \n{token}")

def moked_token_sender(address: str, type: VERIFIABLE_FIELDS, token: str) -> None:
    time.sleep(random()*2)
    print(f"Simulating send {type} to {address}: \n{token}")