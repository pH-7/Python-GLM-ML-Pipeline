from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import os

data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target)

model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

os.makedirs('../model', exist_ok=True)
joblib.dump(model, '../model/logistic_model.pkl')