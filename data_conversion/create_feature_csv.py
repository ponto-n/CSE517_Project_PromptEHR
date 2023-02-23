'''
Create the feature.csv file to train the PromptEHR model
'''


import pandas as pd
from datetime import datetime
import os
import math

'''
Creating features.csv

SUBJECT_ID : constant across files
AGE : ADMISSIONS.ADMITTIME - PATIENTS.DOB
GENDER : PATIENTS
ETHNICITY : ADMISSIONS
MORTALITY : PATIENTS (EXPIRE_FLAG)
'''

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
DIR = 'C:/Users/noah/mimic-iii'
# DIR = 'C:/Users/noah/cse517_project_code/data_conversion/small_csvs'
PATIENTS_FILE = 'PATIENTS.csv'
ADMISSIONS_FILE = 'ADMISSIONS.csv'
SAVE_FILE = './data_conversion/converted_data/feature.csv'


def main():
    patients_df = pd.read_csv(os.path.join(DIR, PATIENTS_FILE), usecols=[
                              'SUBJECT_ID', 'DOB', 'GENDER', 'DOD_HOSP'])
    admissions_df = pd.read_csv(os.path.join(DIR, ADMISSIONS_FILE), usecols=[
                                'SUBJECT_ID', 'ETHNICITY', 'ADMITTIME'])

    # Only use the first admission to calculate age
    admissions_df = admissions_df.drop_duplicates(subset=['SUBJECT_ID'])

    # Join the dataframes on the SUBJECT_ID column
    joint_df = patients_df.join(
        admissions_df.set_index('SUBJECT_ID'), on='SUBJECT_ID')

    def calculate_age(row):
        '''Uses the DOB and ADMITTIME to calculate the age of the participant'''
        start = datetime.strptime(row.DOB, DATE_FORMAT)
        end = datetime.strptime(row.ADMITTIME, DATE_FORMAT)
        age = (end-start).days/365
        if age > 200:
            # Ages over 89 are obscured by making them 300 years old
            age = 90.19999999999999
        return age

    # Add age column
    joint_df['AGE'] = joint_df.apply(calculate_age, axis=1)

    def convert_mortality(row):
        '''If there's something in the hospital date of death field, then the 
        person died'''
        return type(row.DOD_HOSP) == str

    # Add mortality column
    joint_df['MORTALITY'] = joint_df.apply(convert_mortality, axis=1)

    # Reorganize
    joint_df = joint_df[['SUBJECT_ID', 'AGE', 'GENDER', 'ETHNICITY', 'MORTALITY']]

    # Save the feature.csv file
    joint_df.to_csv(SAVE_FILE)


if __name__ == '__main__':
    main()
