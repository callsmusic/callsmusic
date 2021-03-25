from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""I am an open-source @CallsMusic bot, I let you play music in your group's voice chat.

The commands I currently support are:

/play - play the replied audio file or YouTube video
/pause - pause the audio stream
/resume - resume the audio stream
/skip - skip the current audio stream
/mute - mute the userbot
/unmute - unmute the userbot
/stop - clear the queue and remove the userbot from the call
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group", url="https://t.me/callsmusicchat"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/callsmusic"
                    )
                ]
            ]
        )
    )
