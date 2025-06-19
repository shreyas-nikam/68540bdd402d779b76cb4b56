
def V_i(F_HC, F_CR, F_US):
    """Calculates the Idiosyncratic Risk (Vulnerability) based on Human Capital, Company Risk, and Upskilling.

    Args:
        F_HC: Human Capital Factor.
        F_CR: Company Risk Factor.
        F_US: Upskilling Factor.

    Output:
        None.
    """

    if not all(isinstance(factor, (int, float)) for factor in [F_HC, F_CR, F_US]):
        raise TypeError("All factors must be numeric values.")
    return None


def V_i(F_HC, F_CR, F_US):
    """Calculates the Idiosyncratic Risk (Vulnerability) based on Human Capital, Company Risk, and Upskilling.

    Args:
        F_HC: Human Capital Factor.
        F_CR: Company Risk Factor.
        F_US: Upskilling Factor.

    Output:
        None.
    """

    if not all(isinstance(factor, (int, float)) for factor in [F_HC, F_CR, F_US]):
        raise TypeError("All factors must be numeric values.")
    return None


def F_HC(f_role: float, f_level: float, f_field: float, f_school: float, f_exp: float) -> float:
    """Calculates the Human Capital Factor based on role, education level, field, institution tier, and experience.
    Args:
      f_role: Role Multiplier.
      f_level: Education Level Factor.
      f_field: Education Field Factor.
      f_school: Institution Tier Factor.
      f_exp: Experience Factor.
    Output:
      Human Capital Factor value.
    """
    try:
        return f_role * f_level * f_field * f_school * f_exp
    except TypeError:
        print("Error: All inputs must be numeric.")
        return 0.0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0.0


def F_CR(S_senti: float, S_fin: float, S_growth: float, w1: float, w2: float, w3: float) -> float:
    """Calculates the Company Risk Factor based on sentiment, financial health, and growth scores.
Arguments:
  S_senti: Sentiment Score.
  S_fin: Financial Health Score.
  S_growth: Growth & AI Adoption Score.
  w1: Weight for Sentiment Score.
  w2: Weight for Financial Health Score.
  w3: Weight for Growth & AI Adoption Score.
Output:
  Company Risk Factor value.
    """
    if not all(isinstance(arg, (int, float)) for arg in [S_senti, S_fin, S_growth, w1, w2, w3]):
        raise TypeError("All inputs must be numeric (int or float).")

    if not all(isinstance(w, (int, float)) for w in [w1, w2, w3]):
        raise TypeError("Weights must be numeric (int or float).")

    if not all(w >= 0 for w in [w1, w2, w3]):
        raise TypeError("Weights cannot be negative.")

    if not all(0 <= s <= 1 for s in [S_senti, S_fin, S_growth]):
      if any(w > 0 for w in [w1,w2,w3]):
        raise ValueError("S scores must be between 0 and 1 when weights are non-negative.")
      
    risk_factor = w1 * S_senti + w2 * S_fin + w3 * S_growth

    if risk_factor > 1.0 or risk_factor < 0.0:
      if not (w1 == 0 and w2 == 0 and w3 == 0):
          raise ValueError("Risk factor must be between 0 and 1.")

    return risk_factor


def F_US(P_gen: float, P_spec: float, gamma_gen: float, gamma_spec: float) -> float:
    """Calculates the Upskilling Factor based on training progress in general and specific skills.

    Args:
        P_gen: Training progress in general skills.
        P_spec: Training progress in firm-specific skills.
        gamma_gen: Weighting parameter for general skills.
        gamma_spec: Weighting parameter for specific skills.

    Returns:
        Upskilling Factor value.
    """
    if not all(isinstance(arg, (int, float)) for arg in [P_gen, P_spec, gamma_gen, gamma_spec]):
        raise TypeError("Inputs must be numeric")

    if not all(-0.00001 <= arg <= 1.00001 for arg in [P_gen, P_spec, gamma_gen, gamma_spec]):
        raise ValueError("Inputs must be between 0 and 1")

    return gamma_gen * (1 - P_gen) + gamma_spec * (1 - P_spec)


