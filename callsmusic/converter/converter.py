import asyncio
from os import path

from ..helpers.errors import FFmpegReturnCodeError


async def convert(file_path: str) -> str:
    out = path.join('raw_files', path.basename(file_path + '.raw'))
    if path.isfile(out):
        return out
    proc = await asyncio.create_subprocess_shell(
        f'ffmpeg -y -i {file_path} -f s16le -ac 2 -ar 48000 -acodec pcm_s16le {out}',
        asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    await proc.communicate()
    if proc.returncode != 0:
        raise FFmpegReturnCodeError('FFmpeg did not return 0')
    return out
