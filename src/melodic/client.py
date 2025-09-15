import logging
import types
from pathlib import Path

from .network import NetworkManager
from .storage import StorageManager

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class Melodic:
    """An asynchronous client for fetching lyrical discographies of music artists."""

    def __init__(
        self,
        *,
        storage_path: str | Path | None = None,
        proxies: list[str] | None = None,
        max_concurrent_requests: int = 10,
        request_delay: float = 3.5,
        user_agent: str | None = None,
        batch_save_size: int = 20,
    ) -> None:
        """Initialize the Melodic client.

        Args:
            storage_path: The file path where the SQLite database will be stored.
            proxies: A list of proxy strings (e.g., "http://user:pass@host:port").
            max_concurrent_requests: The maximum number of concurrent requests.
            request_delay: The cooldown period for a proxy after it has been used.
            user_agent: A custom User-Agent string for network requests.
            batch_save_size: The number of songs to accumulate in memory before
                saving them to the database.
        """
        self._network_manager = NetworkManager(
            proxies=proxies,
            max_concurrent_requests=max_concurrent_requests,
            request_delay=request_delay,
            user_agent=user_agent,
        )
        self._storage_manager = StorageManager(storage_path) if storage_path else None
        self._batch_save_size = batch_save_size
        self._in_context = False

        logger.info("Melodic instance has been initialized.")

    async def __aenter__(self) -> "Melodic":
        """Enter async context and intialize resources.

        Returns:
            The initialized Melodic instance.
        """
        await self._network_manager.start()
        if self._storage_manager:
            await self._storage_manager.start()

        self._in_context = True
        logger.debug("Melodic context entered.")
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None:
        """Exit async context and close resources."""
        await self._network_manager.stop()
        if self._storage_manager:
            await self._storage_manager.stop()

        self._in_context = False
        logger.debug("Melodic context exited.")
