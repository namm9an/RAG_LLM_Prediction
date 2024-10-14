# Advanced Stock Prediction with LLM-based RAG and Causal Inference

Welcome to the **Advanced Stock Prediction System** that leverages **Long Short-Term Memory (LSTM)**, **Transformer models**, **Quantum computing**, and **LLM-based Retrieval-Augmented Generation (RAG)**. This project aims to predict Tesla stock prices using historical data from Kaggle and augment the predictions with insights from GPT-3.5-turbo.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [LLM Integration](#llm-integration)
- [CICD Deployment on AWS EC2](#cicd-deployment-on-aws-ec2)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Stock Price Prediction Models**: LSTM, Transformer, and Quantum models for predicting Tesla stock prices.
- **LLM-based RAG Engine**: Augments stock predictions with insights from GPT-3.5-turbo, using relevant historical data.
- **Causal Inference**: Adds explainability by calculating causal effects of predictions.
- **Interactive Dashboard**: A React-based frontend that visualizes predictions, LLM insights, and causal analysis.
- **CI/CD Pipeline**: Automated deployment using AWS EC2.

## Tech Stack

**Backend**:
- Python (FastAPI)
- TensorFlow, PyTorch, PennyLane (for LSTM, Transformer, and Quantum models)
- OpenAI API (for GPT-3.5-turbo integration)
- Scikit-learn, Pandas (data processing and causal inference)

**Frontend**:
- React.js
- Axios (for API requests)
- Chart.js (for data visualization)

## Project Structure
advanced_stock_prediction/ 
├── backend/ 
│ ├── app.py 
│ ├── config.py 
│ ├── data_loader.py 
│ ├── models/ 
│ │ ├── init.py 
│ │ ├── ensemble_model.py 
│ │ ├── lstm_model.py 
│ │ ├── transformer_model.py 
│ │ └── quantum_model.py 
│ ├── utils/ 
│ │ ├── data_integrator.py 
│ │ ├── explainable_ai.py 
│ │ ├── nlp_engine.py 
│ │ ├── stream_processor.py 
│ │ ├── causal_inference_engine.py 
│ │ └── rag_engine.py 
│ └── requirements.txt 
├── frontend/ 
│ ├── public/ 
│ ├── src/ 
│ │ ├── components/ 
│ │ │ ├── Dashboard.js 
│ │ ├── App.js 
│ │ └── index.js 
│ └── package.json 
└── streamlit_app.py



## Dataset

The project uses the [Tesla Inc. (TSLA) dataset](https://www.kaggle.com/datasets/abhimaneukj/tesla-inc-tsla-dataset) available on Kaggle, which contains historical stock prices.

## Setup and Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/advanced_stock_prediction.git
    cd advanced_stock_prediction
    ```

2. **Backend Setup**:

    - Navigate to the `backend` directory.
    - Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. **Frontend Setup**:

    - Navigate to the `frontend` directory.
    - Install the required dependencies:

    ```bash
    npm install
    ```

4. **OpenAI API Key**:
   
    - Sign up for an API key at [OpenAI](https://beta.openai.com/signup/) and update the `your-openai-api-key` placeholder in `rag_engine.py`.

5. **Update Dataset Path**:
   
    - Change the `path_to_tesla_dataset.csv` in `data_loader.py` to the actual path of your downloaded dataset.

## Usage

1. **Run the Backend**:

    ```bash
    uvicorn app:app --reload
    ```

    The API will be available at `http://127.0.0.1:8000`.

2. **Run the Frontend**:

    ```bash
    npm start
    ```

    The React app will be available at `http://localhost:3000`.

## LLM Integration

The project integrates with OpenAI's GPT-3.5-turbo to provide insights on stock predictions. This integration is handled in the `rag_engine.py` file, which retrieves relevant historical stock data to inform the LLM's predictions.

## CICD Deployment on AWS EC2

The project includes a CI/CD pipeline that automates deployment on AWS EC2. For details, please refer to the `deployment` documentation (to be provided separately).

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any feature requests or bugs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
