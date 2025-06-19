import pytest
from definition_541b601200264ae9a21f0c796e4f4dfd import H_i

@pytest.mark.parametrize("H_base, M_econ, IAI, w_econ, w_inno, expected", [
    (1.0, 1.0, 1.0, 0.5, 0.5, 1.0),
    (0.5, 1.0, 1.0, 0.5, 0.5, 0.5),
    (1.0, 0.5, 1.0, 0.5, 0.5, 0.75),
    (1.0, 1.0, 0.5, 0.5, 0.5, 0.75),
    (1.0, 0.5, 0.5, 0.5, 0.5, 0.5),
    (0.0, 1.0, 1.0, 0.5, 0.5, 0.0),
    (1.0, 1.0, 1.0, 0.0, 1.0, 1.0),
    (1.0, 1.0, 1.0, 1.0, 0.0, 1.0),
    (1.0, 2.0, 1.0, 0.5, 0.5, 1.5),
    (1.0, 1.0, 2.0, 0.5, 0.5, 1.5),
    (1.0, 2.0, 2.0, 0.5, 0.5, 2.0),
    (0.5, 0.5, 0.5, 0.5, 0.5, 0.25),
    (1.0, 1.0, 1.0, 0.2, 0.8, 1.0),
    (1.0, 1.0, 1.0, 0.8, 0.2, 1.0),
    (1.0, 0.0, 1.0, 0.5, 0.5, 0.5),
    (1.0, 1.0, 0.0, 0.5, 0.5, 0.5),
    (1.0, -1.0, 1.0, 0.5, 0.5, 0.0),  # M_econ can be negative
    (1.0, 1.0, -1.0, 0.5, 0.5, 0.0),  # IAI can be negative
    (2.0, 1.0, 1.0, 0.5, 0.5, 2.0),
    (1.0, 1.0, 1.0, 0.5, 0.5, 1.0),
    (10.0, 5.0, 2.0, 0.3, 0.7, 29.0),
])
def test_H_i_valid_inputs(H_base, M_econ, IAI, w_econ, w_inno, expected):
    assert H_i(H_base, M_econ, IAI, w_econ, w_inno) == expected

@pytest.mark.parametrize("H_base, M_econ, IAI, w_econ, w_inno, expected_exception", [
    ("invalid", 1.0, 1.0, 0.5, 0.5, TypeError),
    (1.0, "invalid", 1.0, 0.5, 0.5, TypeError),
    (1.0, 1.0, "invalid", 0.5, 0.5, TypeError),
    (1.0, 1.0, 1.0, "invalid", 0.5, TypeError),
    (1.0, 1.0, 1.0, 0.5, "invalid", TypeError),
    (None, 1.0, 1.0, 0.5, 0.5, TypeError),
    (1.0, None, 1.0, 0.5, 0.5, TypeError),
    (1.0, 1.0, None, 0.5, 0.5, TypeError),
    (1.0, 1.0, 1.0, None, 0.5, TypeError),
    (1.0, 1.0, 1.0, 0.5, None, TypeError),
    (1.0, 1.0, 1.0, 0.5, 0.5, None), # No exception expected
])
def test_H_i_invalid_inputs(H_base, M_econ, IAI, w_econ, w_inno, expected_exception):
    if expected_exception:
        with pytest.raises(expected_exception):
            H_i(H_base, M_econ, IAI, w_econ, w_inno)
    else:
        H_i(H_base, M_econ, IAI, w_econ, w_inno)