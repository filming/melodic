import logging
import types

from .models import ClientConfig

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class Melodic:
    """An asynchronous client for fetching lyrical discographies of music artists."""

    def __init__(self, config: ClientConfig | None = None) -> None:
        """Initialize the Melodic client.

        Args:
            config: Configuration settings for the client.
        """
        if config is None:
            config = ClientConfig()

        logger.info("Melodic instance has been initialized.")

    async def __aenter__(self) -> "Melodic":
        """Enter async context and intialize resources.

        Returns:
            The initialized Melodic instance.
        """
        logger.debug("Melodic context entered.")
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None:
        """Exit async context and close resources."""
        logger.debug("Melodic context exited.")
