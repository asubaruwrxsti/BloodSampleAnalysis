from database import Database
from utils.populateDatabase import populateDatabase
from utils.predictor import trainPredictor
from utils.models import BloodSample

DATA_FILE = 'Blood_samples_dataset_balanced_2(f).csv'

def main():
    db = Database('db.sqlite3')

    try:
        populateDatabase(db, DATA_FILE)
        predictor = trainPredictor(DATA_FILE)
        sample = getSampleData()
        print(f'The predicted disease is: {predictor.predict(sample)}')
    except Exception as e:
        print(f"An error occurred: {e}")

def getSampleData():
    """
    Sample data, output Thalasse
    """
    return BloodSample(
        glucose=0.1767371924855356,
        cholesterol=0.7522199398931788,
        hemoglobin=0.9717793888731444,
        platelets=0.7852855880607905,
        white_blood_cells=0.4438801892086707,
        red_blood_cells=0.4398513703765432,
        hematocrit=0.8949911870557408,
        mean_corpuscular_volume=0.4421588012526802,
        mean_corpuscular_hemoglobin=0.2572878875579603,
        mean_corpuscular_hemoglobin_concentration=0.8059874751265301,
        insulin=0.1843709356974067,
        bmi=0.5801750125376235,
        systolic_blood_pressure=0.1184610097615879,
        diastolic_blood_pressure=0.0055786481969444,
        triglycerides=0.414406910169573,
        hba1c=0.4294312681249561,
        ldl_cholesterol=0.1462935401342766,
        hdl_cholesterol=0.2215735887189036,
        alt=0.015280079207102,
        ast=0.5671149256550005,
        heart_rate=0.8414118221171962,
        creatinine=0.1533498509469442,
        troponin=0.7940080387209453,
        c_reactive_protein=0.0949703212172067
    ).getData()

if __name__ == "__main__":
    main()