import os
import logging
import joblib
from mla.decisionTree import DiseasePredictor

def trainPredictor(DATA_FILE, predictor_type=DiseasePredictor, model_file='trained_model.pkl'):
    """
    This function trains a DiseasePredictor model and saves it to a file. 
    If a trained model already exists in the specified file, it loads the model from the file instead of training a new one.

    Parameters:
    DATA_FILE (str): The path to the data file.
    predictor_type (class, optional): The type of predictor to train. Defaults to DiseasePredictor.
    model_file (str, optional): The path to the file where the trained model should be saved. Defaults to 'trained_model.pkl'.

    Returns:
    predictor (DiseasePredictor): The trained DiseasePredictor model.
    """
    # If a trained model already exists, load it instead of training a new one
    if os.path.exists(model_file):
        try:
            predictor = joblib.load(model_file)
            logging.info(f"Loaded existing model from {model_file}.")
            return predictor
        except Exception as e:
            logging.error(f"Failed to load model from {model_file}: {e}")
            return None

    try:
        predictor = predictor_type()
        predictor.load_data(DATA_FILE)
    except Exception as e:
        logging.error(f"Failed to load data from {DATA_FILE}: {e}")
        return None

    try:
        predictor.train()
    except Exception as e:
        logging.error(f"Failed to train predictor: {e}")
        return None

    # Save the trained model
    try:
        joblib.dump(predictor, model_file)
        logging.info(f"Successfully trained and saved predictor to {model_file}.")
    except Exception as e:
        logging.error(f"Failed to save model: {e}")
        return None

    return predictor