# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Channel-Auto-Post-Bot/blob/main/LICENSE

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

FROM_CHANNELS = set(int(x) for x in os.environ.get("FROM_CHANNELS", "").split())
TO_CHAT = int(os.environ["TO_CHAT"])

# filters for auto post
FILTER_TEXT = bool(os.environ.get("FILTER_TEXT", True))
FILTER_AUDIO = bool(os.environ.get("FILTER_AUDIO", True))
FILTER_DOCUMENT = bool(os.environ.get("FILTER_DOCUMENT", True))
FILTER_PHOTO = bool(os.environ.get("FILTER_PHOTO", True))
FILTER_STICKER = bool(os.environ.get("FILTER_STICKER", True))
FILTER_VIDEO = bool(os.environ.get("FILTER_VIDEO", True))
FILTER_ANIMATION = bool(os.environ.get("FILTER_ANIMATION", True))
FILTER_VOICE = bool(os.environ.get("FILTER_VOICE", True))
FILTER_VIDEO_NOTE = bool(os.environ.get("FILTER_VIDEO_NOTE", True))
FILTER_CONTACT = bool(os.environ.get("FILTER_CONTACT", True))
FILTER_LOCATION = bool(os.environ.get("FILTER_LOCATION", True))
FILTER_VENUE = bool(os.environ.get("FILTER_VENUE", True))
FILTER_POLL = bool(os.environ.get("FILTER_POLL", True))
FILTER_GAME = bool(os.environ.get("FILTER_GAME", True))

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
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Channel', url='https://telegram.me/FayasNoushad'),
        InlineKeyboardButton('Feedback', url='https://telegram.me/TheFayas')
        ],[
        InlineKeyboardButton('Source Code', url='https://github.com/FayasNoushad/Channel-Auto-Post-Bot')
        ]]
    )

@FayasNoushad.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )

@FayasNoushad.on_message(
    filters.channel & (
        filters.text if FILTER_TEXT else None |
        filters.audio if FILTER_AUDIO else None |
        filters.document if FILTER_DOCUMENT else None |
        filters.photo if FILTER_PHOTO else None |
        filters.sticker if FILTER_STICKER else None |
        filters.video if FILTER_VIDEO else None |
        filters.animation if FILTER_ANIMATION else None |
        filters.voice if FILTER_VOICE else None |
        filters.video_note if FILTER_VIDEO_NOTE else None |
        filters.contact if FILTER_CONTACT else None |
        filters.location if FILTER_LOCATION else None |
        filters.venue if FILTER_VENUE else None |
        filters.poll if FILTER_POLL else None |
        filters.game if FILTER_GAME else None
    )
)
async def autopost(bot, update):
    if (not update.chat.id in FROM_CHANNELS) or (not TO_CHAT) or ((update.chat.id in FROM_CHANNELS) and (not TO_CHAT)):
        return
    try:
        await update.copy(chat_id=TO_CHAT)
    except Exception as error:
        print(error)
