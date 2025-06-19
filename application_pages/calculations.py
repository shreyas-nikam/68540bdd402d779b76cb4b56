
import numpy as np

def calculate_human_capital_factor(f_role, f_level, f_field, f_school, f_exp):
    """
    Calculates the Human Capital Factor (F_HC).
    F_HC = f_role * f_level * f_field * f_school * f_exp
    """
    return f_role * f_level * f_field * f_school * f_exp

def calculate_company_risk_factor(S_senti, S_fin, S_growth, w1, w2, w3):
    """
    Calculates the Company Risk Factor (F_CR).
    F_CR = w1 * S_senti + w2 * S_fin + w3 * S_growth
    Weights (w1, w2, w3) should sum to 1 or be normalized.
    Note: In the specification, lower sentiment/financial health/growth means higher risk.
    So, we interpret S_senti, S_fin, S_growth as positive scores (0-1),
    and a higher score means less risk (lower F_CR).
    Thus, (1 - Score) contributes to risk.
    """
    weight_sum = w1 + w2 + w3
    w1_norm = w1 / weight_sum
    w2_norm = w2 / weight_sum
    w3_norm = w3 / weight_sum
    
    # Interpretation: Lower score means higher risk contribution
    return (w1_norm * (1 - S_senti) +
            w2_norm * (1 - S_fin) +
            w3_norm * (1 - S_growth))

def calculate_upskilling_factor(P_gen, P_spec, gamma_gen, gamma_spec):
    """
    Calculates the Upskilling Factor (F_US).
    F_US = 1 - (gamma_gen * P_gen + gamma_spec * P_spec)
    Weights (gamma_gen, gamma_spec) should sum to 1 or be normalized.
    """
    gamma_sum = gamma_gen + gamma_spec
    gamma_gen_norm = gamma_gen / gamma_sum
    gamma_spec_norm = gamma_spec / gamma_sum
    
    return 1 - (gamma_gen_norm * P_gen + gamma_spec_norm * P_spec)

def calculate_idiosyncratic_risk(F_HC, F_CR, F_US):
    """
    Calculates the Idiosyncratic Risk (V_i(t)).
    V_i(t) = f(F_HC, F_CR, F_US)
    A simple aggregation, e.g., weighted average or product.
    Lower F_HC, lower F_US (more upskilling), and lower F_CR (less company risk) should result in lower V_i(t).
    Let's use a multiplicative inverse for F_HC and F_US, and direct for F_CR.
    Lower F_HC means lower resilience. F_CR higher means higher company risk. F_US higher means lower resilience (less upskilling).
    So, a higher V_i(t) means more risk.
    Let's use an average.
    """
    # Assuming F_HC, F_CR, F_US are normalized or scaled to a comparable range (e.g., 0 to 1)
    # The higher F_CR, the higher the risk. The lower F_HC and F_US, the higher the risk.
    # To make it consistent for aggregation, let's invert F_HC and F_US.
    # A low F_HC (e.g., 0.5) means high risk from human capital.
    # A low F_US (e.g., 0.5) means high risk from upskilling.
    # A high F_CR (e.g., 0.8) means high risk from company.
    # Let's map everything to a "risk contribution" where higher is worse.
    # F_HC: lower value means higher risk, so use (1 - F_HC_normalized)
    # F_CR: higher value means higher risk, so use F_CR_normalized
    # F_US: lower value means higher risk, so use (1 - F_US_normalized)
    
    # Simple example: average of risk contributions. Needs scaling for real world use.
    # For synthetic data, let's ensure F_HC, F_CR, F_US are roughly in a 0-1 range after calculation in data_generation.
    # Higher F_HC from data_generation means *less* risk.
    # Higher F_CR from data_generation means *more* risk.
    # Higher F_US from data_generation means *less* risk.
    
    # Let's define V_i(t) such that higher is worse.
    # We want a high F_HC to *reduce* V_i(t).
    # We want a high F_CR to *increase* V_i(t).
    # We want a high F_US to *reduce* V_i(t).

    # A simple way to combine:
    # Scale F_HC and F_US (which are resilience factors) to represent risk (1-factor).
    # F_HC typically > 0, F_US typically > 0.
    
    # Example mapping: 
    # F_HC range ~[0.3, 2.0] from data_gen. Map to risk [0,1]: risk_hc = max(0, 1 - (F_HC / 1.5))
    # F_CR range ~[0, 1] from data_gen. Map to risk [0,1]: risk_cr = F_CR
    # F_US range ~[0, 1] from data_gen. Map to risk [0,1]: risk_us = max(0, 1 - F_US)

    # For now, let's assume all inputs are "risk scores" where higher is worse.
    # We'll normalize them based on their expected ranges from data_generation.
    # F_HC in data_generation is resilience, so risk is (max_val - F_HC) / max_val
    # F_CR in data_generation is already risk, so F_CR / max_val
    # F_US in data_generation is resilience, so risk is (max_val - F_US) / max_val

    # Given data_generation outputs F_HC (high=good), F_CR (high=bad), F_US (high=good)
    # Let's normalize these to a 0-1 range where 1 is maximum risk.
    
    # These max values should be calibrated, but for synthetic data, we can approximate:
    max_F_HC_expected = 1.5 * 1.3 * 1.4 * 1.2 * 1.1 # from data_generation upper bounds = 3.54
    max_F_CR_expected = 1.0 # 0-1 range already from data_generation
    max_F_US_expected = 1.0 # 0-1 range already from data_generation (actually 0 to 1-gamma_sum*0) -> 1

    # Invert F_HC and F_US to represent 'risk contribution'
    risk_contrib_HC = 1 - (F_HC / max_F_HC_expected) if max_F_HC_expected > 0 else 1
    risk_contrib_CR = F_CR / max_F_CR_expected if max_F_CR_expected > 0 else 1
    risk_contrib_US = 1 - (F_US / max_F_US_expected) if max_F_US_expected > 0 else 1

    # Simple average for now. The problem states f(F_HC, F_CR, F_US) without explicit form.
    # This combination makes sense: if F_HC is high (good), risk_contrib_HC is low. If F_CR is high (bad), risk_contrib_CR is high.
    V_i = np.mean([risk_contrib_HC, risk_contrib_CR, risk_contrib_US])
    return V_i

