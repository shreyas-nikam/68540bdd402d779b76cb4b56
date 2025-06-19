import pytest
from definition_16f5d16046964c2b98ac85d674c3562d import H_base

@pytest.mark.parametrize("k, TTV, H_current, H_target, expected", [
    (0, 12, 0.5, 0.2, 0.5),
    (12, 12, 0.5, 0.2, 0.2),
    (6, 12, 0.5, 0.2, 0.35),
    (3, 6, 0.8, 0.3, 0.55),
    (0, 6, 0.8, 0.3, 0.8),
    (6, 6, 0.8, 0.3, 0.3),
    (1, 10, 0.9, 0.1, 0.82),
    (5, 10, 0.9, 0.1, 0.5),
    (10, 10, 0.9, 0.1, 0.1),
    (0, 1, 1.0, 0.0, 1.0),
    (1, 1, 1.0, 0.0, 0.0),
    (0, 100, 0.0, 1.0, 0.0),
    (100, 100, 0.0, 1.0, 1.0),
    (50, 100, 0.0, 1.0, 0.5),
    (25, 50, 0.2, 0.8, 0.5),
    (0, 50, 0.2, 0.8, 0.2),
    (50, 50, 0.2, 0.8, 0.8),
    (10, 20, 0.7, 0.3, 0.5),
    (20, 20, 0.7, 0.3, 0.3),
    (0, 20, 0.7, 0.3, 0.7),
    (5, 10, 0.6, 0.4, 0.5),
    (-1, 10, 0.9, 0.1, ValueError),
    (1, -10, 0.9, 0.1, ValueError),
    (1, 10, -0.9, 0.1, ValueError),
    (1, 10, 0.9, -0.1, ValueError),
    (1, 10, 0.9, 1.1, ValueError),
    (1, 10, 1.1, 0.1, ValueError),
    (1, 0, 0.9, 0.1, ZeroDivisionError),
])
def test_H_base(k, TTV, H_current, H_target, expected):
    try:
        if expected == ValueError or expected == ZeroDivisionError:
            with pytest.raises(expected):
                 H_base(k, TTV, H_current, H_target)
        else:
            assert H_base(k, TTV, H_current, H_target) == expected
    except Exception as e:
        assert type(e) == expected
