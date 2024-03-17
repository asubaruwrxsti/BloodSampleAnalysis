import pandas as pd
import logging
from database import Database

# Populate the database with the parameter names
def populateParameters(db: Database, dataset: str, exclude: list = []):
    """
    This function populates the 'parameters' table in the database with parameter names from a dataset.

    Parameters:
    db (Database): The database to populate.
    dataset (str): The path to the dataset file.
    exclude (list, optional): A list of column names to exclude from the dataset. Defaults to an empty list.
    """

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
    
    except pd.errors.ParserError:
        logging.error("Failed to parse the dataset.")
    except Exception as e:
        logging.error(e)

# Populate the database with the disease names
def populateDiseaseNames(db: Database, dataset: str):
    """
    This function populates the 'diseases' table in the database with disease names from a dataset.

    Parameters:
    db (Database): The database to populate.
    dataset (str): The path to the dataset file.
    """

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
    
    except pd.errors.ParserError:
        logging.error("Failed to parse the dataset.")
    except Exception as e:
        logging.error(e)

def populateDatabase(db, DATA_FILE):
    """
    This function populates the database with parameter names and disease names from a dataset.
    """
    populateParameters(db, DATA_FILE, exclude=['Disease'])
    populateDiseaseNames(db, DATA_FILE)