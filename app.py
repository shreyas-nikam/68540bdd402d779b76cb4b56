
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="AI-Q Score Visualizer", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("AI-Q Score Visualizer")
st.divider()

st.markdown("""
In this lab, we explore the "AI-Q Score", a metric developed to quantify an individual's risk of job displacement due due to the increasing impact of Artificial Intelligence on the job market. This application allows you to interactively adjust various factors that contribute to this score and visualize their real-time impact.

### Core Concepts

The AI-Q Score is composed of two main components:

1.  **Idiosyncratic Risk ($$V_i(t)$$)**: This represents the individual-specific risk that can be influenced by personal actions and attributes. It is a function of:
    *   **Human Capital ($$F_{HC}$$)**: Your educational background, professional experience, role, and institution tier.
    *   **Company Risk ($$F_{CR}$$)**: The stability, financial health, and AI adoption strategy of your current employer.
    *   **Upskilling ($$F_{US}$$)**: Your efforts in acquiring new general and firm-specific skills.

    The formula for Idiosyncratic Risk is:
    $$V_i(t) = f(F_{HC}, F_{CR}, F_{US})$$

    Where:
    *   $$F_{HC} = f_{role} \cdot f_{level} \cdot f_{field} \cdot f_{school} \cdot f_{exp}$$
    *   $$F_{CR} = w_1 \cdot S_{senti} + w_2 \cdot S_{fin} + w_3 \cdot S_{growth}$$
    *   $$F_{US} = 1 - (\gamma_{gen} \cdot P_{gen}(t) + \gamma_{spec} \cdot P_{spec}(t))$$

2.  **Systematic Risk ($$H_i$$)**: This reflects the broader, macro-level risks influenced by the economic climate and the pace of AI innovation. These factors are generally beyond an individual's direct control. It is a function of:
    *   **Base Occupational Hazard ($$H_{base}(t)$$)**: The inherent risk of your occupation, potentially influenced by career transitions.
    *   **Economic Climate Modifier ($$M_{econ}$$)**: Factors like GDP growth, sector employment, and interest rates.
    *   **AI Innovation Index ($$IAI$$)**: The velocity of AI development, measured by VC funding, R&D spend, and public salience.

    The formula for Systematic Risk is:
    $$H_i = H_{base}(t) \cdot (w_{econ} \cdot M_{econ} + w_{inno} \cdot IAI)$$

    Where:
    *   $$H_{base}(k) = (1 - \frac{k}{TTV}) \cdot H_{current} + (\frac{k}{TTV}) \cdot H_{target}$$
    *   $$M_{econ} = f(GDP\ Growth, Sector\ Employment, Interest\ Rates)$$
    *   $$IAI = f(VC\ Funding, R\&D\ Spend, Public\ Salience)$$

The AI-Q Score is the combination of these two risk components, providing a holistic view of an individual's vulnerability to AI-driven job displacement.

Use the sidebar navigation to explore different aspects of the AI-Q Score calculation and its contributing factors.
"""
# Your code starts here
page = st.sidebar.selectbox(label="Navigation", options=["AI-Q Score Calculation", "Systematic Risk Dynamics", "Raw Data & Insights"])

# Create a directory for application pages if it doesn't exist (not applicable in this execution environment)
# import os
# if not os.path.exists("application_pages"):
#     os.makedirs("application_pages")

if page == "AI-Q Score Calculation":
    from application_pages.ai_q_score_calculation import run_ai_q_score_calculation_page
    run_ai_q_score_calculation_page()
elif page == "Systematic Risk Dynamics":
    from application_pages.systematic_risk_dynamics import run_systematic_risk_dynamics_page
    run_systematic_risk_dynamics_page()
elif page == "Raw Data & Insights":
    from application_pages.raw_data_insights import run_raw_data_insights_page
    run_raw_data_insights_page()

# Your code ends

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
