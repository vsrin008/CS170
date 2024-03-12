from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load Iris dataset
iris = load_iris()
X = iris.data  
y = iris.target  

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=11)

# Normalize
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize and train logistic regression model
logistic_model = LogisticRegression(random_state=11)
logistic_model.fit(X_train_scaled, y_train)

# predict and evaluate logistic regression model
y_pred_logistic = logistic_model.predict(X_test_scaled)
accuracy_logistic = accuracy_score(y_test, y_pred_logistic)

# Initialize and train linear SVM model
svm_model = SVC(kernel='linear', random_state=11)
svm_model.fit(X_train_scaled, y_train)

# Predict and evaluate linear SVM model
y_pred_svm = svm_model.predict(X_test_scaled)
accuracy_svm = accuracy_score(y_test, y_pred_svm)

# Print accuracies
print(f"Logistic Regression Accuracy: {accuracy_logistic}")
print(f"Linear SVM Accuracy: {accuracy_svm}")

# Print weights and biases
print("Logistic Regression Weights and Biases:")
print("Weights:", logistic_model.coef_)
print("Biases:", logistic_model.intercept_)

print("Linear SVM Weights and Biases:")
print("Weights:", svm_model.coef_)
print("Biases:", svm_model.intercept_)
