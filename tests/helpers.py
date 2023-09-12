import json


def load_json_data(file_path: str) -> dict:
    """
    Loads JSON data from a file.

    Args:
        file_path: Full file path of a JSON file
    Returns:
        Dict of the JSON file contents
    """
    with open(file_path, "r") as file:
        json_data = json.load(file)
    return json_data
