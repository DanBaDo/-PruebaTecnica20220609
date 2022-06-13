import os
import asyncio 
from typing import Awaitable, Iterable
from random import random

from local.defines import VERIFIABLE_FIELDS, TOKEN_DELIVERY_DATA

async def token_sender(address: str, type: VERIFIABLE_FIELDS, token: str) -> None:
    print(f"Sending {type} token to {address}: \n{token}")
    await asyncio.sleep(1+random())
    print(f"Token sent to {address}")

async def moked_token_sender(address: str, type: VERIFIABLE_FIELDS, token: str) -> None:
    print(f"Simulating to send {type} token to {address}: \n{token}")
    await asyncio.sleep(1+random())
    print(f"Token sent to {address}")

if os.environ.get("DJANGO_PRODUCTION", False) == True:
    sender = token_sender
else:
    sender = moked_token_sender

async def send_tokens(tokens_data: TOKEN_DELIVERY_DATA) -> None:
    tasks: Iterable[Awaitable] = []
    for token_data in tokens_data:
        tasks.append(
            asyncio.create_task(
                sender(token_data[0], token_data[1], token_data[2])
            )
        )
    for task in tasks:
        await task
