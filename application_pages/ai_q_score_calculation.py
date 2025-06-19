
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def run_ai_q_score_calculation_page():
    st.header("AI-Q Score Calculation")
    st.write("Adjust the parameters below to see how your individual AI-Q Score changes in real-time. This section focuses on the Idiosyncratic Risk factors: Human Capital, Company Risk, and Upskilling.")

    # --- Dummy Data Generation and Calculation Functions ---
    # These are simplified for demonstration purposes and would be more complex in a real application.

    def calculate_human_capital(role_multiplier, education_level_factor, education_field_factor, institution_tier_factor, experience_factor):
        # f_role * f_level * f_field * f_school * f_exp
        return role_multiplier * education_level_factor * education_field_factor * institution_tier_factor * experience_factor

    def calculate_company_risk(sentiment_score, financial_health_score, growth_ai_adoption_score):
        # w_1 * S_senti + w_2 * S_fin + w_3 * S_growth
        # Using arbitrary weights for demonstration
        w1, w2, w3 = 0.3, 0.4, 0.3
        return (w1 * sentiment_score + w2 * financial_health_score + w3 * growth_ai_adoption_score) / 100 # Normalize to 0-1 range

    def calculate_upskilling_factor(gen_progress, spec_progress):
        # 1 - (gamma_gen * P_gen(t) + gamma_spec * P_spec(t))
        # Using arbitrary weights for demonstration
        gamma_gen, gamma_spec = 0.6, 0.4
        return 1 - (gamma_gen * gen_progress + gamma_spec * spec_progress) / 100 # Normalize to 0-1 range

    def calculate_idiosyncratic_risk(human_capital, company_risk, upskilling):
        # V_i(t) = f(F_HC, F_CR, F_US)
        # Simplified composite function: average of normalized factors, inverted to represent risk
        # Lower factor values (better human capital, less company risk, more upskilling) should lead to lower idiosyncratic risk
        normalized_hc = 1 / (1 + human_capital / 100) # Assuming human_capital is a multiplier, higher is better, so risk decreases
        normalized_cr = company_risk # company_risk is already normalized as risk
        normalized_us = 1 - upskilling # upskilling factor is 1-(...), so higher upskilling means lower factor, thus lower risk

        # Let's define a simple linear combination where higher scores mean higher risk
        # F_HC will be inverted because higher HC means lower risk.
        # F_CR and F_US (1-F_US) will directly contribute to risk.
        idiosyncratic_risk = ( (1 - normalized_hc) + normalized_cr + normalized_us) / 3
        return idiosyncratic_risk * 100 # Scale to 0-100

    def calculate_systematic_risk(base_hazard, economic_modifier, ai_innovation_index):
        # H_i = H_base(t) * (w_econ * M_econ + w_inno * IAI)
        # Using arbitrary weights for demonstration
        w_econ, w_inno = 0.5, 0.5
        # Systematic risk is a product. Higher values for modifiers mean higher systematic risk.
        return base_hazard * (w_econ * economic_modifier / 100 + w_inno * ai_innovation_index / 100)

    def calculate_ai_q_score(idiosyncratic_risk, systematic_risk):
        # AI-Q Score is a combination. For simplicity, let's use a weighted sum.
        # Arbitrary weights
        w_idiosyncratic, w_systematic = 0.6, 0.4
        return (w_idiosyncratic * idiosyncratic_risk + w_systematic * systematic_risk)

    # --- Input Widgets ---
    st.sidebar.subheader("Adjust Your Profile")

    with st.sidebar.expander("Human Capital"):
        role_multiplier = st.slider("Role Multiplier (f_role)", 0.5, 2.0, 1.0, 0.1, help="Impact of your current job role. Higher is generally better/more stable.")
        education_level_factor = st.slider("Education Level (f_level)", 0.5, 2.0, 1.0, 0.1, help="Impact of your highest education level.")
        education_field_factor = st.slider("Education Field (f_field)", 0.5, 2.0, 1.0, 0.1, help="Impact of your education field (e.g., STEM vs. Humanities).")
        institution_tier_factor = st.slider("Institution Tier (f_school)", 0.5, 2.0, 1.0, 0.1, help="Impact of the prestige of your educational institution.")
        experience_factor = st.slider("Years of Experience (f_exp)", 0.0, 30.0, 10.0, 1.0, help="Impact of your years of professional experience.")
        
        # Normalize experience factor - higher experience should lead to a lower risk contribution
        # Let's assume a decay: exp_factor_calc = max(0.1, 2.0 - (experience_factor / 15))
        # For calculation, we need a value where higher is better for HC.
        # Let's map years of experience to a factor, e.g., 0-30 -> 0.5-2.0
        exp_factor_for_calc = 0.5 + (experience_factor / 30) * 1.5


    with st.sidebar.expander("Company Risk"):
        sentiment_score = st.slider("Sentiment Score (S_senti)", 0, 100, 75, help="Market perception and employee morale (0-100). Higher is better.")
        financial_health_score = st.slider("Financial Health Score (S_fin)", 0, 100, 80, help="Company's financial stability (0-100). Higher is better.")
        growth_ai_adoption_score = st.slider("Growth & AI Adoption (S_growth)", 0, 100, 70, help="Company's innovation and AI investment (0-100). Higher is better.")

    with st.sidebar.expander("Upskilling"):
        general_skills_progress = st.slider("General Skills Training Progress (P_gen)", 0, 100, 60, help="Progress in transferable skills (0-100%).")
        firm_specific_skills_progress = st.slider("Firm-Specific Skills Training Progress (P_spec)", 0, 100, 40, help="Progress in internal/firm-specific skills (0-100%).")

    # Fixed Systematic Risk inputs for this page, as it's primarily about Idiosyncratic Risk
    # These will be made interactive on the "Systematic Risk Dynamics" page
    st.sidebar.subheader("Global Factors (for current page)")
    base_occupational_hazard = st.sidebar.slider("Base Occupational Hazard", 0.0, 100.0, 50.0, 1.0, help="Inherent risk of your occupation.")
    economic_climate_index = st.sidebar.slider("Economic Climate Index", 0, 100, 50, help="Overall economic environment's effect on AI investment (0-100). Higher implies more pressure.")
    ai_innovation_index = st.sidebar.slider("AI Innovation Index", 0, 100, 50, help="Velocity of AI development and adoption (0-100). Higher implies faster change.")


    # --- Calculations ---
    # Human Capital Calculation: Higher factor means better human capital, thus lower risk contribution
    human_capital_calc_factor = calculate_human_capital(role_multiplier, education_level_factor, education_field_factor, institution_tier_factor, exp_factor_for_calc)

    # Company Risk Calculation: Higher score means better company health, thus lower risk contribution
    company_risk_calc_score = calculate_company_risk(sentiment_score, financial_health_score, growth_ai_adoption_score)

    # Upskilling Calculation: Higher progress means better upskilling, thus lower risk contribution
    upskilling_calc_factor = calculate_upskilling_factor(general_skills_progress, firm_specific_skills_progress)

    # Idiosyncratic Risk
    # For display, we want risk to go up if the factors are "bad"
    # So, higher human_capital_calc_factor (good) -> lower risk contribution
    # Higher company_risk_calc_score (good) -> lower risk contribution (inverted for calculation)
    # Higher upskilling_calc_factor (good) -> lower risk contribution
    
    # Re-evaluating Idiosyncratic Risk:
    # A simplified approach to combine them, where lower values of the factors mean lower risk.
    # human_capital_score: 0.5-2.0, higher is better. Convert to risk: 1 / (human_capital_score) for example. Range 0.5 to 2
    # company_risk_score: 0-1, higher is better. Convert to risk: 1 - company_risk_calc_score. Range 0 to 1
    # upskilling_factor: 0-1, higher is better (closer to 1-...). Convert to risk: 1 - upskilling_calc_factor. Range 0 to 1

    # Let's adjust the factors so they directly represent 'risk contribution' 0-1
    hc_risk_contribution = (1 - (human_capital_calc_factor - 0.5) / 1.5) # maps 0.5->1, 2.0->0
    cr_risk_contribution = 1 - company_risk_calc_score
    us_risk_contribution = 1 - upskilling_calc_factor

    idiosyncratic_risk = (hc_risk_contribution + cr_risk_contribution + us_risk_contribution) / 3 * 100


    # Systematic Risk
    systematic_risk = calculate_systematic_risk(base_occupational_hazard, economic_climate_index, ai_innovation_index)

    # AI-Q Score
    ai_q_score = calculate_ai_q_score(idiosyncratic_risk, systematic_risk)


    # --- Display Results ---
    st.subheader("Your Current AI-Q Score")
    col_metric1, col_metric2, col_metric3 = st.columns(3)
    with col_metric1:
        st.metric(label="Calculated Idiosyncratic Risk (Vulnerability)", value=f"{idiosyncratic_risk:.2f}%")
    with col_metric2:
        st.metric(label="Calculated Systematic Risk (Hazard)", value=f"{systematic_risk:.2f}%")
    with col_metric3:
        st.metric(label="Overall AI-Q Score", value=f"{ai_q_score:.2f}%", delta_color="inverse")

    st.markdown("---")

    # --- Visualizations ---
    st.subheader("Idiosyncratic Risk Factor Breakdown")
    st.write("This chart illustrates the contribution of Human Capital, Company Risk, and Upskilling to your Idiosyncratic Risk.")

    # Data for Idiosyncratic Risk Factor Breakdown
    # Ensure values represent contribution to risk, higher is worse.
    # hc_risk_contribution, cr_risk_contribution, us_risk_contribution are already 0-1, higher is worse.
    risk_data = pd.DataFrame({
        'Factor': ['Human Capital (Impact)', 'Company Risk (Impact)', 'Upskilling (Impact)'],
        'Contribution to Risk': [hc_risk_contribution, cr_risk_contribution, us_risk_contribution]
    })
    
    # Scale for visualization
    risk_data['Contribution to Risk'] = risk_data['Contribution to Risk'] * 100

    fig_idiosyncratic = px.bar(
        risk_data,
        x='Factor',
        y='Contribution to Risk',
        title='Idiosyncratic Risk Factor Contributions',
        color='Factor',
        color_discrete_map={
            'Human Capital (Impact)': 'lightblue',
            'Company Risk (Impact)': 'lightcoral',
            'Upskilling (Impact)': 'lightgreen'
        }
    )
    fig_idiosyncratic.update_layout(yaxis_range=[0, 100])
    st.plotly_chart(fig_idiosyncratic, use_container_width=True)

    st.markdown("---")

    st.subheader("AI-Q Score Dynamics: Idiosyncratic vs. Systematic Risk")
    st.write("This line chart shows how the overall AI-Q score is influenced by both Idiosyncratic and Systematic Risk components.")

    dynamics_df = pd.DataFrame({
        'Risk Type': ['Idiosyncratic Risk', 'Systematic Risk', 'Overall AI-Q Score'],
        'Value': [idiosyncratic_risk, systematic_risk, ai_q_score]
    })

    fig_dynamics = px.bar(dynamics_df, x='Risk Type', y='Value',
                        title='AI-Q Score Composition',
                        color='Risk Type',
                        color_discrete_map={
                            'Idiosyncratic Risk': 'cornflowerblue',
                            'Systematic Risk': 'indianred',
                            'Overall AI-Q Score': 'darkseagreen'
                        })
    fig_dynamics.update_layout(yaxis_range=[0, 100])
    st.plotly_chart(fig_dynamics, use_container_width=True)

