from os import path

from youtube_dl import YoutubeDL

from ..config import DURATION_LIMIT
from ..helpers.errors import DurationLimitError

ytdl = YoutubeDL(
    {
        'format': 'bestaudio/best',
        'geo-bypass': True,
        'nocheckcertificate': True,
        'outtmpl': 'downloads/%(id)s.%(ext)s',
    },
)


def download(url: str) -> str:
    info = ytdl.extract_info(url, False)
    duration = round(info['duration'] / 60)
    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f'Videos longer than {DURATION_LIMIT} minute(s) are not allowed, '
            f'the provided video is {duration} minute(s)',
        )
    ytdl.download([url])
    return path.join('downloads', f"{info['id']}.{info['ext']}")
