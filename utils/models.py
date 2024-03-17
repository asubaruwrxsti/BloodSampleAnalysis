import numpy as np

class BloodSample:
    def __init__(self, **kwargs):
        """
        This is the constructor for the BloodSample class. It initializes a new instance of the class.

        Parameters:
        kwargs (dict): A dictionary containing the data for the blood sample.
        """
        self.data = kwargs

    def getData(self):
        """
        This function returns the data of the blood sample as a numpy array.

        Returns:
        np.array: The data of the blood sample.
        """
        return np.array(list(self.data.values())).reshape(1, -1)