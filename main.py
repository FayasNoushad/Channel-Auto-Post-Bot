import os
from pyrogram import Client

FROM_CHANNELS = int(os.environ["FROM_CHANNELS"])
TO_CHAT = int(os.environ["TO_CHAT"])

FayasNoushad = Client(
    "Channel Auto Post Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)
