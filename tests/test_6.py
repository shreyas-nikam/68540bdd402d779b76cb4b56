import pytest
from definition_6a21fce14508444b81d772bf8ea2f9d5 import M_econ

@pytest.mark.parametrize("gdp_growth, sector_employment, interest_rates, expected", [
    (2.0, 0.5, 0.05, None),
    (3.5, 0.7, 0.03, None),
    (1.0, 0.3, 0.07, None),
    (0.0, 0.0, 0.10, None),
    (-1.0, -0.1, 0.12, None),
    (5.0, 1.0, 0.01, None),
    (-2.0, -0.5, 0.15, None),
    (2.5, 0.6, 0.04, None),
    (1.5, 0.4, 0.06, None),
    (3.0, 0.8, 0.02, None),
    (0.5, 0.2, 0.08, None),
    (-0.5, -0.2, 0.11, None),
    (4.0, 0.9, 0.00, None),
    (-3.0, -0.8, 0.20, None),
    (1.7, 0.35, 0.055, None),
    (2.8, 0.75, 0.025, None),
    (0.3, 0.15, 0.085, None),
    (-0.3, -0.15, 0.115, None),
    (3.7, 0.85, 0.005, None),
    (-2.7, -0.75, 0.175, None),
    ("abc", 0.5, 0.05, TypeError),
    (2.0, "def", 0.05, TypeError),
    (2.0, 0.5, "ghi", TypeError),
    (None, 0.5, 0.05, TypeError),
    (2.0, None, 0.05, TypeError),
    (2.0, 0.5, None, TypeError),
    ([1,2], 0.5, 0.05, TypeError),
    (2.0, [1,2], 0.05, TypeError),
    (2.0, 0.5, [1,2], TypeError)
])
def test_M_econ(gdp_growth, sector_employment, interest_rates, expected):
    try:
        result = M_econ(gdp_growth, sector_employment, interest_rates)
        assert result is None # Since the function has pass, the result will be None
    except Exception as e:
        assert isinstance(e, expected)
