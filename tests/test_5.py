import pytest
from definition_6e31eb5cab1443c3a3647838a5124341 import H_base

@pytest.mark.parametrize("k, TTV, H_current, H_target, expected", [
    (0, 10, 0.5, 0.8, 0.5),  # k = 0, should return H_current
    (10, 10, 0.5, 0.8, 0.8), # k = TTV, should return H_target
    (5, 10, 0.5, 0.8, 0.65), # k = TTV/2, should return average
    (2, 10, 0.5, 0.8, 0.56), # k < TTV
    (8, 10, 0.5, 0.8, 0.74), # k > 0 and k < TTV
    (0, 1, 0.2, 0.9, 0.2),  # Small TTV
    (1, 1, 0.2, 0.9, 0.9),  # Small TTV and k == TTV
    (5, 5, 0.1, 0.1, 0.1), # H_current == H_target
    (0, 100, 0.0, 1.0, 0.0), # H_current is 0
    (0, 100, 1.0, 0.0, 1.0), # H_target is 0
    (50, 100, 0.25, 0.75, 0.5), # H_current, H_target are fractions
    (-1, 10, 0.5, 0.8, 0.5), # k is negative, should return H_current (treated as 0)
    (11, 10, 0.5, 0.8, 0.8), # k > TTV, should return H_target (treated as TTV)
    (0, 0, 0.5, 0.8, ValueError), # TTV is 0, division by zero
    (5, 0, 0.5, 0.8, ValueError),  # TTV is 0 and k >0, division by zero
    (0, 10, "0.5", 0.8, TypeError), # H_current is string
    (0, 10, 0.5, "0.8", TypeError), # H_target is string
    (0, 10, 0.5, 0.8, 0.5),  # Valid float inputs
    (0, 10, 1, 0, 1),      # Integer input for H_current and H_target
    (0, 10, 0, 1, 0),      # Integer input for H_current and H_target
    (2.5, 10, 0.5, 0.8, 0.575), # float value for k, should work fine
    (5, 10.0, 0.5, 0.8, 0.65), # float value for TTV, should work fine
    (float('inf'), 10, 0.5, 0.8, 0.8), # k is infinity, should return H_target (treated as TTV)
    (5, float('inf'), 0.5, 0.8, 0.5),  # TTV is infinity, result tends to H_current
    (float('nan'), 10, 0.5, 0.8, ValueError), #k is Nan
    (5, float('nan'), 0.5, 0.8, ValueError), #TTV is Nan
    (5, 10, float('nan'), 0.8, ValueError), #H_current is Nan
    (5, 10, 0.5, float('nan'), ValueError) #H_target is Nan
])
def test_H_base(k, TTV, H_current, H_target, expected):
    try:
        if expected == ValueError:
            with pytest.raises(ValueError):
                H_base(k, TTV, H_current, H_target)
        elif expected == TypeError:
             with pytest.raises(TypeError):
                H_base(k, TTV, H_current, H_target)
        else:
            assert H_base(k, TTV, H_current, H_target) == expected
    except Exception as e:
        if expected == ValueError or expected == TypeError:
            pass
        else:
             assert False, f"Unexpected exception: {e}"
