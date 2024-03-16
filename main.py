from database import Database
from utils.populateDatabase import populateParameters, populateDiseaseNames

# Create a database object
db = Database('db.sqlite3')

if __name__ == "__main__":
    # Populate the database with the data from the dataset
    populateParameters(db, 'Blood_samples_dataset_balanced_2(f).csv', exclude=['Disease'])

    # Populate the database with the disease names
    populateDiseaseNames(db, 'Blood_samples_dataset_balanced_2(f).csv')