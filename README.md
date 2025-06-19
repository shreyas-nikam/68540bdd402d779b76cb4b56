
# AI-Q Score Visualizer

This repository contains the Streamlit application for the "AI-Q Score Visualizer" lab. The application aims to help users understand and visualize the AI-Q Score, a metric designed to quantify an individual's risk of job displacement due to advancements in Artificial Intelligence.

## Overview of the AI-Q Score

The AI-Q Score is a comprehensive metric described in [Krishnamurthy, 2025] that evaluates an individual's vulnerability to AI-driven job displacement. It comprises two main components: Idiosyncratic Risk and Systematic Risk.

### Idiosyncratic Risk ($V_i(t)$)

Idiosyncratic Risk, or Vulnerability, is an individual-specific risk that can be actively managed through personal actions. It is calculated as a composite of three key factors:

$$V_i(t) = f(F_{HC}, F_{CR}, F_{US})$$

Where:
- $V_i(t)$: Idiosyncratic Risk at time $t$
- $F_{HC}$: Human Capital Factor
- $F_{CR}$: Company Risk Factor
- $F_{US}$: Upskilling Factor

#### Human Capital Factor ($F_{HC}$)

This factor assesses an individual's resilience based on their educational and professional background. It considers various aspects of an individual's profile:

$$F_{HC} = f_{role} \cdot f_{level} \cdot f_{field} \cdot f_{school} \cdot f_{exp}$$

Where:
- $F_{HC}$: Human Capital Factor
- $f_{role}$: Role Multiplier (e.g., impact of current job role)
- $f_{level}$: Education Level Factor (e.g., degree attained)
- $f_{field}$: Education Field Factor (e.g., STEM vs. Humanities)
- $f_{school}$: Institution Tier Factor (e.g., prestige of educational institution)
- $f_{exp}$: Experience Factor (e.g., years in the industry)

This formula highlights that a strong educational background, relevant field expertise, and significant professional experience contribute to lower individual risk.

#### Company Risk Factor ($F_{CR}$)

This factor quantifies the stability and growth prospects of the individual's current employer, particularly concerning their adoption of AI and financial health.

$$F_{CR} = w_1 \cdot S_{senti} + w_2 \cdot S_{fin} + w_3 \cdot S_{growth}$$

Where:
- $F_{CR}$: Company Risk Factor
- $S_{senti}$: Sentiment Score (e.g., market perception, employee morale)
- $S_{fin}$: Financial Health Score (e.g., profitability, debt levels)
- $S_{growth}$: Growth & AI Adoption Score (e.g., innovation, investment in AI)
- $w_1, w_2, w_3$: Weights for each score

A company that is financially robust, has positive market sentiment, and actively invests in AI adoption tends to offer more job security.

#### Upskilling Factor ($F_{US}$)

This factor recognizes and rewards continuous learning and skill development, differentiating between general and firm-specific skills.

$$F_{US} = 1 - (\gamma_{gen} \cdot P_{gen}(t) + \gamma_{spec} \cdot P_{spec}(t))$$

Where:
- $F_{US}$: Upskilling Factor
- $P_{gen}(t)$: Training progress in general skills at time $t$ (e.g., transferable skills like data analysis)
- $P_{spec}(t)$: Training progress in firm-specific skills at time $t$ (e.g., internal software proficiency)
- $\gamma_{gen}, \gamma_{spec}$: Weighting parameters for general and specific skills

Actively engaging in upskilling, especially in future-proof skills, can significantly reduce an individual's Idiosyncratic Risk.

### Systematic Risk ($H_i$)

Systematic Risk reflects the broader occupational hazard and the general economic and technological environment, largely beyond an individual's direct control.

$$H_i = H_{base}(t) \cdot (w_{econ} \cdot M_{econ} + w_{inno} \cdot IAI)$$

Where:
- $H_i$: Systematic Risk
- $H_{base}(t)$: Base Occupational Hazard at time $t$
- $M_{econ}$: Economic Climate Modifier
- $IAI$: AI Innovation Index
- $w_{econ}, w_{inno}$: Calibration weights

This formula indicates that the overall market conditions and the pace of AI innovation influence the macro-level risk.

#### Base Occupational Hazard ($H_{base}(k)$)

This represents the foundational risk score of an occupation, which can change as an individual transitions to a new industry.

$$H_{base}(k) = (1 - \frac{k}{TTV}) \cdot H_{current} + (\frac{k}{TTV}) \cdot H_{target}$$

Where:
- $H_{base}(k)$: Base Occupational Hazard after *k* months
- $k$: Months elapsed since transition pathway completion
- $TTV$: Total Time-to-Value period (time to fully transition)
- $H_{current}$: Base Occupational Hazard of the original industry
- $H_{target}$: Base Occupational Hazard of the new target industry

This formula accounts for the time it takes to mitigate risk by transitioning to a less vulnerable industry.

#### Economic Climate Modifier ($M_{econ}$)

A composite index reflecting the macroeconomic environment's effect on AI investment and adoption.

$$M_{econ} = f(GDP\ Growth, Sector\ Employment, Interest\ Rates)$$

Where:
- $M_{econ}$: Economic Climate Modifier
- $GDP\ Growth$: GDP Growth rate
- $Sector\ Employment$: Employment in the sector
- $Interest\ Rates$: Interest rates

A robust economic climate generally supports innovation and job creation, but can also accelerate AI adoption, leading to shifts in employment.

#### AI Innovation Index ($IAI$)

A momentum indicator reflecting the velocity of AI development and adoption.

$$IAI = f(VC\ Funding, R\&D\ Spend, Public\ Salience)$$

Where:
- $IAI$: AI Innovation Index
- $VC\ Funding$: Venture Capital Funding in AI
- $R\&D\ Spend$: Research and Development Spending in AI
- $Public\ Salience$: Public awareness/discussion of AI

A higher AI Innovation Index suggests faster technological change and potentially quicker job displacement in certain sectors.

## Application Features

The Streamlit application provides:
- Interactive input forms to adjust parameters for Human Capital, Company Risk, Upskilling, Economic Climate, and AI Innovation.
- Real-time display of the calculated AI-Q Score.
- Visualizations (bar charts, line charts) to illustrate the breakdown of Idiosyncratic Risk and the dynamics of Systematic Risk.

## Setup and Running the Application

To set up and run the AI-Q Score Visualizer:

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Create a virtual environment (recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit application**:
    ```bash
    streamlit run app.py
    ```

The application will open in your web browser.

## Docker Deployment

You can also run the application using Docker:

1.  **Build the Docker image**:
    ```bash
    docker build -t ai-q-score-visualizer .
    ```

2.  **Run the Docker container**:
    ```bash
    docker run -p 8501:8501 ai-q-score-visualizer
    ```

Access the application in your browser at `http://localhost:8501`.

---
© 2025 QuantUniversity. All Rights Reserved.
The purpose of this demonstration is solely for educational use and illustration. Any reproduction of this demonstration requires prior written consent from QuantUniversity.
