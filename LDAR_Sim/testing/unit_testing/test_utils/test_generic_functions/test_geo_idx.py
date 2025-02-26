import numpy as np

"""Test file to unit test generic_functions.py geo_idx functionality"""
from src.utils.generic_functions import geo_idx


def test_071_geo_idx_valid():
    """Test geo_idx - Valid"""
    dd = 10.123
    dd_array = np.array([9.0, 10.0, 11.0, 12.0, 13.0])
    expected = 1
    index = geo_idx(dd, dd_array)
    assert index == expected
