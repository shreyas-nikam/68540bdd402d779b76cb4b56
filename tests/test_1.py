import pytest
from definition_620e59c283ce47f2be86fb50e21ada4e import F_HC

@pytest.mark.parametrize("f_role, f_level, f_field, f_school, f_exp, expected", [
    (1.0, 1.0, 1.0, 1.0, 1.0, 1.0),  # Base case: all factors are 1
    (0.8, 1.2, 0.9, 1.1, 1.0, 0.9504),  # Varying factors
    (0.5, 0.5, 0.5, 0.5, 0.5, 0.03125),  # All factors are low
    (2.0, 2.0, 2.0, 2.0, 2.0, 32.0),  # All factors are high
    (1.0, 1.0, 1.0, 1.0, 0.0, 0.0),  # Zero experience
    (0.0, 1.0, 1.0, 1.0, 1.0, 0.0),  # Zero role multiplier
    (1.0, 0.0, 1.0, 1.0, 1.0, 0.0),  # Zero education level
    (1.0, 1.0, 0.0, 1.0, 1.0, 0.0),  # Zero education field
    (1.0, 1.0, 1.0, 0.0, 1.0, 0.0),  # Zero institution tier
    (1.5, 0.7, 1.2, 0.9, 1.1, 1.2474),  # Mixed factors
    (1, 1, 1, 1, 1, 1.0),  # Integer inputs, should still work
    (1.0, 1.0, 1.0, 1.0, -1.0, ValueError),  # Negative experience - raises error
    (1.0, 1.0, 1.0, -1.0, 1.0, ValueError),  # Negative institution tier
    (1.0, 1.0, -1.0, 1.0, 1.0, ValueError),  # Negative Education field
    (1.0, -1.0, 1.0, 1.0, 1.0, ValueError),  # Negative Education level
    (-1.0, 1.0, 1.0, 1.0, 1.0, ValueError),  # Negative role
    (1.0, 1.0, 1.0, 1.0, "a", TypeError), #Experience as String
    ("a", 1.0, 1.0, 1.0, 1.0, TypeError), #Role as String
    (1.0, "a", 1.0, 1.0, 1.0, TypeError), #Level as String
    (1.0, 1.0, "a", 1.0, 1.0, TypeError), #Field as String
    (1.0, 1.0, 1.0, "a", 1.0, TypeError), #School as String
    (None, 1.0, 1.0, 1.0, 1.0, TypeError), #Role as None
    (1.0, None, 1.0, 1.0, 1.0, TypeError), #Level as None
    (1.0, 1.0, None, 1.0, 1.0, TypeError), #Field as None
    (1.0, 1.0, 1.0, None, 1.0, TypeError), #School as None
    (1.0, 1.0, 1.0, 1.0, None, TypeError), #Experience as None
])
def test_F_HC(f_role, f_level, f_field, f_school, f_exp, expected):
    try:
        if expected == ValueError or expected == TypeError:
            with pytest.raises(expected):
                F_HC(f_role, f_level, f_field, f_school, f_exp)

        else:
            assert F_HC(f_role, f_level, f_field, f_school, f_exp) == expected
    except Exception as e:
         if expected not in [ValueError, TypeError]:
            raise e
