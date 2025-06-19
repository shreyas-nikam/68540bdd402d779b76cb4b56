# Overview 2
This document provides technical specifications for a Streamlit application named "AI-Q Score Visualizer". The application's primary goal is to visualize the AI-Q Score, a metric that quantifies an individual's risk of job displacement due to AI, as described in [Krishnamurthy, 2025]. The application utilizes a synthetic dataset to demonstrate the AI-Q score's calculation and the impact of various factors on overall risk. Interactive elements, including data input forms and charts, enable users to explore the concepts and visualize real-time updates.

## Step-by-Step Development Process

1.  **Setup Environment**: Create a new Python environment and install the required libraries (Streamlit, Pandas, NumPy, Matplotlib/Plotly).
2.  **Synthetic Data Generation**: Develop a script to generate a synthetic dataset that mimics the structure and characteristics of the data and formulas from [Krishnamurthy, 2025]. This dataset should include columns representing human capital, company risk, upskilling efforts, economic climate, and AI innovation indices.
3.  **Implement AI-Q Score Calculation**: Implement the formulas described in [Krishnamurthy, 2025] to calculate the Idiosyncratic Risk and Systematic Risk, leading to the final AI-Q score.
4.  **Create Streamlit Application**:
    *   Create a Streamlit application structure with a main title and introduction.
    *   Add input forms and widgets for users to modify parameters related to their skills, educational attainment, and employment details.
    *   Implement interactive charts (line charts, bar graphs, scatter plots) to display trends and correlations based on the synthetic dataset.
    *   Visualize the factor breakdown for Idiosyncratic Risk (Human Capital, Company Risk, Upskilling) and the dynamics of Systematic Risk (Economic Climate, AI Innovation).
    *   Display the calculated AI-Q score in real-time based on the user's inputs and the synthetic data.
5.  **Testing and Refinement**: Test the application with different scenarios and refine the user interface and visualization to ensure clarity and ease of use.

## Core Concepts and Mathematical Foundations

### Idiosyncratic Risk ( $V_i(t)$ )
The Idiosyncratic Risk, or Vulnerability, is calculated as a composite of Human Capital, Company Risk, and Upskilling efforts.
$$
V_i(t) = f(F_{HC}, F_{CR}, F_{US})
$$
Where:
- $V_i(t)$: Idiosyncratic Risk at time $t$
- $F_{HC}$: Human Capital Factor
- $F_{CR}$: Company Risk Factor
- $F_{US}$: Upskilling Factor

This formula quantifies the individual-specific risk, which can be actively managed through personal actions.

### Human Capital Factor ( $F_{HC}$ )
This factor assesses an individual's resilience based on educational and professional background.
$$
F_{HC} = f_{role} \cdot f_{level} \cdot f_{field} \cdot f_{school} \cdot f_{exp}
$$
Where:
- $F_{HC}$: Human Capital Factor
- $f_{role}$: Role Multiplier
- $f_{level}$: Education Level Factor
- $f_{field}$: Education Field Factor
- $f_{school}$: Institution Tier Factor
- $f_{exp}$: Experience Factor

This formula evaluates the foundational resilience of an individual.

### Company Risk Factor ( $F_{CR}$ )
This factor quantifies the stability and growth prospects of the individual's current employer.
$$
F_{CR} = w_1 \cdot S_{senti} + w_2 \cdot S_{fin} + w_3 \cdot S_{growth}
$$
Where:
- $F_{CR}$: Company Risk Factor
- $S_{senti}$: Sentiment Score
- $S_{fin}$: Financial Health Score
- $S_{growth}$: Growth & AI Adoption Score
- $w_1, w_2, w_3$: Weights for each score

This metric reflects the financial health and AI readiness of the company.

### Upskilling Factor ( $F_{US}$ )
This factor quantifies individual upskilling efforts, differentiating between skill types.
$$
F_{US} = 1 - (\gamma_{gen} \cdot P_{gen}(t) + \gamma_{spec} \cdot P_{spec}(t))
$$
Where:
- $F_{US}$: Upskilling Factor
- $P_{gen}(t)$: Training progress in general skills at time $t$
- $P_{spec}(t)$: Training progress in firm-specific skills at time $t$
- $\gamma_{gen}, \gamma_{spec}$: Weighting parameters for general and specific skills

This formula recognizes and rewards continuous learning and skill development.

### Systematic Risk ( $H_i$ )
The Systematic Risk reflects the occupational hazard and broader environment.
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

### Base Occupational Hazard ( $H_{base}(k)$ )
The foundational score of an occupation.
$$
H_{base}(k) = (1 - \frac{k}{TTV}) \cdot H_{current} + (\frac{k}{TTV}) \cdot H_{target}
$$
Where:
- $H_{base}(k)$: Base Occupational Hazard after *k* months
- $k$: Months elapsed since transition pathway completion
- $TTV$: Total Time-to-Value period
- $H_{current}$: Base Occupational Hazard of the original industry
- $H_{target}$: Base Occupational Hazard of the new target industry

