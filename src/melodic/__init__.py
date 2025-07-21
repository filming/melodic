"""A Python client for fetching artist lyrical discographies."""

from .client import Melodic
from .exceptions import (
    MelodicConfigError,
    MelodicConnectionError,
    MelodicDatabaseError,
    MelodicError,
)
from .models import Album, Artist, Track

__all__ = [
    "Melodic",
    "Artist",
    "Album",
    "Track",
    "MelodicError",
    "MelodicConfigError",
    "MelodicDatabaseError",
    "MelodicConnectionError",
]
