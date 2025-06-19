import pytest
from definition_1ce71b4e204f47668c0e652ce842dfbf import F_HC

@pytest.mark.parametrize("f_role, f_level, f_field, f_school, f_exp, expected", [
    (1.0, 1.0, 1.0, 1.0, 1.0, 1.0),  # Base case: all factors are 1
    (0.5, 0.5, 0.5, 0.5, 0.5, 0.03125),  # All factors are 0.5
    (2.0, 2.0, 2.0, 2.0, 2.0, 32.0),  # All factors are 2
    (1.0, 1.0, 1.0, 1.0, 0.0, 0.0),  # Zero experience
    (0.0, 1.0, 1.0, 1.0, 1.0, 0.0),  # Zero role multiplier
    (1.0, 0.0, 1.0, 1.0, 1.0, 0.0),  # Zero education level factor
    (1.0, 1.0, 0.0, 1.0, 1.0, 0.0),  # Zero education field factor
    (1.0, 1.0, 1.0, 0.0, 1.0, 0.0),  # Zero institution tier factor
    (1.5, 2.0, 0.75, 1.2, 3.0, 8.1),  # Mixed factors
    (-1.0, 1.0, 1.0, 1.0, 1.0, -1.0), # Negative role multiplier
    (1.0, -1.0, 1.0, 1.0, 1.0, -1.0), # Negative education level factor
    (1.0, 1.0, -1.0, 1.0, 1.0, -1.0), # Negative field factor
    (1.0, 1.0, 1.0, -1.0, 1.0, -1.0), # Negative school factor
    (1.0, 1.0, 1.0, 1.0, -1.0, -1.0), # Negative experience factor
    (0.0, 0.0, 0.0, 0.0, 0.0, 0.0), # All zero
    (10.0, 10.0, 10.0, 10.0, 10.0, 100000.0), # All high positive numbers
    (-10.0, -10.0, -10.0, -10.0, -10.0, -100000.0), # All high negative numbers
    (0.1, 0.2, 0.3, 0.4, 0.5, 0.0012),  # Small positive values
])
def test_F_HC(f_role, f_level, f_field, f_school, f_exp, expected):
    assert F_HC(f_role, f_level, f_field, f_school, f_exp) == expected
