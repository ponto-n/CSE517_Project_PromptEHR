'''
Split the dataset into training, validation, and test subsets.
'''

import dill
import os
import pandas as pd

VALIDATION_PER = 5  # percentage of total data to reserve for validation
TEST_PER = 10  # percentage of all data to reserve for testing

DATA_DIR = os.path.abspath('./data_conversion/converted_data')
SAVE_PATH = '.\\data_conversion\\datasets'

def main():
    # Load the three files
    visits = dill.load(open(os.path.join(DATA_DIR, 'visits.pkl'), 'rb'))
    voc = dill.load(open(os.path.join(DATA_DIR, 'voc.pkl'), 'rb'))
    feature = pd.read_csv(os.path.join(DATA_DIR, 'feature.csv'), index_col=0)

    assert(len(visits) == len(feature)), f'{len(visits)} {len(feature)}'

    # Figure out size of each dataset
    samples_count = len(visits)
    print(f'Found {samples_count} samples.')
    validation_count = round(samples_count * (VALIDATION_PER / 100))
    test_count = round(samples_count * (TEST_PER / 100))
    train_count = samples_count - validation_count - test_count
    print(F'Splitting data:\n Training:\t{train_count:>6}\n Validation:\t{validation_count:>6}\n Test:\t\t{test_count:>6}')

    # Split and save the files
    train_visit = visits[:train_count]
    train_feature = feature.iloc[:train_count]
    save(train_visit, train_feature, voc, 'train')

    val_visit = visits[train_count:train_count+validation_count]
    val_feature = feature.iloc[train_count:train_count+validation_count]
    save(val_visit, val_feature, voc, 'val')

    test_visit = visits[train_count+validation_count:]
    test_feature = feature.iloc[train_count+validation_count:]
    save(test_visit, test_feature, voc, 'test')


def save(visits: list, feature: pd.DataFrame, voc: dict, set_name: str):
    dir = os.path.join(SAVE_PATH, set_name)
    dir = os.path.abspath(dir)

    visit_file = os.path.join(dir, 'visits.pkl')
    dill.dump(obj=visits, file=open(visit_file, "wb"))

    voc_file = os.path.join(dir, 'voc.pkl')
    dill.dump(obj=voc, file=open(voc_file, "wb"))

    feature_file = os.path.join(dir, 'feature.csv')
    feature.to_csv(feature_file)

if __name__ == '__main__':
    main()
