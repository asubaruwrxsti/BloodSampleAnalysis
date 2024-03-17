import logging
from typing import List
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.INFO)

class DiseasePredictor:
    def __init__(self, random_state=42):
        """
        Constructor for the DiseasePredictor class. Initializes the decision tree classifier.

        Parameters:
        random_state (int): The seed used by the random number generator. Defaults to 42.
        """
        self.clf = DecisionTreeClassifier(random_state=random_state)

    def load_data(self, dataset: str, exclude: List[str] = []):
        """
        Loads and prepares the data from a CSV file.

        Parameters:
        dataset (str): The path to the dataset file.
        exclude (List[str]): A list of column names to exclude from the dataset. Defaults to an empty list.
        """
        try:
            data = pd.read_csv(dataset)
        except FileNotFoundError:
            logging.error(f"File {dataset} not found.")
            return

        if 'Disease' not in data.columns:
            logging.error("No 'Disease' column in data.")
            return

        data = data.drop(exclude, axis=1)
        self.labels = data['Disease'].astype('category').cat.codes
        self.disease_mapping = dict(enumerate(data['Disease'].astype('category').cat.categories))
        self.data = data.drop('Disease', axis=1)

    def split_data(self, test_size=0.2):
        """
        Splits the data into training and test sets.

        Parameters:
        test_size (float): The proportion of the dataset to include in the test split. Defaults to 0.2.
        """
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.data, self.labels, test_size=test_size, random_state=42)

    def train(self):
        """
        Trains the decision tree classifier. The data must be loaded and split before training.
        """
        if self.X_train is None or self.y_train is None:
            logging.error("Data not loaded or split yet.")
            return

        self.clf.fit(self.X_train, self.y_train)

    def predict(self, sample: np.ndarray) -> str:
        """
        Predicts the disease from a sample.

        Parameters:
        sample (np.ndarray): The sample to predict the disease from.

        Returns:
        str: The predicted disease.
        """
        if isinstance(sample, np.ndarray):
            sample = pd.DataFrame(sample, columns=self.X_train.columns)

        if sample.shape[1] != self.X_train.shape[1]:
            raise ValueError(f"Number of features in the sample ({sample.shape[1]}) does not match the number of features in the training data ({self.X_train.shape[1]}).")

        prediction = self.clf.predict(sample)
        return self.disease_mapping[prediction[0]]