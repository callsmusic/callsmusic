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
from pyrogram.types import ChatMemberUpdated

import admins


@Client.on_chat_member_updated()
async def chat_member_updated(_, chat_member_updated: ChatMemberUpdated):
    chat = chat_member_updated.chat.id
    new = chat_member_updated.new_chat_member

    (
        admins.admins[chat].append(new.user.id)
    ) if (
        (
            new.can_manage_voice_chats
        ) and (
            new.user.id not in cache.admins[chat]
        )
    ) else (
        admins.admins[chat].remove(new.user.id)
    ) if (
        new.user.id in admins.admins[chat]
    ) else None
