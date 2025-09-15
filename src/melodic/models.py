from dataclasses import dataclass
from pathlib import Path


@dataclass
class ClientConfig:
    """Configuration settings for the Melodic client."""

    storage_path: str | Path | None = None
    proxies: list[str] | None = None
    max_concurrent_requests: int = 1
    request_delay: float = 3.5
    user_agent: str | None = None
    batch_save_size: int = 20
