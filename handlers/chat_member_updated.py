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
    (
        admins.admins[chat_member_updated.chat.id].append(
            chat_member_updated.new_chat_member.user.id
        )
    ) if (
        (
            chat_member_updated.new_chat_member.can_manage_voice_chats
        ) and (
            (
                chat_member_updated.new_chat_member.user.id
            ) not in admins.admins[chat_member_updated.chat.id]
        )
    ) else (
        admins.admins[chat_member_updated.chat.id].remove(
            chat_member_updated.new_chat_member.user.id
        )
    ) if (
        (
            chat_member_updated.new_chat_member.user.id
        ) in admins.admins[chat_member_updated.chat.id]
    ) else None
