import pytest
from definition_068fb0a40c8a44ad8918551a9ab187c1 import H_i

@pytest.mark.parametrize("H_base, M_econ, IAI, w_econ, w_inno, expected", [
    (1.0, 1.0, 1.0, 0.5, 0.5, 1.0),
    (0.5, 1.0, 1.0, 0.5, 0.5, 0.5),
    (1.0, 0.5, 1.0, 0.5, 0.5, 0.75),
    (1.0, 1.0, 0.5, 0.5, 0.5, 0.75),
    (1.0, 0.5, 0.5, 0.5, 0.5, 0.5),
    (0.0, 1.0, 1.0, 0.5, 0.5, 0.0),
    (1.0, 0.0, 0.0, 0.5, 0.5, 0.0),
    (1.0, -1.0, 1.0, 0.5, 0.5, 0.0),  # Econ climate modifier can be negative
    (1.0, 1.0, -1.0, 0.5, 0.5, 0.0),  # AI innovation index can be negative
    (1.0, 1.0, 1.0, 0.0, 0.0, 0.0), # Weights are zero
    (1.0, 1.0, 1.0, 1.0, 0.0, 1.0), # Only Econ matters
    (1.0, 1.0, 1.0, 0.0, 1.0, 1.0), # Only Inno matters
    (1.0, 1.0, 1.0, 0.2, 0.8, 1.0), # Weights are different
    (0.5, 0.2, 0.8, 0.3, 0.7, 0.41), # Different values for all params
    (2.0, 1.0, 1.0, 0.5, 0.5, 2.0), # H_base > 1
    (1.0, 2.0, 1.0, 0.5, 0.5, 1.5), # M_econ > 1
    (1.0, 1.0, 2.0, 0.5, 0.5, 1.5), # IAI > 1
    (1.0, 1.0, 1.0, -0.5, 1.5, 1.0), # Weights outside [0,1] but sum to 1
    (1.0, 1.0, 1.0, 0.5, 0.6, 1.1),  # Weights exceeding 1 (sum = 1.1)
    (1.0, 1.0, 1.0, 0.5, -0.6, 0.4), # Weights below zero
    (1.0, 1.0, 1.0, 0.5, 0.5, 1.0),
    (1.0, 1.0, 1.0, 0.5, 0.5, 1.0),
])
def test_H_i(H_base, M_econ, IAI, w_econ, w_inno, expected):
    assert H_i(H_base, M_econ, IAI, w_econ, w_inno) == expected

@pytest.mark.parametrize("H_base, M_econ, IAI, w_econ, w_inno, expected_exception", [
    ("a", 1.0, 1.0, 0.5, 0.5, TypeError),
    (1.0, "a", 1.0, 0.5, 0.5, TypeError),
    (1.0, 1.0, "a", 0.5, 0.5, TypeError),
    (1.0, 1.0, 1.0, "a", 0.5, TypeError),
    (1.0, 1.0, 1.0, 0.5, "a", TypeError),
    (None, 1.0, 1.0, 0.5, 0.5, TypeError),
    (1.0, None, 1.0, 0.5, 0.5, TypeError),
    (1.0, 1.0, None, 0.5, 0.5, TypeError),
    (1.0, 1.0, 1.0, None, 0.5, TypeError),
    (1.0, 1.0, 1.0, 0.5, None, TypeError),
])
def test_H_i_type_errors(H_base, M_econ, IAI, w_econ, w_inno, expected_exception):
    with pytest.raises(expected_exception):
        H_i(H_base, M_econ, IAI, w_econ, w_inno)