The formula accounts for the time it takes to transition to a new industry.

### Economic Climate Modifier ( $M_{econ}$ )
A composite index reflecting the macroeconomic environment's effect on AI investment.
$$
M_{econ} = f(GDP\ Growth, Sector\ Employment, Interest\ Rates)
$$
Where:
- $M_{econ}$: Economic Climate Modifier
- $GDP\ Growth$: GDP Growth rate
- $Sector\ Employment$: Employment in the sector
- $Interest\ Rates$: Interest rates

This modifier reflects the influence of the macro-economic climate.

### AI Innovation Index ( $IAI$ )
A momentum indicator reflecting the velocity of AI development and adoption.
$$
IAI = f(VC\ Funding, R\&D\ Spend, Public\ Salience)
$$
Where:
- $IAI$: AI Innovation Index
- $VC\ Funding$: Venture Capital Funding in AI
- $R\&D\ Spend$: Research and Development Spending in AI
- $Public\ Salience$: Public awareness/discussion of AI

This index captures the speed of technological change.

## Required Libraries and Dependencies

*   **Streamlit**: Used to create the user interface and interactive components.
    *   Version: (Latest)
    *   Import: `import streamlit as st`
    *   Usage: `st.title()`, `st.slider()`, `st.line_chart()`
*   **Pandas**: Used for data manipulation and analysis.
    *   Version: (Latest)
    *   Import: `import pandas as pd`
    *   Usage: `pd.DataFrame()`, `df['column_name']`
*   **NumPy**: Used for numerical operations and array manipulation.
    *   Version: (Latest)
    *   Import: `import numpy as np`
    *   Usage: `np.mean()`, `np.random.rand()`
*   **Matplotlib/Plotly**: Used for creating visualizations and charts.
    *   Versions: Matplotlib (Latest), Plotly (Latest)
    *   Import: `import matplotlib.pyplot as plt` or `import plotly.express as px`
    *   Usage: `plt.plot()`, `plt.bar()`, `px.scatter()`

## Implementation Details

1.  **Data Generation**:
    *   Use NumPy's random number generation capabilities to create synthetic data for each factor (Human Capital, Company Risk, Upskilling, Economic Climate, AI Innovation).
    *   Ensure that the generated data has realistic ranges and distributions.
    *   Store the generated data in a Pandas DataFrame.
2.  **AI-Q Score Calculation**:
    *   Implement the formulas for Idiosyncratic Risk and Systematic Risk as Python functions.
    *   Use the Pandas DataFrame to store and process the input data for these functions.
    *   Display the calculated AI-Q score prominently in the application.
3.  **Visualization**:
    *   Use Streamlit's charting capabilities (`st.line_chart`, `st.bar_chart`, `st.scatter_chart`) to create interactive charts that display the relationships between different factors and the AI-Q score.
    *   Allow users to modify parameters through Streamlit widgets (e.g., sliders, number inputs, select boxes) and observe the real-time impact on the visualizations.
    *   Incorporate informative labels, titles, and tooltips to enhance the clarity and usability of the charts.
4.  **User Interface**:
    *   Use Streamlit's layout capabilities (`st.sidebar`, `st.columns`, `st.expander`) to organize the application into logical sections.
    *   Provide clear instructions and explanations for each input parameter and visualization.
    *   Design the application to be responsive and user-friendly on different screen sizes.

## User Interface Components

1.  **Title and Introduction**: Display a clear title ("AI-Q Score Visualizer") and a brief introduction explaining the purpose of the application.
2.  **Input Forms**: Provide input forms or widgets in the sidebar to allow users to modify the following parameters:
    *   **Human Capital**:
        *   Role Multiplier (dropdown)
        *   Education Level (dropdown)
        *   Education Field (dropdown)
        *   Institution Tier (dropdown)
        *   Years of Experience (slider)
    *   **Company Risk**:
        *   Sentiment Score (slider)
        *   Financial Health Score (slider)
        *   Growth & AI Adoption Score (slider)
    *   **Upskilling**:
        *   General Skills Training Progress (slider)
        *   Firm-Specific Skills Training Progress (slider)
    *   **Economic Climate**:
        *   Economic Climate Index (slider)
    *   **AI Innovation**:
        *   AI Innovation Index (slider)
3.  **AI-Q Score Display**: Display the calculated AI-Q score prominently using `st.metric`.
4.  **Visualization Section**:
    *   **Factor Breakdown**: Use a bar chart or pie chart to visualize the contribution of Human Capital, Company Risk, and Upskilling to the Idiosyncratic Risk.
    *   **Systematic Risk Dynamics**: Use a line chart to show how the Economic Climate and AI Innovation indices affect the Systematic Risk.  The x-axis could represent time or different scenarios.
5. **Explanatory Text**: Use `st.markdown` to include definitions, practical examples, and explanations of the formulas and concepts behind the AI-Q Score.  Ensure that all mathematical content follows the LaTeX formatting rules.

