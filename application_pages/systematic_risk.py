
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from .calculations import calculate_base_occupational_hazard, calculate_systematic_risk
from .data_generation import generate_all_synthetic_data

def run_systematic_risk_page():
    st.header("Systematic Risk (Macro-level Risk)")

    st.markdown("""
    The Systematic Risk ($H_i$) represents the broader, macro-level factors that influence your job displacement risk
    due to AI. These factors are generally outside your direct control, such as the overall economic climate
    and the pace of AI innovation. A higher score means higher risk.
    """)

    st.subheader("Input Macroeconomic and Innovation Factors")

    # --- Base Occupational Hazard Inputs ---
    st.sidebar.subheader("Base Occupational Hazard")
    k_months = st.sidebar.slider(
        "Months Elapsed Since Transition Start (k)",
        min_value=0, max_value=36, value=0, step=1,
        help="Months elapsed since starting a transition pathway to a new industry/role."
    )
    TTV = st.sidebar.slider(
        "Total Time-to-Value Period (TTV in months)",
        min_value=1, max_value=36, value=12, step=1,
        help="Total time (in months) expected to fully transition to a new industry/role."
    )
    H_current = st.sidebar.slider(
        "Base Hazard of Current Industry (H_current)",
        min_value=0.0, max_value=1.0, value=0.7, step=0.05,
        help="Inherent AI-driven risk of your current occupation/industry (0=Low Risk, 1=High Risk)."
    )
    H_target = st.sidebar.slider(
        "Base Hazard of Target Industry (H_target)",
        min_value=0.0, max_value=1.0, value=0.3, step=0.05,
        help="Inherent AI-driven risk of your target occupation/industry if transitioning (0=Low Risk, 1=High Risk)."
    )

    H_base = calculate_base_occupational_hazard(k_months, TTV, H_current, H_target)
    st.write(f"**Calculated Base Occupational Hazard ($H_{{base}}(k)$):** `{H_base:.2f}`")
    st.caption("This reflects the dynamic risk of your occupation, adjusting as you transition.")


    # --- Economic Climate Inputs ---
    st.sidebar.subheader("Economic Climate Modifier")
    M_econ = st.sidebar.slider(
        "Economic Climate Modifier ($M_{{econ}}$)",
        min_value=0.5, max_value=1.5, value=1.0, step=0.05,
        help="Reflects the macroeconomic environment's effect on AI investment. Higher means more impact from economy on AI risk."
    )

    # --- AI Innovation Inputs ---
    st.sidebar.subheader("AI Innovation Index")
    IAI = st.sidebar.slider(
        "AI Innovation Index ($IAI$)",
        min_value=0.5, max_value=1.5, value=1.0, step=0.05,
        help="Momentum indicator reflecting velocity of AI development and adoption. Higher means faster AI advancement, increasing risk."
    )

    # Systematic Risk weights (fixed for simplicity in UI, can be sliders too)
    w_econ_sys, w_inno_sys = 0.5, 0.5 # These weights sum to 1

    H_i = calculate_systematic_risk(H_base, M_econ, IAI, w_econ_sys, w_inno_sys)
    st.metric(label="Your Systematic Risk ($H_i$)", value=f"{H_i:.2f}")
    st.caption("This is your macro-level risk score, combining occupational hazard, economic climate, and AI innovation. Higher is worse.")

    st.subheader("Systematic Risk Dynamics")
    st.markdown("Visualize how economic climate and AI innovation influence Systematic Risk.")

    synthetic_df = generate_all_synthetic_data(num_samples=200)

    # Recalculate H_i for the synthetic data to ensure consistency with our calculation logic
    synthetic_df['H_i_calculated'] = synthetic_df.apply(
        lambda row: calculate_systematic_risk(row['H_base'], row['M_econ'], row['IAI'], w_econ_sys, w_inno_sys),
        axis=1
    )

    col1, col2 = st.columns(2)

    with col1:
        st.write("#### Economic Climate vs. Systematic Risk")
        fig_econ = px.scatter(synthetic_df, x='M_econ', y='H_i_calculated',
                              title='Economic Climate Modifier vs. Systematic Risk',
                              labels={'M_econ': 'Economic Climate Modifier (Higher = More Impact)', 'H_i_calculated': 'Systematic Risk'},
                              trendline="ols",
                              hover_data=['H_base', 'IAI'])
        st.plotly_chart(fig_econ, use_container_width=True)
        st.markdown("As the Economic Climate Modifier increases, Systematic Risk tends to increase.")

    with col2:
        st.write("#### AI Innovation vs. Systematic Risk")
        fig_iai = px.scatter(synthetic_df, x='IAI', y='H_i_calculated',
                             title='AI Innovation Index vs. Systematic Risk',
                             labels={'IAI': 'AI Innovation Index (Higher = Faster Advancement)', 'H_i_calculated': 'Systematic Risk'},
                             trendline="ols",
                             hover_data=['H_base', 'M_econ'])
        st.plotly_chart(fig_iai, use_container_width=True)
        st.markdown("As the AI Innovation Index increases, Systematic Risk tends to increase.")

    st.write("#### Base Occupational Hazard Over Time (Scenario)")
    st.markdown("This chart illustrates how your occupational hazard might change during a transition period.")

    # Create a scenario for Base Occupational Hazard
    time_points = np.arange(0, TTV + 1, 1) # Months from 0 to TTV
    hazard_over_time = [calculate_base_occupational_hazard(t, TTV, H_current, H_target) for t in time_points]
    
    hazard_df = pd.DataFrame({
        'Months Elapsed': time_points,
        'Base Occupational Hazard': hazard_over_time
    })

    fig_base_hazard = px.line(hazard_df, x='Months Elapsed', y='Base Occupational Hazard',
                              title=f'Base Occupational Hazard During Transition (TTV={TTV} months)',
                              labels={'Base Occupational Hazard': 'Hazard Level'})
    st.plotly_chart(fig_base_hazard, use_container_width=True)
    st.markdown("The Base Occupational Hazard transitions from your current industry's hazard to your target industry's hazard over the Time-to-Value (TTV) period.")

