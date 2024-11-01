import pytest
from data_visualization import parse_data, visualize_data


def test_parse_data():
    data = parse_data('example.txt')
    assert len(data) == 5
    assert data[0] == '10'
    assert data[4] == '20'


def test_visualize_data():
    data = [10, 20, 15, 25, 18]
    visualize_data(data)
    # Add a check for the plot's title or any other visible element if possible
