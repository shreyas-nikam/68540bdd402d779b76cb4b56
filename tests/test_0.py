import pytest
from definition_f586e922e5f6411493dc2c193caa7d0d import V_i

@pytest.mark.parametrize("F_HC, F_CR, F_US, expected", [
    (1, 1, 1, None),
    (0, 0, 0, None),
    (-1, -1, -1, None),
    (10, 5, 2, None),
    (0.5, 0.5, 0.5, None),
    (1.0, 1.0, 1.0, None),
    (0.0, 0.0, 0.0, None),
    (1, 0, 0, None),
    (0, 1, 0, None),
    (0, 0, 1, None),
    (1, 1, 0, None),
    (1, 0, 1, None),
    (0, 1, 1, None),
    (1, 0.5, 0.25, None),
    (0.25, 0.5, 1, None),
    (1.0, 0.0, -1.0, None),
    (-1.0, 0.0, 1.0, None)
])
def test_V_i(F_HC, F_CR, F_US, expected):
    """Test cases for V_i function."""
    assert V_i(F_HC, F_CR, F_US) == expected
