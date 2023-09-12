import pytest

from app import data_processors


def test_process_received_data(load_input_data, load_output_data):
    expected_output = data_processors.process_received_data(load_input_data)
    assert expected_output == load_output_data