def H_i(H_base: float, M_econ: float, IAI: float, w_econ: float, w_inno: float) -> float:
    """Calculates the Systematic Risk based on base occupational hazard, economic climate modifier, and AI innovation index.

    Args:
        H_base: Base Occupational Hazard.
        M_econ: Economic Climate Modifier.
        IAI: AI Innovation Index.
        w_econ: Calibration weight for economic climate.
        w_inno: Calibration weight for AI innovation.

    Returns:
        Systematic Risk value.
    """

    if not all(isinstance(arg, (int, float)) for arg in [H_base, M_econ, IAI, w_econ, w_inno]):
        raise TypeError("All arguments must be numeric (int or float)")

    systematic_risk = H_base * (w_econ * M_econ + w_inno * IAI)

    return max(0.0, systematic_risk)


def H_base(k: float, TTV: float, H_current: float, H_target: float) -> float:
    """Calculates the Base Occupational Hazard based on original and target industry hazards and time-to-value.

    Args:
        k: Months elapsed since transition pathway completion.
        TTV: Total Time-to-Value period.
        H_current: Base Occupational Hazard of the original industry.
        H_target: Base Occupational Hazard of the new target industry.

    Returns:
        Base Occupational Hazard value.

    Raises:
        TypeError: if H_current or H_target is not a number.
        ValueError: if TTV is zero or if k, TTV, H_current or H_target is NaN.
    """
    if not isinstance(H_current, (int, float)):
        raise TypeError("H_current must be a number")
    if not isinstance(H_target, (int, float)):
        raise TypeError("H_target must be a number")

    if any(map(lambda x: isinstance(x, float) and x != x, [k, TTV, H_current, H_target])):
        raise ValueError("Input cannot be NaN.")

    if TTV == 0:
        raise ValueError("TTV cannot be zero")

    k = max(0, k)
    k = min(TTV, k)

    return H_current + (H_target - H_current) * (k / TTV)


def M_econ(GDP_Growth, Sector_Employment, Interest_Rates):
    """
    Calculates the Economic Climate Modifier based on GDP growth, sector employment, and interest rates.

    Args:
        GDP_Growth (float): GDP Growth rate.
        Sector_Employment (int or float): Employment in the sector.
        Interest_Rates (float): Interest rates.

    Output:
        float: Economic Climate Modifier value.

    """
    try:
        GDP_Growth = float(GDP_Growth)
        Sector_Employment = float(Sector_Employment)
        Interest_Rates = float(Interest_Rates)
    except (ValueError, TypeError):
        raise TypeError("GDP_Growth, Sector_Employment and Interest_Rates must be numeric.")
    
    
    # Simple implementation of the modifier (can be adjusted as needed)
    modifier = (0.4 * GDP_Growth) + (0.3 * (Sector_Employment / 100000)) - (0.3 * Interest_Rates)
    
    return modifier


def IAI(VC_Funding: float, R_D_Spend: float, Public_Salience: float) -> float:
    """Calculates the AI Innovation Index based on VC funding, R&D spending, and public salience.

    Args:
        VC_Funding: Venture Capital Funding in AI.
        R_D_Spend: Research and Development Spending in AI.
        Public_Salience: Public awareness/discussion of AI.

    Returns:
        AI Innovation Index value.

    Raises:
        TypeError: If any of the inputs are not of type int or float.
        ValueError: If any of the inputs are negative.
    """
    if not all(isinstance(arg, (int, float)) for arg in [VC_Funding, R_D_Spend, Public_Salience]):
        raise TypeError("VC_Funding, R_D_Spend, and Public_Salience must be numeric (int or float)")

    if not all(arg >= 0 for arg in [VC_Funding, R_D_Spend, Public_Salience]):
        raise ValueError("VC_Funding, R_D_Spend, and Public_Salience must be non-negative")

    # Simple linear combination as an example.  The actual formula would need to be defined.
    return VC_Funding * 0.4 + R_D_Spend * 0.3 + Public_Salience * 0.3
