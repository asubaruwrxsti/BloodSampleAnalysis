import pandas as pd
from database import Database

# Populate the database with the parameter names
def populateParameters(db: Database, dataset: str, exclude: list = []):
    try:
        # Load the data
        data = pd.read_csv(dataset)

        # Exclude the columns that are are in the exclude list
        data = data.drop(exclude, axis=1)

        for column in data.columns:
            # Check if the column name already exists in the database
            select_query = "SELECT * FROM parameters WHERE name = ?"
            db.cursor.execute(select_query, (column,))
            result = db.cursor.fetchone()

            # If the column name doesn't exist in the database, insert it
            if result is None:
                insert_query = "INSERT INTO parameters (name) VALUES (?)"
                db.execute_query(insert_query, (column,))
    
    except Exception as e:
        print(e)

# Populate the database with the disease names
def populateDiseaseNames(db: Database, dataset: str):
    try:
        # Load the data
        data = pd.read_csv(dataset)

        for disease in data['Disease'].unique():
            # Check if the disease name already exists in the database
            select_query = "SELECT * FROM diseases WHERE name = ?"
            db.cursor.execute(select_query, (disease,))
            result = db.cursor.fetchone()

            # If the disease name doesn't exist in the database, insert it
            if result is None:
                insert_query = "INSERT INTO diseases (name) VALUES (?)"
                db.execute_query(insert_query, (disease,))
    
    except Exception as e:
        print(e)