def calculate_base_occupational_hazard(k, TTV, H_current, H_target):
    """
    Calculates the Base Occupational Hazard (H_base(k)).
    H_base(k) = (1 - k/TTV) * H_current + (k/TTV) * H_target
    """
    if TTV <= 0:
        return H_target # Avoid division by zero, or handle appropriately
    
    # Cap k at TTV to prevent negative weights or weights > 1
    k = min(k, TTV)
    
    return (1 - k/TTV) * H_current + (k/TTV) * H_target

def calculate_systematic_risk(H_base, M_econ, IAI, w_econ, w_inno):
    """
    Calculates the Systematic Risk (H_i).
    H_i = H_base * (w_econ * M_econ + w_inno * IAI)
    Weights (w_econ, w_inno) should sum to 1 or be normalized.
    """
    weight_sum = w_econ + w_inno
    w_econ_norm = w_econ / weight_sum
    w_inno_norm = w_inno / weight_sum
    
    return H_base * (w_econ_norm * M_econ + w_inno_norm * IAI)

def calculate_ai_q_score(idiosyncratic_risk, systematic_risk):
    """
    Combines Idiosyncratic Risk and Systematic Risk to calculate the final AI-Q Score.
    This is a conceptual combination; a simple sum or weighted sum is an option.
    Assuming both risks are scaled to a similar range (e.g., 0-1) where higher is worse.
    """
    # A simple additive model for AI-Q Score, could be weighted sum.
    # For demonstration, let's average them.
    # If both are normalized 0-1, then the score will also be 0-1.
    return (idiosyncratic_risk + systematic_risk) / 2.0

# Example usage for testing purposes
if __name__ == '__main__':
    # Human Capital
    f_role_val, f_level_val, f_field_val, f_school_val, f_exp_val = 1.0, 1.0, 1.0, 1.0, 1.0
    F_HC_val = calculate_human_capital_factor(f_role_val, f_level_val, f_field_val, f_school_val, f_exp_val)
    print(f"Human Capital Factor (F_HC): {F_HC_val:.2f}")

    # Company Risk (sentiment, financial health, growth/AI adoption, weights)
    S_senti_val, S_fin_val, S_growth_val = 0.8, 0.7, 0.9 # Higher is better for company
    w1_cr, w2_cr, w3_cr = 0.3, 0.4, 0.3
    F_CR_val = calculate_company_risk_factor(S_senti_val, S_fin_val, S_growth_val, w1_cr, w2_cr, w3_cr)
    print(f"Company Risk Factor (F_CR): {F_CR_val:.2f}") # Higher F_CR is worse

    # Upskilling (progress gen, progress spec, gamma gen, gamma spec)
    P_gen_val, P_spec_val = 0.6, 0.7
    gamma_gen_val, gamma_spec_val = 0.5, 0.5
    F_US_val = calculate_upskilling_factor(P_gen_val, P_spec_val, gamma_gen_val, gamma_spec_val)
    print(f"Upskilling Factor (F_US): {F_US_val:.2f}") # Higher F_US is worse (less upskilling leads to higher 1-(...))

    # Idiosyncratic Risk
    # Need to ensure F_HC, F_CR, F_US are in comparable ranges for the generic aggregation function.
    # Let's adjust for testing:
    # F_HC_val (higher=better) -> risk_contrib_HC = 1 - F_HC_val/max_F_HC_expected
    # F_CR_val (higher=worse) -> risk_contrib_CR = F_CR_val/max_F_CR_expected
    # F_US_val (higher=better) -> risk_contrib_US = 1 - F_US_val/max_F_US_expected
    
    # For testing, let's provide F_HC_val (resilience) and F_CR_val, F_US_val (upskilling) directly
    # and let the calculate_idiosyncratic_risk handle the inversion/normalization for its internal averaging.
    V_i_val = calculate_idiosyncratic_risk(F_HC=F_HC_val, F_CR=F_CR_val, F_US=F_US_val)
    print(f"Idiosyncratic Risk (V_i(t)): {V_i_val:.2f}")

    # Systematic Risk - Base Occupational Hazard
    k_val, TTV_val, H_current_val, H_target_val = 6, 12, 0.7, 0.3 # 6 months into a 12 month transition
    H_base_val = calculate_base_occupational_hazard(k_val, TTV_val, H_current_val, H_target_val)
    print(f"Base Occupational Hazard (H_base(k)): {H_base_val:.2f}")

    # Systematic Risk (H_base, econ modifier, AI index, weights)
    M_econ_val, IAI_val = 1.1, 1.2 # Modifiers for economic and AI innovation
    w_econ_sys, w_inno_sys = 0.5, 0.5
    H_i_val = calculate_systematic_risk(H_base_val, M_econ_val, IAI_val, w_econ_sys, w_inno_sys)
    print(f"Systematic Risk (H_i): {H_i_val:.2f}")

    # AI-Q Score
    ai_q_score_val = calculate_ai_q_score(V_i_val, H_i_val)
    print(f"AI-Q Score: {ai_q_score_val:.2f}")
