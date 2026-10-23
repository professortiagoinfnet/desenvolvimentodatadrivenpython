from fastapi import FastAPI
from routers.prediction_routers import router
app = FastAPI()
app.include_router(router)