# Calls Music 1 - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  Roj Serbest

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""I am an open-source @CallsMusic bot, I let you play music in your group’s voice chat.

The commands I currently support are:

/play - play the replied audio file or YouTube video
/pause - pause the audio stream
/resume - resume the audio stream
/skip - skip the current audio stream
/mute - mute the userbot
/unmute - unmute the userbot
/stop - clear the queue and remove the userbot from the call""",
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
