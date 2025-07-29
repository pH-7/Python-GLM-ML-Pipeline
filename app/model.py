import joblib

model = joblib.load("model/logistic_model.pkl")

def predict(data):
    prediction = model.predict([data])
    return int(prediction[0])