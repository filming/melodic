"""A Python client for fetching artist lyrical discographies."""

from .client import Melodic
from .exceptions import (
    ArtistNotFoundError,
    DiscographyNotFoundError,
    LyricsNotFoundError,
    MelodicConfigError,
    MelodicError,
    NetworkError,
    SessionNotStartedError,
)
from .models import Song, SongInfo

__all__ = [
    "Melodic",
    "MelodicError",
    "MelodicConfigError",
    "SessionNotStartedError",
    "NetworkError",
    "ArtistNotFoundError",
    "LyricsNotFoundError",
    "DiscographyNotFoundError",
    "Song",
    "SongInfo",
]
