# Customer Churn Prediction

## Project Overview

Customer Churn Prediction is a machine learning project that predicts whether a customer is likely to leave a company based on demographic and service-related information.

The project aims to help businesses identify customers at risk of churning and take proactive steps to improve customer retention.

## Problem Statement

Customer churn is a major challenge for businesses, as losing customers can negatively impact revenue and growth. This project uses machine learning techniques to predict customer churn and support better customer retention strategies.

## Dataset

- **Source:** Kaggle
- **Records:** 1,000 rows
- **Features:** 10 columns
- **Target Variable:** Churn

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit

## Project Workflow

1. **Data Loading:** Imported the dataset using Pandas.
2. **Data Cleaning:** Checked for missing values and duplicate records. Handled missing entries in the Internet Service column.
3. **Exploratory Data Analysis:** Analyzed numerical features and explored relationships using correlation and data visualizations.
4. **Feature Encoding:** Applied binary encoding to the Gender and Churn columns.
5. **Feature Scaling:** Used StandardScaler to standardize numerical features.
6. **Model Training:** Trained and evaluated multiple machine learning algorithms.
7. **Model Selection:** Compared model accuracy and selected SVM based on the highest reported accuracy.

## Model Performance

The following accuracy scores were obtained during model evaluation:

| Machine Learning Model | Accuracy |
|---|---:|
| Logistic Regression | 85% |
| K-Nearest Neighbors | 84% |
| Support Vector Machine (SVM) | **87%** |
| Decision Tree Classifier | 85% |
| Random Forest Classifier | 83% |

**Best Performing Model:** Support Vector Machine (SVM) with 87% accuracy.

## Model Deployment

The trained model and scaler were saved as `.pkl` files using model persistence.

A web application was developed using Streamlit, allowing users to enter customer information and receive churn predictions.

The application is deployed on Render.

## Project Structure

```text
customer-churn-prediction/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── customer_churn_data.csv
├── notebook.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/shashank-43/customer-churn-prediction.git
```

2. Navigate to the project directory:

```bash
cd customer-churn-prediction
```

3. Install the required libraries:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit application:

```bash
streamlit run app.py
```

## Project Links

- **GitHub Repository:** https://github.com/shashank-43/customer-churn-prediction
- **Live Application:** Add your Render deployment URL here.
