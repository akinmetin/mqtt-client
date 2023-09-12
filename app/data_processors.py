from datetime import datetime, timezone
import logging
from typing import Any

from app import validators

logger = logging.getLogger(__name__)


def _purge_none_keys(readings: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Purges `None` values in the given list of dicts readings data.

    Args:
        readings: List of dicts
    Returns:
        List of dicts without None key values
    """
    return [{k: v for k, v in reading.items() if v is not None}
            for reading in readings]


def _purge_empty_readings(readings: dict[str, Any]) -> dict[str, Any]:
    """
    Purges empty readings in the given list of dicts readings data.

    Args:
        readings: List of dicts
    Returns:
        List of dicts without empty readings
    """
    result = {}
    for vid, data in readings.items():
        if data:
            result[vid] = data
    return result


def _merge_readings_data(
        reading_data: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Merge multiple reading data from same vendors into same `_vid` key.

    Args:
        readings_data: List of reading data dicts
    Returns:
        List of merged reading data
    """
    merged_data = {}

    for reading in reading_data:
        vid = reading["_vid"]
        if vid not in merged_data:
            merged_data[vid] = {}

        for k, v in reading.items():
            if k.startswith("_"):
                continue

            if k in merged_data[vid]:
                merged_data[vid][k] = max(merged_data[vid][k], v) \
                    if isinstance(k, (int, float)) else v
            else:
                merged_data[vid][k] = v

    merged_data = _purge_empty_readings(merged_data)
    return merged_data


def _convert_timestamp_to_iso_format(timestamp: int) -> str:
    """
    Converts timestamp in Unix epoch seconds to an ISO 8601 formatted date
    and time string.

    Args:
        timestamp: Int Unix epoch seconds
    Returns:
        ISO 8601 formatted date string
    """
    dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    return dt.isoformat()


def process_received_data(data: dict) -> dict[str, Any]:
    """
    Entrypoint to process a received raw data.

    Args:
        data: Raw data from the MQTT broker
    Returns:
        Dict of validated and processed data
    """
    try:
        validators.validate_vids(data["r"])
    except KeyError:
        logger.warn("Data is missing _vid field", data=data)

    filtered_readings_data = _purge_none_keys(data["r"])

    return {
        "time": _convert_timestamp_to_iso_format(data["t"]),
        "data": _merge_readings_data(filtered_readings_data)
    }
