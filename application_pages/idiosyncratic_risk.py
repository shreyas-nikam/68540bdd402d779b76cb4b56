
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from .calculations import calculate_human_capital_factor, calculate_company_risk_factor, calculate_upskilling_factor, calculate_idiosyncratic_risk
from .data_generation import generate_all_synthetic_data

def run_idiosyncratic_risk_page():
    st.header("Idiosyncratic Risk (Your Personal Risk)")

    st.markdown("""
    The Idiosyncratic Risk ($V_i(t)$) represents the factors that are specific to you as an individual,
    and which you can largely influence. It's composed of your **Human Capital**, your **Company Risk**,
    and your **Upskilling** efforts. A higher score means higher risk.
    """)

    st.subheader("Input Your Personal Factors")

    # --- Human Capital Inputs ---
    st.sidebar.subheader("Human Capital Factors")
    f_role = st.sidebar.select_slider(
        "Role Multiplier (f_role)",
        options=[round(x, 2) for x in np.arange(0.5, 1.51, 0.05)],
        value=1.0,
        help="Higher value means role is more susceptible to AI automation."
    )
    f_level = st.sidebar.select_slider(
        "Education Level Factor (f_level)",
        options=[round(x, 2) for x in np.arange(0.7, 1.31, 0.05)],
        value=1.0,
        help="Higher value means education level offers less resilience."
    )
    f_field = st.sidebar.select_slider(
        "Education Field Factor (f_field)",
        options=[round(x, 2) for x in np.arange(0.6, 1.41, 0.05)],
        value=1.0,
        help="Higher value means education field offers less resilience."
    )
    f_school = st.sidebar.select_slider(
        "Institution Tier Factor (f_school)",
        options=[round(x, 2) for x in np.arange(0.8, 1.21, 0.05)],
        value=1.0,
        help="Higher value means institution tier offers less resilience."
    )
    f_exp = st.sidebar.slider(
        "Experience Factor (Years of Experience)",
        min_value=0.0, max_value=30.0, value=10.0, step=1.0,
        help="Years of experience. Higher experience generally means more resilience (lower factor here if it was inverse)."
    )
    # The f_exp in formula should be inverse of experience. Let's make it intuitive for user input.
    # Higher experience should reduce risk, so a higher f_exp input should translate to a lower f_exp factor for calculation.
    # Let's map 0-30 years to a factor from 1.1 (low experience, high risk) to 0.9 (high experience, low risk).
    exp_factor_mapped = np.interp(f_exp, [0, 30], [1.1, 0.9])

    F_HC = calculate_human_capital_factor(f_role, f_level, f_field, f_school, exp_factor_mapped)
    st.write(f"**Calculated Human Capital Factor ($F_{{HC}}$):** `{F_HC:.2f}`")
    st.caption("A higher $F_{HC}$ value indicates higher human capital resilience (lower individual risk from human capital).")

    # --- Company Risk Inputs ---
    st.sidebar.subheader("Company Risk Factors")
    S_senti = st.sidebar.slider("Sentiment Score (0=Bad, 1=Good)", 0.0, 1.0, 0.7, 0.05)
    S_fin = st.sidebar.slider("Financial Health Score (0=Bad, 1=Good)", 0.0, 1.0, 0.6, 0.05)
    S_growth = st.sidebar.slider("Growth & AI Adoption Score (0=Low, 1=High)", 0.0, 1.0, 0.8, 0.05)
    
    # Company risk weights (fixed for simplicity in UI, can be sliders too)
    w1_cr, w2_cr, w3_cr = 0.3, 0.4, 0.3 # These weights sum to 1

    F_CR = calculate_company_risk_factor(S_senti, S_fin, S_growth, w1_cr, w2_cr, w3_cr)
    st.write(f"**Calculated Company Risk Factor ($F_{{CR}}$):** `{F_CR:.2f}`")
    st.caption("A higher $F_{CR}$ value indicates higher company-specific risk.")

    # --- Upskilling Inputs ---
    st.sidebar.subheader("Upskilling Factors")
    P_gen = st.sidebar.slider("General Skills Training Progress (0=None, 1=High)", 0.0, 1.0, 0.5, 0.05)
    P_spec = st.sidebar.slider("Firm-Specific Skills Training Progress (0=None, 1=High)", 0.0, 1.0, 0.6, 0.05)
    
    # Upskilling weights (fixed for simplicity)
    gamma_gen, gamma_spec = 0.5, 0.5 # These weights sum to 1

    F_US = calculate_upskilling_factor(P_gen, P_spec, gamma_gen, gamma_spec)
    st.write(f"**Calculated Upskilling Factor ($F_{{US}}$):** `{F_US:.2f}`")
    st.caption("A lower $F_{US}$ value indicates more upskilling effort and thus lower individual risk from this factor.")

    # --- Idiosyncratic Risk Calculation ---
    V_i = calculate_idiosyncratic_risk(F_HC, F_CR, F_US)
    st.metric(label="Your Idiosyncratic Risk ($V_i(t)$)", value=f"{V_i:.2f}")
    st.caption("This is your personal risk score, combining human capital, company risk, and upskilling. Higher is worse.")

    st.subheader("Factor Breakdown of Idiosyncratic Risk")
    
    # To visualize the breakdown, we need to consider how each contributes to the total risk.
    # The `calculate_idiosyncratic_risk` function converts F_HC and F_US to risk contributions.
    max_F_HC_expected = 1.5 * 1.3 * 1.4 * 1.2 * 1.1 # from data_generation upper bounds = 3.54
    max_F_CR_expected = 1.0
    max_F_US_expected = 1.0

    risk_contrib_HC_calc = 1 - (F_HC / max_F_HC_expected) if max_F_HC_expected > 0 else 1
    risk_contrib_CR_calc = F_CR / max_F_CR_expected if max_F_CR_expected > 0 else 1
    risk_contrib_US_calc = 1 - (F_US / max_F_US_expected) if max_F_US_expected > 0 else 1

    # Normalize these contributions to sum to 1 for the pie chart
    total_risk_contrib = risk_contrib_HC_calc + risk_contrib_CR_calc + risk_contrib_US_calc
    
    if total_risk_contrib > 0:
        hc_pct = (risk_contrib_HC_calc / total_risk_contrib) * 100
        cr_pct = (risk_contrib_CR_calc / total_risk_contrib) * 100
        us_pct = (risk_contrib_US_calc / total_risk_contrib) * 100
    else: # Handle case where total_risk_contrib is zero to avoid division by zero
        hc_pct, cr_pct, us_pct = 0, 0, 0
        if risk_contrib_HC_calc == 0 and risk_contrib_CR_calc == 0 and risk_contrib_US_calc == 0:
            st.warning("All risk contributions are zero. Adjust inputs for a breakdown visualization.")
        else: # One of them is non-zero but the sum is still zero (e.g. if some are negative, which they shouldn't be here)
            st.error("Could not normalize risk contributions for breakdown visualization.")


    risk_data = pd.DataFrame({
        'Factor': ['Human Capital', 'Company Risk', 'Upskilling'],
        'Contribution': [hc_pct, cr_pct, us_pct]
    })

    fig_pie = px.pie(risk_data, values='Contribution', names='Factor', title='Contribution to Idiosyncratic Risk',
                     hole=0.3)
    st.plotly_chart(fig_pie, use_container_width=True)

    st.subheader("Interactive Analysis with Synthetic Data")
    st.markdown("Explore how different factors impact Idiosyncratic Risk based on a synthetic dataset.")

    synthetic_df = generate_all_synthetic_data(num_samples=200)
    
    # Filter for relevant columns
    idiosyncratic_factors_df = synthetic_df[['F_HC', 'F_CR', 'F_US']]
    
    # Recalculate V_i for the synthetic data to ensure consistency with our calculation logic
    # This also allows us to use the mapped risk contributions directly for scatter plots if needed.
    # Apply the same risk contribution mapping as in calculate_idiosyncratic_risk
    synthetic_df['risk_contrib_HC'] = 1 - (synthetic_df['F_HC'] / max_F_HC_expected)
    synthetic_df['risk_contrib_CR'] = synthetic_df['F_CR'] / max_F_CR_expected
    synthetic_df['risk_contrib_US'] = 1 - (synthetic_df['F_US'] / max_F_US_expected)
    
    # Calculate overall Idiosyncratic Risk for each synthetic sample
    synthetic_df['V_i'] = synthetic_df[['risk_contrib_HC', 'risk_contrib_CR', 'risk_contrib_US']].mean(axis=1)


    col1, col2 = st.columns(2)

    with col1:
        st.write("#### Human Capital vs. Idiosyncratic Risk")
        fig_hc = px.scatter(synthetic_df, x='F_HC', y='V_i',
                            title='Human Capital Factor vs. Idiosyncratic Risk',
                            labels={'F_HC': 'Human Capital Factor (Higher = More Resilience)', 'V_i': 'Idiosyncratic Risk'},
                            trendline="ols",
                            hover_data=['role_multiplier', 'education_level_factor', 'experience_factor'])
        st.plotly_chart(fig_hc, use_container_width=True)
        st.markdown("As Human Capital (F_HC) increases, Idiosyncratic Risk generally decreases.")

    with col2:
        st.write("#### Company Risk vs. Idiosyncratic Risk")
        fig_cr = px.scatter(synthetic_df, x='F_CR', y='V_i',
                            title='Company Risk Factor vs. Idiosyncratic Risk',
                            labels={'F_CR': 'Company Risk Factor (Higher = More Risk)', 'V_i': 'Idiosyncratic Risk'},
                            trendline="ols",
                            hover_data=['sentiment_score', 'financial_health_score', 'growth_ai_adoption_score'])
        st.plotly_chart(fig_cr, use_container_width=True)
        st.markdown("As Company Risk (F_CR) increases, Idiosyncratic Risk generally increases.")

    col3, col4 = st.columns(2)
    with col3:
        st.write("#### Upskilling vs. Idiosyncratic Risk")
        fig_us = px.scatter(synthetic_df, x='P_gen', y='V_i',
                            title='General Skills Progress vs. Idiosyncratic Risk',
                            labels={'P_gen': 'General Skills Progress (Higher = More Upskilling)', 'V_i': 'Idiosyncratic Risk'},
                            trendline="ols",
                            hover_data=['P_spec'])
        st.plotly_chart(fig_us, use_container_width=True)
        st.markdown("As upskilling progress increases (higher P_gen/P_spec), Idiosyncratic Risk generally decreases.")

    with col4:
        st.write("#### Interaction: F_US vs. V_i")
        fig_us_factor = px.scatter(synthetic_df, x='F_US', y='V_i',
                                    title='Upskilling Factor vs. Idiosyncratic Risk',
                                    labels={'F_US': 'Upskilling Factor (Lower = More Upskilling)', 'V_i': 'Idiosyncratic Risk'},
                                    trendline="ols",
                                    hover_data=['P_gen', 'P_spec'])
        st.plotly_chart(fig_us_factor, use_container_width=True)
        st.markdown("As the Upskilling Factor (F_US) *decreases* (meaning more upskilling effort), Idiosyncratic Risk generally decreases.")

