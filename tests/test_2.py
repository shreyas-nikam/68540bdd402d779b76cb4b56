import pytest
from definition_89117188f8354e2d9116f92a31c94eaf import F_CR

@pytest.mark.parametrize("S_senti, S_fin, S_growth, w1, w2, w3, expected", [
    (0.8, 0.9, 0.7, 0.3, 0.4, 0.3, 0.82),
    (0.2, 0.3, 0.4, 0.3, 0.4, 0.3, 0.3),
    (0.5, 0.5, 0.5, 0.33, 0.33, 0.34, 0.5),
    (1.0, 1.0, 1.0, 0.1, 0.1, 0.8, 1.0),
    (0.0, 0.0, 0.0, 0.3, 0.4, 0.3, 0.0),
    (0.8, 0.9, 0.7, 0.0, 0.0, 1.0, 0.7),
    (0.8, 0.9, 0.7, 1.0, 0.0, 0.0, 0.8),
    (0.8, 0.9, 0.7, 0.0, 1.0, 0.0, 0.9),
    (0.8, 0.9, 0.7, 0.5, 0.5, 0.0, 0.85),
    (0.8, 0.9, 0.7, 0.5, 0.0, 0.5, 0.75),
    (0.8, 0.9, 0.7, 0.0, 0.5, 0.5, 0.8),
    (-0.5, 0.6, 0.7, 0.3, 0.4, 0.3, pytest.approx(0.27, abs=1e-6)),
    (0.5, -0.6, 0.7, 0.3, 0.4, 0.3, pytest.approx(0.17, abs=1e-6)),
    (0.5, 0.6, -0.7, 0.3, 0.4, 0.3, pytest.approx(0.07, abs=1e-6)),
    (0.5, 0.6, 0.7, -0.3, 0.4, 0.3, TypeError),
    (0.5, 0.6, 0.7, 0.3, -0.4, 0.3, TypeError),
    (0.5, 0.6, 0.7, 0.3, 0.4, -0.3, TypeError),
    (0.5, 0.6, 0.7, 0.3, 0.4, 0.3, 0.1),
    (0.8, 0.9, 0.7, 0.3, 0.4, 0.3, 1.0),
    (0.8, 0.9, 0.7, 0.3, 0.4, 0.3, -1.0),
    ("a", 0.9, 0.7, 0.3, 0.4, 0.3, TypeError),
    (0.8, "b", 0.7, 0.3, 0.4, 0.3, TypeError),
    (0.8, 0.9, "c", 0.3, 0.4, 0.3, TypeError),
    (0.8, 0.9, 0.7, "d", 0.4, 0.3, TypeError),
    (0.8, 0.9, 0.7, 0.3, "e", 0.3, TypeError),
    (0.8, 0.9, 0.7, 0.3, 0.4, "f", TypeError),
    (None, 0.9, 0.7, 0.3, 0.4, 0.3, TypeError),
    (0.8, None, 0.7, 0.3, 0.4, 0.3, TypeError),
    (0.8, 0.9, None, 0.3, 0.4, 0.3, TypeError),
    (0.8, 0.9, 0.7, None, 0.4, 0.3, TypeError),
    (0.8, 0.9, 0.7, 0.3, None, 0.3, TypeError),
    (0.8, 0.9, 0.7, 0.3, 0.4, None, TypeError),
    (0.8, 0.9, 0.7, 0.3, 0.4, 0.3, 0.7),
    (0.8, 0.9, 0.7, 0.3, 0.4, 0.3, 0.9)

])
def test_F_CR(S_senti, S_fin, S_growth, w1, w2, w3, expected):
    try:
        if expected == 0.1:
           with pytest.raises(ValueError):
             F_CR(S_senti, S_fin, S_growth, w1, w2, w3)
        elif expected == 0.7:
             with pytest.raises(ValueError):
               F_CR(S_senti, S_fin, S_growth, w1, w2, w3)
        elif expected == 0.9:
             with pytest.raises(ValueError):
               F_CR(S_senti, S_fin, S_growth, w1, w2, w3)
        elif expected == 1.0:
            with pytest.raises(ValueError):
                F_CR(S_senti, S_fin, S_growth, w1, w2, w3)
        elif expected == -1.0:
             with pytest.raises(ValueError):
               F_CR(S_senti, S_fin, S_growth, w1, w2, w3)
        else:
            result = F_CR(S_senti, S_fin, S_growth, w1, w2, w3)
            assert result == pytest.approx(expected, abs=1e-6)
    except Exception as e:
        assert isinstance(e, expected)
