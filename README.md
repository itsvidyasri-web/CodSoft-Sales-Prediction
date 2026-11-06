# Sales Prediction Using Machine Learning

A Machine Learning-based Sales Prediction application that estimates product sales based on advertising expenditure across TV, Radio, and Newspaper platforms.

**Live Demo:** https://codsoft-sales-prediction-eqwpqpdewmaxgqjkxtawdk.streamlit.app/

## Project Overview

This project uses Linear Regression, a supervised machine learning algorithm, to understand the relationship between advertising expenditure and sales.

Users can interact with the dashboard by adjusting advertising budgets and generating sales predictions instantly.

The application is built using Python and Streamlit, providing a simple and interactive interface for exploring sales predictions.

## Objectives

- Analyze advertising expenditure data.
- Understand the relationship between advertising channels and sales.
- Build a Linear Regression prediction model.
- Create an interactive web dashboard.
- Demonstrate how machine learning can support advertising and sales analysis.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Pickle
- Matplotlib / Streamlit Charts

## Dataset

**Dataset:** Advertising Dataset

**Source:** [Kaggle – Advertising Dataset](https://www.kaggle.com/datasets/bumba5341/advertisingcsv)

The dataset contains advertising expenditure and corresponding sales information.

### Dataset Features

| Feature | Description |
|---|---|
| TV | Advertising expenditure on TV |
| Radio | Advertising expenditure on Radio |
| Newspaper | Advertising expenditure on Newspaper |
| Sales | Target variable used for prediction |

## Machine Learning Algorithm

**Linear Regression**

Linear Regression is used to learn the relationship between the advertising expenditure features and sales.

### Model Development Process

1. Load the dataset using Pandas.
2. Perform basic data exploration.
3. Check for missing values.
4. Separate input features and target variable.
5. Split the dataset into training and testing sets.
6. Train the Linear Regression model.
7. Evaluate model performance.
8. Save the trained model using Pickle.

## Dashboard Features

- Interactive advertising budget sliders.
- TV, Radio, and Newspaper expenditure inputs.
- Automatic total advertising budget calculation.
- Sales prediction with one click.
- Predicted sales displayed using a metric card.
- Advertising budget breakdown bar chart.
- User-friendly Streamlit dashboard.

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

The application will open in your browser.

## How to Use

1. Open the Sales Prediction Dashboard.
2. Adjust TV, Radio, and Newspaper advertising budgets.
3. Review the total advertising budget.
4. Click the **Predict Sales** button.
5. View the predicted sales result.
6. Analyze the advertising budget breakdown chart.

## Project Outcome

This project demonstrates the practical implementation of a supervised machine learning algorithm and its integration into an interactive web application.

It provides a simple way to explore how different advertising budgets relate to predicted sales.

## Internship Information

**Organization:** CodSoft  
**Domain:** Data Science  
**Project:** Sales Prediction Using Python

## Author

Developed as part of the CodSoft Data Science Internship.

---

**Note:** Predictions are model-based estimates using the supplied dataset. They are not guaranteed actual sales results.
