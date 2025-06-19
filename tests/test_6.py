import pytest
from definition_76eba6bac9cd46dd8efa08be458a9001 import M_econ

@pytest.mark.parametrize("GDP_Growth, Sector_Employment, Interest_Rates, expected", [
    (2.0, 150000, 3.0, None),  # Example values, replace None with expected value once implemented
    (0.0, 100000, 5.0, None),  # Stagnant GDP growth
    (5.0, 200000, 1.0, None),  # High GDP growth, low interest rates
    (-1.0, 90000, 7.0, None), # Negative GDP Growth
    (2.5, 125000, 4.0, None), #Mid-range values
    (10.0, 250000, 0.5, None), # Edge case: very high growth, very low rates
    (-5.0, 50000, 10.0, None), # Edge case: severe recession, high rates
    (2.0, 150000.5, 3.0, None),  #Float Employment values.
    (2.0, 150000, 3.05, None),  #Float Interest Rate values
    ("abc", 150000, 3.0, TypeError), #Invalid GDP type.
    (2.0, "abc", 3.0, TypeError), #Invalid Employment type.
    (2.0, 150000, "abc", TypeError), #Invalid Interest Rate type.
    (None, 150000, 3.0, TypeError), # GDP is none.
    (2.0, None, 3.0, TypeError), # Sector employment is none.
    (2.0, 150000, None, TypeError), # Interest rates is none.
    (2, 150000, 3, None), #Int GDP, Employment, Interest rates
])
def test_M_econ(GDP_Growth, Sector_Employment, Interest_Rates, expected):
    try:
        result = M_econ(GDP_Growth, Sector_Employment, Interest_Rates)
        assert result == expected
    except Exception as e:
        assert isinstance(e, expected)
