import pytest

from tests.helpers import load_json_data


@pytest.fixture
def load_input_data():
    return load_json_data("tests/data/input.json")


@pytest.fixture
def load_output_data():
    return load_json_data("tests/data/output.json")
