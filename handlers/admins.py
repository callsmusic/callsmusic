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

from asyncio import QueueEmpty

from pyrogram import Client
from pyrogram.types import Message

import queues

from callsmusic import callsmusic
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only


@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    (
        await message.reply_text("Paused!")
    ) if (
        callsmusic.pause(message.chat.id)
    ) else (
        await message.reply_text("Nothing is playing!")
    )


@Client.on_message(command("resume") & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    (
        await message.reply_text("Resumed!")
    ) if (
        callsmusic.resume(message.chat.id)
    ) else (
        await message.reply_text("Nothing is paused!")
    )


@Client.on_message(command("stop") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.active_chats:
        await message.reply_text("Nothing is playing!")
    else:
        try:
            queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        await callsmusic.stop(message.chat.id)
        await message.reply_text("Cleared the queue and left the call!")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    if message.chat.id not in callsmusic.active_chats:
        await message.reply_text("Nothing is playing!")
    else:
        queues.task_done(message.chat.id)

        if queues.is_empty(message.chat.id):
            await callsmusic.stop(message.chat.id)
        else:
            await callsmusic.set_stream(
                message.chat.id, queues.get(message.chat.id)["file"]
            )

        await message.reply_text("Skipped!")


@Client.on_message(command("mute") & other_filters)
@errors
@authorized_users_only
async def mute(_, message: Message):
    result = callsmusic.mute(message.chat.id)

    (
        await message.reply_text("Muted!")
    ) if (
        result == 0
    ) else (
        await message.reply_text("Already muted!")
    ) if (
        result == 1
    ) else (
        await message.reply_text("Not in voice chat!")
    )


@Client.on_message(command("unmute") & other_filters)
@errors
@authorized_users_only
async def unmute(_, message: Message):
    result = callsmusic.unmute(message.chat.id)

    (
        await message.reply_text("Unmuted!")
    ) if (
        result == 0
    ) else (
        await message.reply_text("Not muted!")
    ) if (
        result == 1
    ) else (
        await message.reply_text("Not in voice chat!")
    )
