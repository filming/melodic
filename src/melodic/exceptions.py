class MelodicError(Exception):
    """A base exception for general library errors."""


class ConfigError(MelodicError):
    """Raise for configuration related errors."""
