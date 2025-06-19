
# AI-Q Score Visualizer

This Streamlit application, "AI-Q Score Visualizer", is designed to help users understand and visualize the AI-Q Score, a metric that quantifies an individual's risk of job displacement due to AI. The application uses a synthetic dataset to demonstrate the calculation of the AI-Q score and the impact of various factors on overall risk. Interactive elements allow users to explore the concepts and see real-time updates.

## Business Logic Explained

The AI-Q Score is a comprehensive metric composed of two main components: **Idiosyncratic Risk** and **Systematic Risk**.

### 1. Idiosyncratic Risk ( $V_i(t)$ )

Idiosyncratic Risk, or Vulnerability, is an individual-specific risk that can be actively managed through personal actions. It is calculated as a composite of three key factors: Human Capital, Company Risk, and Upskilling efforts.

$$
V_i(t) = f(F_{HC}, F_{CR}, F_{US})
$$

#### 1.1 Human Capital Factor ( $F_{HC}$ )

This factor assesses an individual's resilience based on their educational and professional background. A higher human capital factor generally indicates lower idiosyncratic risk.

$$
F_{HC} = f_{role} \cdot f_{level} \cdot f_{field} \cdot f_{school} \cdot f_{exp}
$$

*   **Role Multiplier ($f_{role}$)**: Reflects the inherent AI-vulnerability of one's job role.
*   **Education Level Factor ($f_{level}$)**: Higher education levels often correlate with more specialized skills, potentially reducing vulnerability.
*   **Education Field Factor ($f_{field}$)**: Certain fields (e.g., creative arts, highly specialized research) may be less susceptible to AI automation.
*   **Institution Tier Factor ($f_{school}$)**: The prestige or quality of an educational institution can impact perceived resilience.
*   **Experience Factor ($f_{exp}$)**: More years of experience in a field can indicate deeper expertise and adaptability.

#### 1.2 Company Risk Factor ( $F_{CR}$ )

This factor quantifies the stability and growth prospects of the individual's current employer, particularly regarding their adoption of AI and financial health. A company with higher risk contributes to higher individual idiosyncratic risk.

$$
F_{CR} = w_1 \cdot S_{senti} + w_2 \cdot S_{fin} + w_3 \cdot S_{growth}
$$

*   **Sentiment Score ($S_{senti}$)**: General market sentiment or internal employee sentiment regarding the company's future.
*   **Financial Health Score ($S_{fin}$)**: Reflects the company's financial stability (e.g., revenue growth, profitability).
*   **Growth & AI Adoption Score ($S_{growth}$)**: Assesses how aggressively the company is growing and integrating AI into its operations.
*   **Weights ($w_1, w_2, w_3$)**: Calibration weights for each score.

#### 1.3 Upskilling Factor ( $F_{US}$ )

This factor quantifies an individual's continuous learning and skill development efforts. Engaging in upskilling reduces idiosyncratic risk.

$$
F_{US} = 1 - (\gamma_{gen} \cdot P_{gen}(t) + \gamma_{spec} \cdot P_{spec}(t))
$$

*   **Training progress in general skills ($P_{gen}(t)$)**: Progress in broad, transferable skills (e.g., critical thinking, communication, data literacy).
*   **Training progress in firm-specific skills ($P_{spec}(t)$)**: Progress in skills highly relevant to the current company or industry.
*   **Weighting parameters ($\gamma_{gen}, \gamma_{spec}$)**: Parameters to weigh the importance of general vs. specific skills.

### 2. Systematic Risk ( $H_i$ )

Systematic Risk reflects the broader occupational hazard and macro-economic environment, which is largely outside an individual's direct control.

$$
H_i = H_{base}(t) \cdot (w_{econ} \cdot M_{econ} + w_{inno} \cdot IAI)
$$

