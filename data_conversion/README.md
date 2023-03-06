# Data Conversion
This folder has the logic to convert the MIMIC-III dataset CSV files into
the three files required for training the PromptEHR model:
```
feature.csv
visitis.pkl
voc.pkl
```

---

## Steps to create required files

1. Download the MIMIC-III dataset. The only required files are:
    * PRESCRIPTIONS
    * DIAGNOSES_ICD
    * PROCEDURES_ICD
    * PATIENTS
    * ADMISSIONS

2. Download the input files for the SaveDrug processing file. The instructions for this are in the README in the `safedrug_input` directory.

3. Run the `processing.py` script. This will create 4 files in the `converted_data` folder:
    * atc3toSMILES.pkl : drug ID to drug SMILES string dict (only important for SafeDrug processing)
    * visits.pkl : a list of visit events (one entry for each participant)
    * voc.pkl
    * unique_patients.pkl

4. Run the `create_feature_csv.py` script. This will create the feature.csv file.

5. To split into train, validation, and test sets, run `split_datasets.py`, which should have an output like:
```
Found 35419 samples.
Splitting data:
 Training:       30106
 Validation:      1771
 Test:            3542
 ```