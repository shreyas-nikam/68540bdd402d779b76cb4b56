import pytest
from definition_013e1f5df2ae43fd9e2563b76baf1d52 import F_US

@pytest.mark.parametrize("P_gen, P_spec, gamma_gen, gamma_spec, expected", [
    (0.5, 0.5, 0.5, 0.5, 0.5),
    (0.0, 0.0, 0.5, 0.5, 1.0),
    (1.0, 1.0, 0.5, 0.5, 0.0),
    (0.25, 0.75, 0.3, 0.7, 0.425),
    (0.75, 0.25, 0.7, 0.3, 0.325),
    (0.5, 0.5, 0.0, 0.0, 1.0),
    (0.5, 0.5, 1.0, 1.0, 0.0),
    (0.0, 1.0, 0.5, 0.5, 0.5),
    (1.0, 0.0, 0.5, 0.5, 0.5),
    (0.0, 0.0, 0.0, 0.0, 1.0),
    (1.0, 1.0, 1.0, 1.0, -1.0),
    (0.5, 0.5, -0.5, 0.5, 0.75),
    (0.5, 0.5, 0.5, -0.5, 0.75),
    (0.5, 0.5, 1.5, 0.5, -0.5),
    (0.5, 0.5, 0.5, 1.5, -0.5),
    (0.0, 0.0, 1.0, 1.0, 1.0), #Edge case with no progress
    (1.0, 1.0, 0.0, 0.0, 1.0), #Edge case with full progress but zero weight
    (0.5, 0.5, 1.0, 0.0, 0.5), #Edge case, only general progress matters
    (0.5, 0.5, 0.0, 1.0, 0.5), #Edge case, only specific progress matters
    (0.0, 0.0, 1.0, 0.0, 1.0), #Edge case, zero progress, only general skill is weighted
    (0.0, 0.0, 0.0, 1.0, 1.0), #Edge case, zero progress, only specific skill is weighted
    (1.0, 0.0, 1.0, 0.0, 0.0), #Edge case, full general progress, zero specific progress
    (0.0, 1.0, 0.0, 1.0, 0.0), #Edge case, full specific progress, zero general progress
    (0.3, 0.7, 0.2, 0.8, 0.2), #Typical Use case
    (-0.1, 0.5, 0.5, 0.5, ValueError),  # Invalid input for P_gen
    (0.5, -0.1, 0.5, 0.5, ValueError),  # Invalid input for P_spec
    (0.5, 0.5, -0.1, 0.5, ValueError),  # Invalid input for gamma_gen
    (0.5, 0.5, 0.5, -0.1, ValueError),  # Invalid input for gamma_spec
    (1.1, 0.5, 0.5, 0.5, ValueError),  # Invalid input for P_gen
    (0.5, 1.1, 0.5, 0.5, ValueError),  # Invalid input for P_spec
    (0.5, 0.5, 1.1, 0.5, ValueError),  # Invalid input for gamma_gen
    (0.5, 0.5, 0.5, 1.1, ValueError),  # Invalid input for gamma_spec
    ("a", 0.5, 0.5, 0.5, TypeError),  # Invalid input type for P_gen
    (0.5, "a", 0.5, 0.5, TypeError),  # Invalid input type for P_spec
    (0.5, 0.5, "a", 0.5, TypeError),  # Invalid input type for gamma_gen
    (0.5, 0.5, 0.5, "a", TypeError),  # Invalid input type for gamma_spec
])
def test_F_US(P_gen, P_spec, gamma_gen, gamma_spec, expected):
    try:
        if expected is ValueError or expected is TypeError:
            with pytest.raises(expected):
                F_US(P_gen, P_spec, gamma_gen, gamma_spec)
        else:
            assert F_US(P_gen, P_spec, gamma_gen, gamma_spec) == pytest.approx(expected)
    except Exception as e:
        if isinstance(expected, type) and issubclass(expected, Exception):
            assert isinstance(e, expected)
        else:
            raise