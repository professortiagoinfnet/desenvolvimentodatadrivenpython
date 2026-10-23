from fastapi import APIRouter
from models.prediction_models import PredictionRequest, PredictionResponse, Prediction
from services.prediction_services import Predictor

router = APIRouter()

predictions = []

@router.post("/predict", response_model=PredictionResponse)
async def predict(predictionRequest : PredictionRequest):
    predictor = Predictor(predictionRequest.prompt)
    predictor.run()
    prediction = Prediction(id=len(predictions) + 1, prompt=predictor.prompt, response=predictor.response)
    predictions.append(prediction)
    predictionResponse = PredictionResponse(prompt=predictor.prompt, response=predictor.response)
    return predictionResponse

@router.get("/predictions", response_model=list[PredictionResponse])
async def retreive_predictions():
    return predictions
