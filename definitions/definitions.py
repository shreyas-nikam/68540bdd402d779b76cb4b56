
def V_i(F_HC: float, F_CR: float, F_US: float) -> None:
    """Calculates the Idiosyncratic Risk based on Human Capital, Company Risk, and Upskilling factors.

    Arguments:
      F_HC: Human Capital Factor
      F_CR: Company Risk Factor
      F_US: Upskilling Factor
    Output:
      None
    """
    return None


def V_i(F_HC: float, F_CR: float, F_US: float) -> None:
    """Calculates the Idiosyncratic Risk based on Human Capital, Company Risk, and Upskilling factors.

    Arguments:
      F_HC: Human Capital Factor
      F_CR: Company Risk Factor
      F_US: Upskilling Factor
    Output:
      None
    """
    return None


def F_HC(f_role: float, f_level: float, f_field: float, f_school: float, f_exp: float) -> float:
    """Calculates the Human Capital Factor based on role, education level, field, institution tier, and experience.

    Args:
        f_role: Role Multiplier
        f_level: Education Level Factor
        f_field: Education Field Factor
        f_school: Institution Tier Factor
        f_exp: Experience Factor

    Returns:
        Human Capital Factor (float)

    Raises:
        TypeError: if any of the inputs are not of type float or int.
        ValueError: if any of the inputs are negative.
    """
    if not all(isinstance(arg, (float, int)) for arg in [f_role, f_level, f_field, f_school, f_exp]):
        raise TypeError("All inputs must be of type float or int.")

    if any(arg < 0 for arg in [f_role, f_level, f_field, f_school, f_exp]):
        raise ValueError("All factors must be non-negative.")

    return float(f_role * f_level * f_field * f_school * f_exp)


def F_HC(f_role: float, f_level: float, f_field: float, f_school: float, f_exp: float) -> float:
    """Calculates the Human Capital Factor based on role, education level, field, institution tier, and experience.

    Args:
        f_role: Role Multiplier
        f_level: Education Level Factor
        f_field: Education Field Factor
        f_school: Institution Tier Factor
        f_exp: Experience Factor

    Returns:
        Human Capital Factor (float)

    Raises:
        TypeError: if any of the inputs are not of type float or int.
        ValueError: if any of the inputs are negative.
    """
    if not all(isinstance(arg, (float, int)) for arg in [f_role, f_level, f_field, f_school, f_exp]):
        raise TypeError("All inputs must be of type float or int.")

    if any(arg < 0 for arg in [f_role, f_level, f_field, f_school, f_exp]):
        raise ValueError("All factors must be non-negative.")

    return float(f_role * f_level * f_field * f_school * f_exp)


def F_CR(S_senti: float, S_fin: float, S_growth: float, w1: float, w2: float, w3: float) -> float:
    """
    Calculates the Company Risk Factor based on sentiment, financial health, and growth & AI adoption scores.

    Args:
      S_senti: Sentiment Score (0.0 to 1.0).
      S_fin: Financial Health Score (0.0 to 1.0).
      S_growth: Growth & AI Adoption Score (0.0 to 1.0).
      w1: Weight for Sentiment Score (0.0 to 1.0).
      w2: Weight for Financial Health Score (0.0 to 1.0).
      w3: Weight for Growth & AI Adoption Score (0.0 to 1.0).

    Returns:
      Company Risk Factor (float).

    Raises:
      TypeError: If any of the inputs are not of type float or int.
      ValueError: If any of the scores or weights are outside the range of 0.0 to 1.0,
                  or if the sum of the weights is not approximately equal to 1.0.
    """

    if not all(isinstance(arg, (float, int)) for arg in [S_senti, S_fin, S_growth, w1, w2, w3]):
        raise TypeError("All inputs must be numeric (int or float).")

    if not all(0 <= arg <= 1 for arg in [S_senti, S_fin, S_growth, w1, w2, w3]):
        raise ValueError("All scores and weights must be between 0.0 and 1.0.")

    if not (0.999 <= (w1 + w2 + w3) <= 1.001):
        raise ValueError("The sum of the weights must be approximately equal to 1.0.")

    return S_senti * w1 + S_fin * w2 + S_growth * w3


def F_US(P_gen: float, P_spec: float, gamma_gen: float, gamma_spec: float) -> float:
    """Calculates the Upskilling Factor based on training progress in general and specific skills.

    Arguments:
        P_gen: Training progress in general skills (0.0 to 1.0).
        P_spec: Training progress in firm-specific skills (0.0 to 1.0).
        gamma_gen: Weighting parameter for general skills.
        gamma_spec: Weighting parameter for specific skills.

    Output:
        Upskilling Factor (float).
    """
    if not all(isinstance(arg, (float, int)) for arg in [P_gen, P_spec, gamma_gen, gamma_spec]):
        raise TypeError("All inputs must be numeric (float or int).")

    if not all(-1.0 <= arg <= 2.0 for arg in [P_gen, P_spec, gamma_gen, gamma_spec]):
        raise ValueError("All inputs must be between -1.0 and 2.0.")
    
    if not all(0.0 <= arg <= 1.0 for arg in [P_gen, P_spec]):
            raise ValueError("P_gen and P_spec must be between 0.0 and 1.0.")
    
    upskilling_factor = (gamma_gen * (1 - P_gen)) + (gamma_spec * (1 - P_spec))

    return upskilling_factor


