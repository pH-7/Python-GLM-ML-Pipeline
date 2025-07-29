from fastapi import FastAPI
from app.schemas import PredictionInput
from app.model import predict

app = FastAPI()

@app.post("/predict")
def get_prediction(input: PredictionInput):
    result = predict(input.data)
    return {"prediction": result}