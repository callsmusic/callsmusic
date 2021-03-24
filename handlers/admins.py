from asyncio import QueueEmpty

from pyrogram import Client
from pyrogram.types import Message

from callsmusic import callsmusic, queues

from helpers.filters import command
from helpers.decorators import errors, authorized_users_only


@Client.on_message(command(["pause", "p"]))
@errors
@authorized_users_only
async def pause(_, message: Message):
    if callsmusic.pause(message.chat.id):
        await message.reply_text("⏸ Paused")
    else:
        await message.reply_text("❗️ Nothing is playing")


@Client.on_message(command(["resume", "r"]))
@errors
@authorized_users_only
async def resume(_, message: Message):
    if callsmusic.resume(message.chat.id):
        await message.reply_text("🎧 Resumed")
    else:
        await message.reply_text("❗️ Nothing is paused")


@Client.on_message(command(["stop", "s"]))
@errors
@authorized_users_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.active_chats:
        await message.reply_text("❗️ Nothing is playing")
    else:
        try:
            queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        callsmusic.stop(message.chat.id)
        await message.reply_text("✅ Cleared the queue and left the call")


@Client.on_message(command(["skip", "f"]))
@errors
@authorized_users_only
async def skip(_, message: Message):
    if message.chat.id not in callsmusic.active_chats:
        await message.reply_text("❗️ Nothing is playing")
    else:
        queues.task_done(message.chat.id)

        if queues.is_empty(message.chat.id):
            await callsmusic.stop(message.chat.id)
        else:
            await callsmusic.set_stream(
                message.chat.id, queues.get(message.chat.id)["file"]
            )

        await message.reply_text("Skipped.")


@Client.on_message(command(["mute", "m"]))
@errors
@authorized_users_only
async def mute(_, message: Message):
    result = callsmusic.mute(message.chat.id)

    if result == 0:
        await message.reply_text("🔇 Muted")
    elif result == 1:
        await message.reply_text("🔇 Already muted")
    elif result == 2:
        await message.reply_text("❗️ Not in voice chat")


@Client.on_message(command(["unmute", "u"]))
@errors
@authorized_users_only
async def unmute(_, message: Message):
    result = callsmusic.unmute(message.chat.id)

    if result == 0:
        await message.reply_text("🔈 Unmuted")
    elif result == 1:
        await message.reply_text("🔈 Already unmuted")
    elif result == 2:
        await message.reply_text("❗️ Not in voice chat")
