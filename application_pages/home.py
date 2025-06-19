
import streamlit as st

def run_home_page():
    st.header("Welcome to the AI-Q Score Visualizer")
    st.markdown("""
    This application helps you understand and visualize the **AI-Q Score**, a metric designed to quantify an individual's risk of job displacement due to Artificial Intelligence.
    It breaks down this complex risk into manageable components, allowing you to explore the factors that influence your professional vulnerability and the broader economic landscape.

    Understanding your AI-Q Score can empower you to make informed decisions about upskilling, career planning, and adapting to the evolving job market.

    ---

    ### Core Concepts and Mathematical Foundations

    The AI-Q Score is a comprehensive metric derived from two main components: **Idiosyncratic Risk** and **Systematic Risk**. Each component is calculated based on several underlying factors.

    #### 1. Idiosyncratic Risk ( $V_i(t)$ )

    Idiosyncratic Risk, or Vulnerability, is the individual-specific risk that can be actively managed through personal actions. It is calculated as a composite of Human Capital, Company Risk, and Upskilling efforts.

    $$
    V_i(t) = f(F_{HC}, F_{CR}, F_{US})
    $$

    Where:
    - $V_i(t)$: Idiosyncratic Risk at time $t$
    - $F_{HC}$: Human Capital Factor
    - $F_{CR}$: Company Risk Factor
    - $F_{US}$: Upskilling Factor

    This formula quantifies the individual-specific risk, which can be actively managed through personal actions.

    ##### 1.1 Human Capital Factor ( $F_{HC}$ )

    This factor assesses an individual's resilience based on educational and professional background. A higher Human Capital Factor generally indicates lower idiosyncratic risk.

    $$
    F_{HC} = f_{role} \cdot f_{level} \cdot f_{field} \cdot f_{school} \cdot f_{exp}
    $$

    Where:
    - $F_{HC}$: Human Capital Factor
    - $f_{role}$: Role Multiplier (reflects inherent AI-vulnerability of job role)
    - $f_{level}$: Education Level Factor (higher education often correlates with specialized skills)
    - $f_{field}$: Education Field Factor (certain fields may be less susceptible to AI automation)
    - $f_{school}$: Institution Tier Factor (quality of educational institution)
    - $f_{exp}$: Experience Factor (years of experience indicating expertise and adaptability)

    This formula evaluates the foundational resilience of an individual.

    ##### 1.2 Company Risk Factor ( $F_{CR}$ )

    This factor quantifies the stability and growth prospects of the individual's current employer, particularly regarding their adoption of AI and financial health. A company with higher risk contributes to higher individual idiosyncratic risk.

    $$
    F_{CR} = w_1 \cdot S_{senti} + w_2 \cdot S_{fin} + w_3 \cdot S_{growth}
    $$

    Where:
    - $F_{CR}$: Company Risk Factor
    - $S_{senti}$: Sentiment Score (market/internal sentiment regarding company's future)
    - $S_{fin}$: Financial Health Score (company's financial stability)
    - $S_{growth}$: Growth & AI Adoption Score (how aggressively company integrates AI)
    - $w_1, w_2, w_3$: Weights for each score (calibrated importance)

    This metric reflects the financial health and AI readiness of the company. Note that for calculation, higher $S_{senti}$, $S_{fin}$, $S_{growth}$ contribute to *lower* company risk, and thus lower $F_{CR}$.

    ##### 1.3 Upskilling Factor ( $F_{US}$ )

    This factor quantifies individual upskilling efforts, differentiating between skill types. Engaging in upskilling reduces idiosyncratic risk.

    $$
    F_{US} = 1 - (\gamma_{gen} \cdot P_{gen}(t) + \gamma_{spec} \cdot P_{spec}(t))
    $$

    Where:
    - $F_{US}$: Upskilling Factor
    - $P_{gen}(t)$: Training progress in general skills at time $t$ (e.g., data literacy, critical thinking)
    - $P_{spec}(t)$: Training progress in firm-specific skills at time $t$ (relevant to current company/industry)
    - $\gamma_{gen}, \gamma_{spec}$: Weighting parameters for general and specific skills

    This formula recognizes and rewards continuous learning and skill development. A higher $P_{gen}(t)$ or $P_{spec}(t)$ leads to a *lower* $F_{US}$, representing less risk due to upskilling.

    #### 2. Systematic Risk ( $H_i$ )

    The Systematic Risk reflects the occupational hazard and broader economic and technological environment. This component is largely outside an individual's direct control.

    $$
    H_i = H_{base}(t) \cdot (w_{econ} \cdot M_{econ} + w_{inno} \cdot IAI)
    $$

    Where:
    - $H_i$: Systematic Risk
    - $H_{base}(t)$: Base Occupational Hazard at time $t$
    - $M_{econ}$: Economic Climate Modifier
    - $IAI$: AI Innovation Index
    - $w_{econ}, w_{inno}$: Calibration weights

    This formula represents the macro-level automation risk influenced by economic and technological factors.

    ##### 2.1 Base Occupational Hazard ( $H_{base}(k)$ )

    The foundational score of an occupation, accounting for the time it takes to transition to a new industry.

    $$
    H_{base}(k) = (1 - \frac{k}{TTV}) \cdot H_{current} + (\frac{k}{TTV}) \cdot H_{target}
    $$

    Where:
    - $H_{base}(k)$: Base Occupational Hazard after *k* months
    - $k$: Months elapsed since transition pathway completion
    - $TTV$: Total Time-to-Value period (time to fully transition)
    - $H_{current}$: Base Occupational Hazard of the original industry
    - $H_{target}$: Base Occupational Hazard of the new target industry

    The formula accounts for the dynamic nature of risk during a career transition.

    ##### 2.2 Economic Climate Modifier ( $M_{econ}$ )

    A composite index reflecting the macroeconomic environment's effect on AI investment and adoption.

    $$
    M_{econ} = f(GDP\ Growth, Sector\ Employment, Interest\ Rates)
    $$

    Where:
    - $M_{econ}$: Economic Climate Modifier
    - $GDP\ Growth$: GDP Growth rate
    - $Sector\ Employment$: Employment in the relevant sector
    - $Interest\ Rates$: Prevailing interest rates

    This modifier reflects the influence of the macro-economic climate. Higher positive values for $M_{econ}$ could imply a more aggressive AI adoption environment, increasing systematic risk.

    ##### 2.3 AI Innovation Index ( $IAI$ )

    A momentum indicator reflecting the velocity of AI development and adoption.

    $$
    IAI = f(VC\ Funding, R\&D\ Spend, Public\ Salience)
    $$

    Where:
    - $IAI$: AI Innovation Index
    - $VC\ Funding$: Venture Capital Funding in AI
    - $R\&D\ Spend$: Research and Development Spending in AI
    - $Public\ Salience$: Public awareness/discussion of AI

    This index captures the speed of technological change. A higher $IAI$ indicates faster AI advancement, contributing to higher systematic risk.

    ---

    Navigate through the sidebar to explore these factors interactively and calculate your AI-Q Score.
    """
    )
