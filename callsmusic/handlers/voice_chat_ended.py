from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message

from ..callsmusic.callsmusic import remove


@Client.on_message(filters.voice_chat_ended)
async def voice_chat_ended(_, message: Message):
    try:
        remove(message.chat.id)
    except Exception:
        pass