*   **Base Occupational Hazard ($H_{base}(t)$)**: The inherent AI-driven risk level of a particular occupation at a given time.
*   **Economic Climate Modifier ($M_{econ}$)**: Reflects the macroeconomic environment's effect on AI investment and adoption.
*   **AI Innovation Index ($IAI$)**: A momentum indicator reflecting the velocity of AI development and adoption.
*   **Calibration weights ($w_{econ}, w_{inno}$)**: Weights for the economic and AI innovation factors.

#### 2.1 Base Occupational Hazard ( $H_{base}(k)$ )

This foundational score of an occupation considers the time it takes to transition to a new industry, reflecting a dynamic risk profile.

$$
H_{base}(k) = (1 - \frac{k}{TTV}) \cdot H_{current} + (\frac{k}{TTV}) \cdot H_{target}
$$

*   **$k$**: Months elapsed since transition pathway completion.
*   **$TTV$**: Total Time-to-Value period (time to transition fully).
*   **$H_{current}$**: Base Occupational Hazard of the original industry.
*   **$H_{target}$**: Base Occupational Hazard of the new target industry.

#### 2.2 Economic Climate Modifier ( $M_{econ}$ )

A composite index reflecting how the overall economic environment impacts AI investment and job displacement.

$$
M_{econ} = f(GDP\ Growth, Sector\ Employment, Interest\ Rates)
$$

Factors include GDP growth, employment trends in relevant sectors, and interest rates, all influencing the pace of AI adoption.

#### 2.3 AI Innovation Index ( $IAI$ )

This index captures the speed of technological change and how rapidly AI is developing and being integrated across industries.

$$
IAI = f(VC\ Funding, R\&D\ Spend, Public\ Salience)
$$

Key components include Venture Capital Funding in AI, Research and Development Spending in AI, and Public awareness/discussion of AI.

---

## Getting Started

### Prerequisites

*   Python 3.8+
*   Docker (optional, for containerized deployment)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd ai-q-score-visualizer
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  **Locally:**
    ```bash
    streamlit run app.py
    ```
    The application will open in your web browser, typically at `http://localhost:8501`.

2.  **Using Docker:**
    1.  **Build the Docker image:**
        ```bash
        docker build -t ai-q-score-visualizer .
        ```
    2.  **Run the Docker container:**
        ```bash
        docker run -p 8501:8501 ai-q-score-visualizer
        ```
    The application will be accessible in your web browser at `http://localhost:8501`.

## Application Structure

*   `app.py`: The main Streamlit application file, handling navigation and overall layout.
*   `requirements.txt`: Lists all Python dependencies.
*   `Dockerfile`: Defines the Docker image for containerized deployment.
*   `README.md`: This file, providing an overview and instructions.
*   `application_pages/`: Directory containing individual page modules for the Streamlit app.
    *   `application_pages/data_generation.py`: Contains functions for synthetic data generation.
    *   `application_pages/calculations.py`: Contains functions for AI-Q Score calculations.
    *   `application_pages/home.py`: The home page explaining concepts.
    *   `application_pages/idiosyncratic_risk.py`: Page for Idiosyncratic Risk visualization and inputs.
    *   `application_pages/systematic_risk.py`: Page for Systematic Risk visualization and inputs.
    *   `application_pages/overall_score.py`: Page to display the combined AI-Q Score and scenario analysis.

## Core Features

*   **Interactive Input Forms**: Adjust parameters for Human Capital, Company Risk, Upskilling, Economic Climate, and AI Innovation.
*   **Real-time AI-Q Score Display**: See the calculated AI-Q Score update instantly.
*   **Visualizations**:
    *   Bar charts/Pie charts for Idiosyncratic Risk factor breakdown.
    *   Line charts for Systematic Risk dynamics.
    *   Scatter plots for correlations between factors.

## License

© 2025 QuantUniversity. All Rights Reserved.

The purpose of this demonstration is solely for educational use and illustration. Any reproduction of this demonstration requires prior written consent from QuantUniversity.
