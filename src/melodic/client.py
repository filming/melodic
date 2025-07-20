"""Provide a Python client for fetching artist lyrical discographies."""

import logging
import types
from pathlib import Path

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class Melodic:
    """A Python client for fetching artist lyrical discographies.

    This library provides an asynchronous interface to retrieve complete
    artist discographies from AZLyrics, including album metadata and song
    lyrics, with built-in database storage, proxy support, and robust error
    handling.
    """

    def __init__(
        self,
        storage_path: str | Path | None = None,
        proxies: list[str] | None = None,
        max_concurrent_requests: int = 10,
        delay_per_request: float = 3.5,
    ) -> None:
        """Initialize the Melodic instance.

        Args:
            storage_path: An optional path for database storage.
            proxies: An optional list of proxy strings to use for requests.
            max_concurrent_requests: Maximum number of concurrent requests when
                using proxies.
            delay_per_request: Delay in seconds between requests.
        """
        self._storage_path = storage_path
        self._proxies = proxies

        logger.info("Melodic instance has been initialized.")

    async def __aenter__(self) -> "Melodic":
        """Enter the async context manager, initializing resources."""
        logger.debug("Melodic context entered.")
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None:
        """Exit the async context manager, closing resources."""
        logger.debug("Melodic context exited.")

    async def get_discography(self, artist_name: str) -> None:
        """Fetch and process the complete discography for the given artist.

        Args:
            artist_name: The name of the artist whose discography to fetch.
        """
        logger.info("Fetching discography for artist: %s", artist_name)
