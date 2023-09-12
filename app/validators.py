from typing import Any


def validate_vids(readings_data: list[dict[str, Any]]) -> None:
    """
    Validate if the all raw readings data include `_vid` identifier.

    Args:
        readings_data: List of dicts of raw readings data
    Returns:
        Raises KeyError if `_vid` is not present
    """
    for reading in readings_data:
        if not reading.get("_vid"):
            raise KeyError("_vid cannot be found in the payload")
