from fastapi import FastAPI, Request
from utils.populateDatabase import populateDatabase
from utils.predictor import trainPredictor
from database import Database
from utils.models import BloodSample

class API:
    def __init__(self, DATA_FILE='Blood_samples_dataset_balanced_2(f).csv'):
        """
        Initialize the API instance.
        
        Parameters:
        DATA_FILE (str): The path to the data file. Default is 'Blood_samples_dataset_balanced_2(f).csv'.
        """
        self.app = FastAPI()
        self.db = Database('db.sqlite3')
        self.data_file = DATA_FILE
        self.predictor = trainPredictor(DATA_FILE)

        populateDatabase(self.db, DATA_FILE)

    def configure(self):
        """
        Configure the API routes.
        """
        @self.app.post("/")
        async def predict(request: Request):
            """
            Predict the disease based on the blood sample data.
            
            Parameters:
            request (Request): The request object containing the blood sample data.
            
            Returns:
            dict: A dictionary containing the predicted disease.
            """
            data = await request.json()
            blood_sample = BloodSample(**data)
            return {"Disease": self.predictor.predict(blood_sample.getData())}

api_instance = API()
api_instance.configure()
app = api_instance.app