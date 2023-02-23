'''
Print columns of the MIMIC files and print out useful information about 
what is contained in each file.
'''
import os
import csv

os.system('cls')
print('\n\n')
MIMIC_DIR = 'C:/Users/noah/mimic-iii'

processed_feature_cols = set(['AGE', 'GENDER', 'ETHNICITY', 'MORTALITY'])

csv_files = []
for file in os.listdir(MIMIC_DIR):
    if file[-4:] == '.csv':
        csv_files.append(file)

print(f'{len(csv_files)} files: {csv_files}')

# Show columns of each file
have_subject_id = []
cols_to_files = {}
files_with_dates = {

}
for file in csv_files:
    full_path = os.path.join(MIMIC_DIR, file)
    # if file != 'CHARTEVENTS.csv': continue
    with open(full_path, 'r', newline='') as f:
        reader = csv.reader(f, delimiter='\n')
        headings = next(reader)[0].split(',')
        headings = [x.replace('\"', '') for x in headings]
        # output = []
        # for row in reader:
        #     output.append(row[:])
        headings_set = set(headings)
        if 'SUBJECT_ID' not in headings_set:
            # print('\tMISSING SUBJECT_ID')
            continue
        else:
            have_subject_id.append(file)
        print(f'File: {file} has {len(headings)} headings: \n\t{headings}')
        intersection = headings_set.intersection(processed_feature_cols)
        if len(intersection) > 0:
            for col in intersection:
                if col not in cols_to_files:
                    cols_to_files[col] = []
                cols_to_files[col].append(file)
            print(f'\tFOUND: {intersection}')

        # Find things that might be dates
        # if file in ['CHARTEVENTS.csv']: 
        #     continue
        # example_elements = [None] * len(headings)
        # max_rows = 50
        # while any([x==None for x in example_elements]) and max_rows:
        #     line = next(reader)
        #     line = [0].split(',')
        #     for i in [x for x, e in enumerate(example_elements) if e is None]:
        #         ele = line[i]
        #         if len(ele) > 0:
        #             example_elements[i] = ele
        #     max_rows -= 1
        #     if max_rows <= 0:
        #         break

        # for i, ele in enumerate(example_elements):
        #     if ele is not None and len(ele) > 9 and ele[4] == '-' and ele[7] == '-':
        #         col = headings[i]
        #         if file not in files_with_dates:
        #             files_with_dates[file] = []
        #         files_with_dates[file].append(col)
        # print(first_line)

print(f'\nFiles with SUBJECT_ID:\n{have_subject_id}')

print('\nFiles with cols:')
for col in cols_to_files:
    print(f'{col}: {cols_to_files[col]}')

found_cols = set(cols_to_files.keys())
print(f'\nColumns not found: {processed_feature_cols.difference(found_cols)}')

'''
14,17,"F",2087-07-14 -> 47.84931506849315 -> 2135
18,21,"M",2047-04-04 -> 87.4958904109589 -> 2134
20,23,"M",2082-07-17 -> 75.30410958904109 -> 2157
34 1886-07-18 -> +90.19999999999999 -> 1976
2131 - 2061 -> 
'''

print(f'\nFiles with dates:')
for file in files_with_dates:
    print(f'{file}: {files_with_dates[file]}')

        