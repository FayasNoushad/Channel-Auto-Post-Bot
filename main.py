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

START_TEXT = """
Hello {}, I am a channel auto post telegram bot.

Made by @FayasNoushad
"""

@FayasNoushad.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True
    )

@FayasNoushad.on_message(filters.channel & (filters.media | filters.text))
async def autopost(bot, update):
    if not update.chat.id in FROM_CHANNELS:
        return
    try:
        await update.copy(chat_id=TO_CHAT)
    except Exception as error:
        print(error)
