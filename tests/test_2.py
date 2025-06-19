import pytest
from definition_3d5594a006254215b1580235fe5a6b2c import F_CR

@pytest.mark.parametrize("S_senti, S_fin, S_growth, w1, w2, w3, expected", [
    (0.8, 0.7, 0.9, 0.3, 0.4, 0.3, 0.78),
    (0.5, 0.5, 0.5, 0.3, 0.4, 0.3, 0.5),
    (0.2, 0.3, 0.1, 0.3, 0.4, 0.3, 0.23),
    (1.0, 1.0, 1.0, 0.3, 0.4, 0.3, 1.0),
    (0.0, 0.0, 0.0, 0.3, 0.4, 0.3, 0.0),
    (0.8, 0.7, 0.9, 0.0, 0.0, 1.0, 0.9),
    (0.8, 0.7, 0.9, 1.0, 0.0, 0.0, 0.8),
    (0.8, 0.7, 0.9, 0.0, 1.0, 0.0, 0.7),
    (0.8, 0.7, 0.9, 0.5, 0.5, 0.0, 0.75),
    (0.8, 0.7, 0.9, 0.5, 0.0, 0.5, 0.85),
    (0.8, 0.7, 0.9, 0.0, 0.5, 0.5, 0.8),
    (0.8, 0.7, 0.9, 0.1, 0.1, 0.8, 0.86),
    (0.8, 0.7, 0.9, 0.1, 0.8, 0.1, 0.73),
    (0.8, 0.7, 0.9, 0.8, 0.1, 0.1, 0.77),
    (0.8, 0.7, 0.9, 0.333, 0.333, 0.334, pytest.approx(0.799, 0.001)),
    (-0.5, 0.7, 0.9, 0.3, 0.4, 0.3, ValueError),
    (0.8, -0.7, 0.9, 0.3, 0.4, 0.3, ValueError),
    (0.8, 0.7, -0.9, 0.3, 0.4, 0.3, ValueError),
    (0.8, 0.7, 0.9, -0.3, 0.4, 0.3, ValueError),
    (0.8, 0.7, 0.9, 0.3, -0.4, 0.3, ValueError),
    (0.8, 0.7, 0.9, 0.3, 0.4, -0.3, ValueError),
    (0.8, 0.7, 0.9, 0.3, 0.4, 0.3, 2),
    (0.8, 0.7, 0.9, 0.3, 0.4, 0.3, 0.78),
    ("a", 0.7, 0.9, 0.3, 0.4, 0.3, TypeError),
    (0.8, "a", 0.9, 0.3, 0.4, 0.3, TypeError),
    (0.8, 0.7, "a", 0.3, 0.4, 0.3, TypeError),
    (0.8, 0.7, 0.9, "a", 0.4, 0.3, TypeError),
    (0.8, 0.7, 0.9, 0.3, "a", 0.3, TypeError),
    (0.8, 0.7, 0.9, 0.3, 0.4, "a", TypeError),
    (None, 0.7, 0.9, 0.3, 0.4, 0.3, TypeError),
    (0.8, None, 0.9, 0.3, 0.4, 0.3, TypeError),
    (0.8, 0.7, None, 0.3, 0.4, 0.3, TypeError),
    (0.8, 0.7, 0.9, None, 0.4, 0.3, TypeError),
    (0.8, 0.7, 0.9, 0.3, None, 0.3, TypeError),
    (0.8, 0.7, 0.9, 0.3, 0.4, None, TypeError),
    (0.8, 0.7, 0.9, 0.3, 0.4, 0.3, "str"),
    (0.8, 0.7, 0.9, 0.3, 0.4, 0.3, None),
    (0.8, 0.7, 0.9, 0.3, 0.4, 0.3, ValueError),
    (0.8, 0.7, 0.9, 0.3, 0.4, 0.3, TypeError),
    (0.8, 0.7, 0.9, 0.5, 0.5, 0.5, ValueError),
    (0.9, 0.9, 0.9, 0.9, 0.9, 0.9, ValueError),
    (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, pytest.approx(0.1, 0.001)),
    (0.9, 0.9, 0.9, 0.0, 0.0, 0.0, 0.0),
    (0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0),
    (0.1, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0)

])
def test_F_CR(S_senti, S_fin, S_growth, w1, w2, w3, expected):
    if isinstance(S_senti, (int, float)) and isinstance(S_fin, (int, float)) and isinstance(S_growth, (int, float)) and isinstance(w1, (int, float)) and isinstance(w2, (int, float)) and isinstance(w3, (int, float)):
        if not (0 <= S_senti <= 1 and 0 <= S_fin <= 1 and 0 <= S_growth <= 1):
            with pytest.raises(ValueError):
                F_CR(S_senti, S_fin, S_growth, w1, w2, w3)
        elif not (0 <= w1 <= 1 and 0 <= w2 <= 1 and 0 <= w3 <= 1):
            with pytest.raises(ValueError):
                 F_CR(S_senti, S_fin, S_growth, w1, w2, w3)

        elif not (pytest.approx(w1 + w2 + w3, 0.001) == 1):
            with pytest.raises(ValueError):
                F_CR(S_senti, S_fin, S_growth, w1, w2, w3)

        elif expected == ValueError or expected == TypeError:
             with pytest.raises(expected):
                  F_CR(S_senti, S_fin, S_growth, w1, w2, w3)

        elif isinstance(expected,(int, float)):
            assert F_CR(S_senti, S_fin, S_growth, w1, w2, w3) == expected
        elif expected == None or expected == "str":
             with pytest.raises(TypeError):
                F_CR(S_senti, S_fin, S_growth, w1, w2, w3)
        else:
             assert F_CR(S_senti, S_fin, S_growth, w1, w2, w3) == expected

    else:
         with pytest.raises(TypeError):
              F_CR(S_senti, S_fin, S_growth, w1, w2, w3)

