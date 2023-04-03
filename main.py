import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


load_dotenv()

# chat details
FROM_CHANNELS = set(int(x)
                    for x in os.environ.get("FROM_CHANNELS", "").split())
TO_CHATS = set(int(x) for x in os.environ.get("TO_CHATS", "").split())

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

# for copy
AS_COPY = bool(os.environ.get("AS_COPY", True))
REPLY_MARKUP = bool(os.environ.get("REPLY_MARKUP", False))

# bot informations
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

Bot = Client(
    "Channel Auto Post Bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

START_TEXT = """Hello {}, \
I am a channel auto post telegram bot.

I can send any messages from one or more channels \
to one or more chats (including users, groups, channels)"""

BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Feedback", url="https://telegram.me/FayasNoushad"),
            InlineKeyboardButton(
                text="Source Code", url="https://github.com/FayasNoushad/Channel-Auto-Post-Bot")
        ]
    ]
)


@Bot.on_message(filters.private & filters.command("start"))
async def start(_, message):
    await message.reply_text(
        text=START_TEXT.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )


@Bot.on_message(
    filters.channel & (
        filters.text |
        filters.audio |
        filters.document |
        filters.photo |
        filters.sticker |
        filters.video |
        filters.animation |
        filters.voice |
        filters.video_note |
        filters.contact |
        filters.location |
        filters.venue |
        filters.poll |
        filters.game
    )
)
async def autopost(_, message):

    if len(FROM_CHANNELS) == 0 or len(TO_CHATS) == 0 or message.chat.id not in FROM_CHANNELS:
        return

    if not (
        (
            message.text and FILTER_TEXT
        ) or (
            message.audio and FILTER_AUDIO
        ) or (
            message.document and FILTER_DOCUMENT
        ) or (
            message.photo and FILTER_PHOTO
        ) or (
            message.sticker and FILTER_STICKER
        ) or (
            message.video and FILTER_VIDEO
        ) or (
            message.animation and FILTER_ANIMATION
        ) or (
            message.voice and FILTER_VOICE
        ) or (
            message.video_note and FILTER_VIDEO_NOTE
        ) or (
            message.contact and FILTER_CONTACT
        ) or (
            message.location and FILTER_LOCATION
        ) or (
            message.venue and FILTER_VENUE
        ) or (
            message.poll and FILTER_POLL
        ) or (
            message.game and FILTER_GAME
        )
    ):
        return

    try:
        for chat_id in TO_CHATS:
            if AS_COPY:
                if REPLY_MARKUP:
                    await message.copy(
                        chat_id=chat_id,
                        reply_markup=message.reply_markup
                    )
                else:
                    await message.copy(chat_id=chat_id)
            else:
                await message.forward(chat_id=chat_id)
    except Exception as error:
        print(error)


Bot.run()
