import pytest
from definition_113e5a8d5eb14a4d97d11fd42bd8dcf1 import IAI

@pytest.mark.parametrize("vc_funding, r_d_spend, public_salience, expected", [
    (100, 50, 25, None),  # Example with valid inputs - Replace None with expected value if known.
    (0, 0, 0, None),      # All inputs zero - Replace None with expected value if known.
    (1000, 500, 250, None), # Large valid inputs - Replace None with expected value if known.
    (-100, 50, 25, None), # Negative VC Funding  - Replace None with expected behavior/expected exception.
    (100, -50, 25, None), # Negative R&D Spend  - Replace None with expected behavior/expected exception.
    (100, 50, -25, None), # Negative Public Salience  - Replace None with expected behavior/expected exception.
    (100, 50, 25.5, None), # Float Public Salience - Replace None with expected value if known.
    (100.5, 50, 25, None), # Float VC Funding - Replace None with expected value if known.
    (100, 50.5, 25, None), # Float R&D Spend - Replace None with expected value if known.
    ("100", 50, 25, TypeError), # String VC Funding
    (100, "50", 25, TypeError), # String R&D Spend
    (100, 50, "25", TypeError), # String Public Salience
    (None, 50, 25, TypeError), # None VC Funding
    (100, None, 25, TypeError), # None R&D Spending
    (100, 50, None, TypeError), # None Public Salience
    ([100], 50, 25, TypeError), # List VC Funding
    (100, [50], 25, TypeError), # List R&D Spending
    (100, 50, [25], TypeError), # List Public Salience
    (100, 50, 25, None)  # Same as first case, checking for consistent behavior
])
def test_IAI(vc_funding, r_d_spend, public_salience, expected):
    try:
        result = IAI(vc_funding, r_d_spend, public_salience)
        if expected is not None:
            assert result == expected
    except Exception as e:
        if isinstance(expected, type) and issubclass(expected, Exception):
            assert isinstance(e, expected)
        else:
            raise #Re-raise the exception if it wasn't expected
