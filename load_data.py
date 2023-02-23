'''
The example file from here:
https://github.com/RyanWangZf/PromptEHR/blob/main/example/demo_promptehr.ipynb
'''

import os
os.chdir('../')

# load pytrial demodata, supported by PyTrial package to load the demo EHR data
from pytrial.data.demo_data import load_mimic_ehr_sequence
from pytrial.tasks.trial_simulation.data import SequencePatient

# see the input format
demo = load_mimic_ehr_sequence(n_sample=100, input_dir='C:/Users/noah/PyTrial/demo_data/demo_patient_sequence/ehr')

# build sequence dataset
seqdata = SequencePatient(data={'v':demo['visit'], 'y':demo['mortality'], 'x':demo['feature'],},
    metadata={
        'visit':{'mode':'dense'},
        'label':{'mode':'tensor'}, 
        'voc':demo['voc'],
        'max_visit':20,
        }
    )

print('visit', demo['visit'][0]) # a list of visit events
print('mortality', demo['mortality'][0]) # array of labels
print('feature', demo['feature'][0]) # array of patient baseline features
print('voc', demo['voc']) # dict of dicts containing the mapping from index to the original event names
print('order', demo['order']) # a list of three types of code
print('n_num_feature', demo['n_num_feature']) # int: a number of patient's numerical features
print('cat_cardinalities', demo['cat_cardinalities']) # list: a list of cardinalities of patient's categorical features