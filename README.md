# Sales Prediction Using Machine Learning

### CodSoft Data Science Internship Project

**Live Demo:** https://codsoft-sales-prediction-eqwpqpdewmaxgqjkxtawdk.streamlit.app/

## Project Overview

Sales Prediction Using Machine Learning is a data science project that predicts product sales based on advertising expenditure across TV, Radio, and Newspaper platforms.

This project uses a Linear Regression algorithm to analyse advertising data and estimate sales based on user-provided advertising budgets.

An interactive web application is developed using Streamlit, allowing users to enter advertising expenses and receive instant sales predictions.

## Project Objectives

- Analyse advertising expenditure data.
- Understand the relationship between advertising and sales.
- Perform data preprocessing and exploration.
- Build a Machine Learning prediction model.
- Evaluate model performance using standard metrics.
- Develop an interactive web application for sales prediction.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Pickle
- GitHub

## Dataset Description

The project uses the Advertising dataset (`Advertising.csv`).

The dataset contains the following features:

| Feature | Description |
|---|---|
| TV | TV advertising expenditure |
| Radio | Radio advertising expenditure |
| Newspaper | Newspaper advertising expenditure |
| Sales | Actual sales values |

## Machine Learning Algorithm

**Linear Regression**

Linear Regression is used to understand the relationship between advertising expenditure and sales.

### Model Development

1. Load the advertising dataset.
2. Perform exploratory data analysis.
3. Check for missing values.
4. Separate input features and target variable.
5. Split the dataset into training and testing sets.
6. Train the Linear Regression model.
7. Evaluate model performance.
8. Save the trained model using Pickle.

### Model Evaluation Metrics

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

## Application Features

- Simple and interactive user interface.
- TV advertising expenditure input.
- Radio advertising expenditure input.
- Newspaper advertising expenditure input.
- Instant sales prediction.
- User-friendly prediction results.

## Project Structure

```text
CodSoft-Sales-Prediction/
│
├── Advertising.csv
├── main.py
├── app.py
├── sales_model.pkl
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd CodSoft-Sales-Prediction
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m streamlit run app.py
```

### 5. Open the Application

Open the local URL displayed in your terminal.

## Live Application

Try the deployed application here:

**[Sales Prediction – Live Demo](https://codsoft-sales-prediction-eqwpqpdewmaxgqjkxtawdk.streamlit.app/)**

## Project Outcome

Successfully developed an interactive Machine Learning application that predicts estimated sales based on advertising expenditure using Linear Regression.

This project provided practical experience in Python programming, data analysis, Machine Learning, model evaluation, and web application deployment.

## Internship Details

**Organization:** CodSoft  
**Domain:** Data Science  
**Project:** Sales Prediction Using Machine Learning

## Conclusion

This project demonstrates how Machine Learning can be applied to analyse advertising data and estimate sales. It also provides practical experience in developing and deploying a complete data science application.

---

**Developed as part of the CodSoft Data Science Internship.**
