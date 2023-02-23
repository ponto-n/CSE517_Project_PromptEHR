'''
Create copies of the csv files with only the sample uids

The smaller csv files are easier to experiment with and take less time to load.
'''
import pandas as pd
import os

NUM_SAMPLES = 100

SAMPLE_FEATURE_FILE = 'C:/Users/noah/PyTrial/demo_data/demo_patient_sequence/ehr/feature.csv'
MIMIC_DIR = 'C:/Users/noah/mimic-iii'

# Find set of SUBJECT_IDs to use
num_feature_lines = sum(1 for line in open(SAMPLE_FEATURE_FILE))-1
# print(f'Number lines: {num_feature_lines}')

sample_df = pd.read_csv(SAMPLE_FEATURE_FILE, skiprows=range(
    NUM_SAMPLES, num_feature_lines))

sids_list = sample_df['SUBJECT_ID'].values.tolist()
sids_list = sorted(sids_list)
sids_set = set(sids_list)
assert (len(sids_list) == len(sids_set))
assert (len(sids_set) == NUM_SAMPLES)


def get_relevant_rows(mimic_file: str, sids: set):
    print(mimic_file)
    save_path = os.path.join('./data_conversion/small_csvs', mimic_file)
    if os.path.exists(save_path):
        print('\talready created file')
        return
    full_path = os.path.join(MIMIC_DIR, mimic_file)
    assert (os.path.exists(full_path)), full_path
    full_length = sum(1 for line in open(full_path))-1
    print(f'\ttotal rows {full_length}')

    # Get indexes where participant ID matches the subset
    print('\tgetting subject ID indexes...')
    sid_df = pd.read_csv(full_path, usecols=['SUBJECT_ID'])
    if 'SUBJECT_ID' not in sid_df:
        return
    match_indexes = sid_df[sid_df['SUBJECT_ID'].isin(sids)].index.tolist()
    # print(match_indexes)
    match_indexes = set(match_indexes)
    print(f'\trelevant rows: {len(match_indexes)}')

    # Only load indexes for matching participant IDs
    print(f'\tloading relevant rows...')
    exclude = [i+1 for i in range(full_length) if i not in match_indexes]
    small_df = pd.read_csv(full_path, skiprows=exclude)
    small_df = small_df.sort_values(by=['SUBJECT_ID'])
    print(f'\tsaving smaller file...')
    small_df.to_csv(save_path, index=False)


# get_relevant_rows('PATIENTS.csv', sids_set)
FILES_WITH_SID = ['ADMISSIONS.csv', 'CALLOUT.csv', 'CHARTEVENTS.csv', 'CPTEVENTS.csv', 'DATETIMEEVENTS.csv', 'DIAGNOSES_ICD.csv', 'DRGCODES.csv', 'ICUSTAYS.csv', 'INPUTEVENTS_CV.csv', 'INPUTEVENTS_MV.csv',
                  'LABEVENTS.csv', 'MICROBIOLOGYEVENTS.csv', 'NOTEEVENTS.csv', 'OUTPUTEVENTS.csv', 'PATIENTS.csv', 'PRESCRIPTIONS.csv', 'PROCEDUREEVENTS_MV.csv', 'PROCEDURES_ICD.csv', 'SERVICES.csv', 'TRANSFERS.csv']
for file in FILES_WITH_SID:
    get_relevant_rows(file, sids_set)
