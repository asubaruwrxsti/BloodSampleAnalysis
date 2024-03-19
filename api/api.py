from fastapi import FastAPI, Request, HTTPException, Depends
from pydantic import ValidationError
from utils.populateDatabase import populateDatabase
from utils.predictor import trainPredictor
from utils.models import BloodSample
from database import Database

class API:
    def __init__(self, app: FastAPI, db: Database, predictor):
        self.app = app
        self.db = db
        self.predictor = predictor

    def configure(self):
        @self.app.post("/")
        async def predict(request: Request):
            try:
                data = await request.json()
                blood_sample = BloodSample(**data)
                return {"Disease": self.predictor.predict(blood_sample.getData())}
            except ValidationError as e:
                raise HTTPException(status_code=400, detail=e.json())

def create_api(db: Database, predictor, data_file='Blood_samples_dataset_balanced_2(f).csv'):
    app = FastAPI()
    populateDatabase(db, data_file)
    api = API(app, db, predictor)
    api.configure()
    return app

db = Database('db.sqlite3')
predictor = trainPredictor('Blood_samples_dataset_balanced_2(f).csv')
app = create_api(db, predictor)