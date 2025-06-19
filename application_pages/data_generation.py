
import pandas as pd
import numpy as np

def generate_human_capital_data(num_samples=100):
    data = {
        'role_multiplier': np.random.uniform(0.5, 1.5, num_samples),
        'education_level_factor': np.random.uniform(0.7, 1.3, num_samples),
        'education_field_factor': np.random.uniform(0.6, 1.4, num_samples),
        'institution_tier_factor': np.random.uniform(0.8, 1.2, num_samples),
        'experience_factor': np.random.uniform(0.9, 1.1, num_samples),
    }
    df = pd.DataFrame(data)
    df['F_HC'] = df['role_multiplier'] * df['education_level_factor'] * df['education_field_factor'] * df['institution_tier_factor'] * df['experience_factor']
    return df

def generate_company_risk_data(num_samples=100):
    data = {
        'sentiment_score': np.random.uniform(0, 1, num_samples), # 0 (bad) to 1 (good)
        'financial_health_score': np.random.uniform(0, 1, num_samples), # 0 (bad) to 1 (good)
        'growth_ai_adoption_score': np.random.uniform(0, 1, num_samples), # 0 (low) to 1 (high)
        'w1': np.random.uniform(0.2, 0.4, num_samples),
        'w2': np.random.uniform(0.3, 0.5, num_samples),
        'w3': np.random.uniform(0.2, 0.4, num_samples),
    }
    df = pd.DataFrame(data)
    # Normalize weights to sum to 1
    df['weight_sum'] = df['w1'] + df['w2'] + df['w3']
    df['w1_norm'] = df['w1'] / df['weight_sum']
    df['w2_norm'] = df['w2'] / df['weight_sum']
    df['w3_norm'] = df['w3'] / df['weight_sum']

    df['F_CR'] = (df['w1_norm'] * (1 - df['sentiment_score']) + # Lower sentiment -> higher risk
                  df['w2_norm'] * (1 - df['financial_health_score']) + # Lower financial health -> higher risk
                  df['w3_norm'] * (1 - df['growth_ai_adoption_score'])) # Lower AI adoption -> higher risk
    return df

def generate_upskilling_data(num_samples=100):
    data = {
        'P_gen': np.random.uniform(0, 1, num_samples), # Training progress 0 (low) to 1 (high)
        'P_spec': np.random.uniform(0, 1, num_samples),
        'gamma_gen': np.random.uniform(0.3, 0.7, num_samples),
        'gamma_spec': np.random.uniform(0.3, 0.7, num_samples),
    }
    df = pd.DataFrame(data)
    # Ensure gamma_gen + gamma_spec <= 1
    df['gamma_sum'] = df['gamma_gen'] + df['gamma_spec']
    df['gamma_gen_norm'] = df['gamma_gen'] / df['gamma_sum']
    df['gamma_spec_norm'] = df['gamma_spec'] / df['gamma_sum']
    
    df['F_US'] = 1 - (df['gamma_gen_norm'] * df['P_gen'] + df['gamma_spec_norm'] * df['P_spec'])
    return df

def generate_systematic_risk_data(num_samples=100):
    data = {
        'H_base': np.random.uniform(0.1, 0.9, num_samples), # Base occupational hazard
        'M_econ': np.random.uniform(0.5, 1.5, num_samples), # Economic climate modifier
        'IAI': np.random.uniform(0.5, 1.5, num_samples), # AI Innovation Index
        'w_econ': np.random.uniform(0.4, 0.6, num_samples),
        'w_inno': np.random.uniform(0.4, 0.6, num_samples),
    }
    df = pd.DataFrame(data)
    df['weight_sum'] = df['w_econ'] + df['w_inno']
    df['w_econ_norm'] = df['w_econ'] / df['weight_sum']
    df['w_inno_norm'] = df['w_inno'] / df['weight_sum']

    df['H_i'] = df['H_base'] * (df['w_econ_norm'] * df['M_econ'] + df['w_inno_norm'] * df['IAI'])
    return df

def generate_all_synthetic_data(num_samples=100):
    df_hc = generate_human_capital_data(num_samples)
    df_cr = generate_company_risk_data(num_samples)
    df_us = generate_upskilling_data(num_samples)
    df_sys = generate_systematic_risk_data(num_samples)

    # Combine relevant factors into a single DataFrame for overall analysis
    # We'll take the F_HC, F_CR, F_US, H_i, and the original inputs for each
    combined_df = pd.DataFrame({
        'F_HC': df_hc['F_HC'],
        'F_CR': df_cr['F_CR'],
        'F_US': df_us['F_US'],
        'H_i': df_sys['H_i'],
        'role_multiplier': df_hc['role_multiplier'],
        'education_level_factor': df_hc['education_level_factor'],
        'education_field_factor': df_hc['education_field_factor'],
        'institution_tier_factor': df_hc['institution_tier_factor'],
        'experience_factor': df_hc['experience_factor'],
        'sentiment_score': df_cr['sentiment_score'],
        'financial_health_score': df_cr['financial_health_score'],
        'growth_ai_adoption_score': df_cr['growth_ai_adoption_score'],
        'P_gen': df_us['P_gen'],
        'P_spec': df_us['P_spec'],
        'H_base': df_sys['H_base'],
        'M_econ': df_sys['M_econ'],
        'IAI': df_sys['IAI']
    })
    return combined_df

if __name__ == '__main__':
    # Example usage:
    synthetic_data = generate_all_synthetic_data(num_samples=5)
    print(synthetic_data)
