from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train a Logistic Regression model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Define a function for making predictions
def predict(input_data):
    input_data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_data)
    return iris.target_names[prediction][0]

# Example usage
sample_input = [5.1, 3.5, 1.4, 0.2]  # Example Iris flower measurements
prediction = predict(sample_input)
print(f"Predicted class: {prediction}")
