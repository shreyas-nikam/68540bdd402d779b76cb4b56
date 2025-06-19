import pytest
from definition_b8d4c69db125445a89e5f3196c966edd import V_i

@pytest.mark.parametrize("F_HC, F_CR, F_US, expected", [
    (0.5, 0.5, 0.5, None),  # Basic test case
    (1.0, 1.0, 1.0, None),  # All factors at maximum
    (0.0, 0.0, 0.0, None),  # All factors at minimum
    (0.75, 0.25, 0.5, None), # Uneven distribution
    (0.33, 0.33, 0.34, None), # Close to equal distribution
    (-0.5, 0.5, 0.5, None), #Negative F_HC
    (0.5, -0.5, 0.5, None), #Negative F_CR
    (0.5, 0.5, -0.5, None), #Negative F_US
    (2.0, 0.5, 0.5, None),  # F_HC above 1
    (0.5, 2.0, 0.5, None),  # F_CR above 1
    (0.5, 0.5, 2.0, None),  # F_US above 1
    (0.0, 1.0, 0.0, None),  # Edge case: F_HC and F_US are 0
    (1.0, 0.0, 0.0, None),  # Edge case: F_CR and F_US are 0
    (0.0, 0.0, 1.0, None),  # Edge case: F_HC and F_CR are 0
    ("a", 0.5, 0.5, TypeError),  # Invalid type for F_HC
    (0.5, "a", 0.5, TypeError),  # Invalid type for F_CR
    (0.5, 0.5, "a", TypeError),  # Invalid type for F_US
    (None, 0.5, 0.5, TypeError), # None input
    (0.5, None, 0.5, TypeError), # None input
    (0.5, 0.5, None, TypeError), # None input
    ([], 0.5, 0.5, TypeError), # List input
    (0.5, [], 0.5, TypeError), # List input
    (0.5, 0.5, [], TypeError), # List input
])
def test_V_i(F_HC, F_CR, F_US, expected):
    try:
        V_i(F_HC, F_CR, F_US) # Call the function, no assertions since pass
    except Exception as e:
        assert isinstance(e, expected)