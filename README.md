# Bank Loan Approval Classification - End-to-End Project

Welcome to the **Bank Loan Approval Classification** project! This project is designed to build a machine learning system that predicts loan approval decisions based on applicant information. The project is implemented in Python and includes a well-structured codebase for training, testing, and deploying the model in a web application.

---

## Table of Contents
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Project Walkthrough](#project-walkthrough)
- [Web Application](#web-application)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Credits](#credits)

---

## Project Structure

This project is organized into several directories and files, as follows:

```plaintext
├── artifacts                # Stores models and datasets
│   ├── model.pkl            # Saved trained model
│   ├── train_data.csv       # Training data file
│   ├── test_data.csv        # Testing data file
│   └── loan_data.csv        # Raw loan data file
├── notebooks                # Jupyter notebooks for analysis and model training
│   ├── EDA.ipynb            # Exploratory Data Analysis
│   └── Model_Training.ipynb # Model training and evaluation
├── src                      # Source code for the project
│   ├── components           # Modules for data ingestion, transformation, and training
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline             # Code for training and prediction pipelines
│   │   ├── __init__.py
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   ├── __init__.py
│   ├── logger.py            # Custom logging module
│   ├── exception.py         # Custom exception handling module
│   └── utils.py             # Utility functions
├── templates                # HTML templates for web application
│   ├── home.html
│   └── index.html
├── app.py                   # Flask application for deploying the model
├── setup.py                 # Setup configuration for the project
├── requirements.txt         # Required packages and dependencies
└── README.md                # Project documentation
```

---

## Setup and Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd Bank-Loan-Approval-Classification
    ```

2. **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## Project Walkthrough

### 1. **Data Preparation**

   - **Data Ingestion**: `data_ingestion.py` is responsible for loading and splitting data into training and testing sets.
   - **Data Transformation**: `data_transformation.py` includes preprocessing steps, such as handling missing values, encoding categorical variables, and scaling.
   - **Artifacts Folder**: Holds `train_data.csv`, `test_data.csv`, and `loan_data.csv` files, along with the final trained model `model.pkl`.

### 2. **Model Training**

   - The **Model Training** notebook contains code for building, training, and evaluating a model to classify loan approval.
   - `model_trainer.py` includes code to handle the training logic and model saving.

### 3. **Pipeline**

   - **Training Pipeline** (`train_pipeline.py`): End-to-end execution of data ingestion, transformation, and training.
   - **Prediction Pipeline** (`predict_pipeline.py`): Loads the trained model and makes predictions for new applicants.

### 4. **Logging and Exception Handling**

   - `logger.py`: Custom logger to track events, errors, and information during pipeline execution.
   - `exception.py`: Custom exception classes to handle errors gracefully and log helpful error messages.

### 5. **Web Application**

   - **Flask Application** (`app.py`): The Flask app serves as a frontend for users to input loan applicant details and receive an approval prediction.
   - **Templates**: 
      - `home.html`: Main landing page.
      - `index.html`: Interface for inputting applicant details and displaying prediction results.

---

## Web Application

The project includes a simple Flask web application for loan prediction. After setting up the application, navigate to `http://127.0.0.1:5000/` to access the app:

1. **Run the Flask app:**
    ```bash
    python app.py
    ```

2. **Access the app**:
   Open your web browser and go to `http://127.0.0.1:5000/`.

---

## Requirements

- **Data Handling**: `pandas`, `numpy`
- **Visualization**: `matplotlib`, `seaborn`
- **Machine Learning**: `scikit-learn`
- **Web Application**: `Flask`
- **Serialization**: `dill`, `pickle`
- **Project Structure**: `setup.py`, `-e .` (editable installation)

Install all requirements using:

```bash
pip install -r requirements.txt
```

---

## Getting Started

1. Perform **EDA** to understand data patterns and insights.
2. Train and evaluate the model on the prepared dataset.
3. Run the **training pipeline** and save the model in `artifacts/model.pkl`.
4. Use the **Flask web application** for model deployment and predictions.

---

## Credits

This project was developed to demonstrate an end-to-end machine learning pipeline for classifying loan approval status based on applicant data.
