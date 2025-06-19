import pytest
from definition_97d84c70f09b411d93027496911623b9 import IAI

@pytest.mark.parametrize("VC_Funding, R_D_Spend, Public_Salience, expected", [
    (1000000, 500000, 0.75, None),
    (0, 0, 0, None),
    (-100000, -50000, -0.25, None),
    (500000, 250000, 0.5, None),
    (1e6, 5e5, 0.75, None),
    (1000000.50, 500000.75, 0.75, None),
    ("1000000", "500000", "0.75", None),
    (None, None, None, TypeError),
    ([1000000], [500000], [0.75], TypeError),
    ((1000000,), (500000,), (0.75,), TypeError)

])
def test_IAI(VC_Funding, R_D_Spend, Public_Salience, expected):
    try:
        result = IAI(VC_Funding, R_D_Spend, Public_Salience)
        if expected is not None:
            assert result == expected
    except Exception as e:
        assert isinstance(e, TypeError)
