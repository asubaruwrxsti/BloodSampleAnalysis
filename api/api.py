from fastapi import FastAPI, Request, HTTPException, Depends
from pydantic import ValidationError
from utils.populateDatabase import populateDatabase
from utils.predictor import trainPredictor
from utils.models import BloodSample
from database import Database

class API:
    def __init__(self, app: FastAPI, db: Database, predictor):
        """
        Initialize the API class with FastAPI instance, Database instance, and a predictor.
        """
        self.app = app
        self.db = db
        self.predictor = predictor

    def configure(self):
        """
        Configure the FastAPI instance with a POST endpoint at "/".
        This endpoint expects a JSON request body and returns a prediction.
        """
        @self.app.post("/")
        async def predict(request: Request):
            try:
                # Parse the request body to a BloodSample instance
                data = await request.json()
                blood_sample = BloodSample(**data)
                
                # Return the prediction result
                return {"Disease": self.predictor.predict(blood_sample.getData())}
            except ValidationError as e:
                # If the request body cannot be parsed to a BloodSample instance, return a 400 error
                raise HTTPException(status_code=400, detail=e.json())

def create_api(db: Database, predictor, data_file='Blood_samples_dataset_balanced_2(f).csv'):
    """
    Create a FastAPI instance, populate the database, and configure the API.
    """
    app = FastAPI()
    populateDatabase(db, data_file)
    api = API(app, db, predictor)
    api.configure()
    return app

# Create a Database instance
db = Database('db.sqlite3')

# Train the predictor
predictor = trainPredictor('Blood_samples_dataset_balanced_2(f).csv')

# Create and configure the FastAPI instance
app = create_api(db, predictor)