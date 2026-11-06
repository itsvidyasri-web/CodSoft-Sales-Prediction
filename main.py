import pandas as pd

# Load the dataset
data = pd.read_csv("Advertising.csv")

# Display first 5 rows
print(data.head())

# Check dataset rows and columns
print("Dataset Shape:", data.shape)

# Get dataset information
print(data.info())

# Get statistical details
print(data.describe())
# Check missing values
print("Missing Values:")
print(data.isnull().sum())

# Separate input and output

X = data[['TV', 'Radio', 'Newspaper']]

y = data['Sales']

print("Input Data:")
print(X.head())

print("Output Data:")
print(y.head())

from sklearn.model_selection import train_test_split

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)

from sklearn.linear_model import LinearRegression

# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

print("Model trained successfully!")

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Predict sales
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("R2 Score:", r2)

# Predict sales for new advertising expenses

new_data = [[200, 40, 30]]

predicted_sales = model.predict(new_data)

print("Predicted Sales:", predicted_sales[0])

import pickle

# Save the trained model
with open("sales_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")