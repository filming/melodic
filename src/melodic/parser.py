import re
import unicodedata

from .constants import BASE_URL
from .exceptions import MelodicError


def get_artist_url(artist_name: str) -> str:
    """Construct the URL for an artist's page.

    Args:
        artist_name: The name of the artist.

    Returns:
        The full URL for the artist's page.
    """
    cleaned_name = _clean_artist_name(artist_name)
    return f"{BASE_URL}/{cleaned_name[0]}/{cleaned_name}.html"


def _clean_artist_name(name: str) -> str:
    """Normalize an artist's name for the URL path.

    Args:
        name: The raw artist name.

    Returns:
        The URL-safe artist name.

    Raises:
        MelodicError: If the name is empty or becomes empty after cleaning.
    """
    if not name or not name.strip():
        raise MelodicError("Artist name cannot be empty.")

    # Normalize to remove accents (e.g., 'é' -> 'e')
    try:
        normalized = unicodedata.normalize("NFKD", name)
        ascii_name = normalized.encode("ASCII", "ignore").decode("utf-8")
    except Exception as e:
        raise MelodicError(f"Failed to normalize artist name: {name}") from e

    # Perform common substitutions (e.g., Ke$ha -> kesha)
    substituted_name = ascii_name.replace("$", "s")

    # Clean to keep only lowercase letters and numbers
    cleaned = re.sub(r"[^a-z0-9]", "", substituted_name.lower())

    if not cleaned:
        raise MelodicError(
            f"Cleaning artist name '{name}' resulted in an empty string."
        )

    return cleaned
