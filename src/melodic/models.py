"""Dataclasses for representing song data."""

from dataclasses import dataclass


@dataclass(frozen=True)
class SongInfo:
    """A temporary object holding a song's URL and metadata."""

    artist: str
    album: str
    title: str
    url: str


@dataclass(frozen=True)
class Song:
    """The final representation of a song, including its lyrics."""

    artist: str
    album: str
    title: str
    lyrics: str
    url: str
