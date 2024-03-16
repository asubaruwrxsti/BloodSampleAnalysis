import pandas as pd
from database import Database

# Insert the data into the database
def populateDatabase(db: Database, dataset: str, exclude: list = []):
    try:
        # Load the data
        data = pd.read_csv(dataset)

        # Exclude the columns that are are in the exclude list
        data = data.drop(exclude, axis=1)

        for column in data.columns:
            # Check if the column name already exists in the database
            select_query = "SELECT * FROM diseases WHERE name = ?"
            db.cursor.execute(select_query, (column,))
            result = db.cursor.fetchone()

            # If the column name doesn't exist in the database, insert it
            if result is None:
                insert_query = "INSERT INTO diseases (name) VALUES (?)"
                db.execute_query(insert_query, (column,))
    
    except Exception as e:
        print(e)