def H_i(H_base: float, M_econ: float, IAI: float, w_econ: float, w_inno: float) -> float:
    """Calculates the Systematic Risk based on base occupational hazard, economic climate modifier, and AI innovation index.

    Args:
        H_base: Base Occupational Hazard
        M_econ: Economic Climate Modifier
        IAI: AI Innovation Index
        w_econ: Calibration weight for Economic Climate
        w_inno: Calibration weight for AI Innovation

    Returns:
        Systematic Risk (float)
    """

    if not all(isinstance(arg, (int, float)) for arg in [H_base, M_econ, IAI, w_econ, w_inno]):
        raise TypeError("All inputs must be numeric (int or float)")

    H_i = H_base * (w_econ * M_econ + w_inno * IAI)
    return H_i


def H_i(H_base: float, M_econ: float, IAI: float, w_econ: float, w_inno: float) -> float:
    """Calculates the Systematic Risk based on base occupational hazard, economic climate modifier, and AI innovation index.

    Args:
        H_base: Base Occupational Hazard
        M_econ: Economic Climate Modifier
        IAI: AI Innovation Index
        w_econ: Calibration weight for Economic Climate
        w_inno: Calibration weight for AI Innovation

    Returns:
        Systematic Risk (float)
    """

    if not all(isinstance(arg, (int, float)) for arg in [H_base, M_econ, IAI, w_econ, w_inno]):
        raise TypeError("All inputs must be numeric (int or float)")

    H_i = H_base * (w_econ * M_econ + w_inno * IAI)
    return H_i


def H_base(k: int, TTV: int, H_current: float, H_target: float) -> float:
    """Calculates the Base Occupational Hazard based on the time elapsed since transition, hazard of the original industry, and hazard of the target industry.

    Args:
        k: Months elapsed since transition pathway completion
        TTV: Total Time-to-Value period
        H_current: Base Occupational Hazard of the original industry
        H_target: Base Occupational Hazard of the new target industry

    Returns:
        Base Occupational Hazard (float)

    Raises:
        ValueError: if k or TTV is negative, or if H_current or H_target are outside the range [0, 1].
        ZeroDivisionError: if TTV is zero.
    """

    if k < 0 or TTV < 0:
        raise ValueError("k and TTV must be non-negative")
    if not 0 <= H_current <= 1 or not 0 <= H_target <= 1:
        raise ValueError("H_current and H_target must be between 0 and 1")
    if TTV == 0:
        raise ZeroDivisionError("TTV cannot be zero")

    return H_current + (H_target - H_current) * (k / TTV)


def M_econ(GDP_Growth: float, Sector_Employment: float, Interest_Rates: float) -> float:
    """Calculates the Economic Climate Modifier based on GDP growth, sector employment, and interest rates.

    Args:
        GDP_Growth (float): GDP Growth rate
        Sector_Employment (float): Employment in the sector
        Interest_Rates (float): Interest rates

    Returns:
        float: Economic Climate Modifier

    Raises:
        TypeError: if any of the inputs are not of type float or int.
    """
    if not all(isinstance(arg, (float, int)) for arg in [GDP_Growth, Sector_Employment, Interest_Rates]):
        raise TypeError("GDP_Growth, Sector_Employment, and Interest_Rates must be numeric.")

    # A more robust implementation might involve a weighted sum or a more complex formula.
    # This is a placeholder, as the specific calculation wasn't provided.
    economic_climate_modifier = GDP_Growth + Sector_Employment - Interest_Rates
    return None


def M_econ(GDP_Growth: float, Sector_Employment: float, Interest_Rates: float) -> float:
    """Calculates the Economic Climate Modifier based on GDP growth, sector employment, and interest rates.

    Args:
        GDP_Growth (float): GDP Growth rate
        Sector_Employment (float): Employment in the sector
        Interest_Rates (float): Interest rates

    Returns:
        float: Economic Climate Modifier

    Raises:
        TypeError: if any of the inputs are not of type float or int.
    """
    if not all(isinstance(arg, (float, int)) for arg in [GDP_Growth, Sector_Employment, Interest_Rates]):
        raise TypeError("GDP_Growth, Sector_Employment, and Interest_Rates must be numeric.")

    # A more robust implementation might involve a weighted sum or a more complex formula.
    # This is a placeholder, as the specific calculation wasn't provided.
    economic_climate_modifier = GDP_Growth + Sector_Employment - Interest_Rates
    return None


def IAI(VC_Funding, R_D_Spend, Public_Salience):
    """Calculates the AI Innovation Index based on VC funding, R&D spend, and public salience.

    Args:
        VC_Funding: Venture Capital Funding in AI (numeric).
        R_D_Spend: Research and Development Spending in AI (numeric).
        Public_Salience: Public awareness/discussion of AI (numeric between 0 and 1).

    Returns:
        None.

    Raises:
        TypeError: If inputs are not of the correct type (numeric).
        ValueError: If public salience is not between 0 and 1.
    """
    try:
        VC_Funding = float(VC_Funding)
        R_D_Spend = float(R_D_Spend)
        Public_Salience = float(Public_Salience)
    except (ValueError, TypeError):
        raise TypeError("VC_Funding, R_D_Spend, and Public_Salience must be numeric")

    if not (0 <= Public_Salience <= 1):
        raise ValueError("Public_Salience must be between 0 and 1")
    
    return None
