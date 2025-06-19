import pytest
from definition_3c54f2f598af49de82bd39c9daf9ef14 import F_US

@pytest.mark.parametrize("P_gen, P_spec, gamma_gen, gamma_spec, expected", [
    (0.5, 0.5, 0.5, 0.5, 0.5),
    (0.0, 0.0, 0.5, 0.5, 1.0),
    (1.0, 1.0, 0.5, 0.5, 0.0),
    (0.5, 0.5, 0.0, 0.0, 1.0),
    (0.5, 0.5, 1.0, 1.0, -0.0),
    (0.2, 0.8, 0.3, 0.7, 0.3),
    (0.8, 0.2, 0.7, 0.3, 0.3),
    (0.0, 1.0, 0.5, 0.5, 0.5),
    (1.0, 0.0, 0.5, 0.5, 0.5),
    (0.0, 0.0, 0.0, 0.0, 1.0),
    (1.0, 1.0, 1.0, 1.0, -1.0),
    (0.5, 0.5, 0.25, 0.75, 0.375),
    (0.5, 0.5, 0.75, 0.25, 0.375),
    (0.0, 0.0, 1.0, 1.0, 1.0),
    (1.0, 1.0, 0.0, 0.0, 1.0),
    (0.0, 1.0, 1.0, 0.0, 1.0),
    (1.0, 0.0, 0.0, 1.0, 1.0),
    (0.3, 0.7, 0.4, 0.6, 0.4),
    (0.7, 0.3, 0.6, 0.4, 0.4),
    (-0.1, 0.5, 0.5, 0.5, ValueError),
    (0.5, -0.1, 0.5, 0.5, ValueError),
    (0.5, 0.5, -0.1, 0.5, ValueError),
    (0.5, 0.5, 0.5, -0.1, ValueError),
    (1.1, 0.5, 0.5, 0.5, ValueError),
    (0.5, 1.1, 0.5, 0.5, ValueError),
    (0.5, 0.5, 1.1, 0.5, ValueError),
    (0.5, 0.5, 0.5, 1.1, ValueError),
    ("a", 0.5, 0.5, 0.5, TypeError),
    (0.5, "a", 0.5, 0.5, TypeError),
    (0.5, 0.5, "a", 0.5, TypeError),
    (0.5, 0.5, 0.5, "a", TypeError),
    (None, 0.5, 0.5, 0.5, TypeError),
    (0.5, None, 0.5, 0.5, TypeError),
    (0.5, 0.5, None, 0.5, TypeError),
    (0.5, 0.5, 0.5, None, TypeError),
])
def test_F_US(P_gen, P_spec, gamma_gen, gamma_spec, expected):
    try:
        if expected == ValueError or expected == TypeError:
            with pytest.raises(expected):
                F_US(P_gen, P_spec, gamma_gen, gamma_spec)
        else:
            assert F_US(P_gen, P_spec, gamma_gen, gamma_spec) == expected
    except Exception as e:
        if expected == ValueError or expected == TypeError:
            assert type(e) == expected
        else:
            raise e
