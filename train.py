import torch
from pytrial.data.demo_data import load_mimic_ehr_sequence
from pytrial.tasks.trial_simulation.data import SequencePatient
from math import ceil
from promptehr import PromptEHR

'''
Test pytorch
'''
print(f'Using torch version {torch.__version__}')
batch_size = 4
if torch.cuda.is_available():
    gpu_name = torch.cuda.get_device_name()
    device_memory = torch.cuda.get_device_properties(0).total_memory
    device_memory /= 1e9
    print(f'Found GPU: {torch.cuda.get_device_name()}, with {device_memory}GB of memory')
    batch_size = int(device_memory/3)
print(f'Batch size: {batch_size}')

'''
Load the data
'''
N_SAMPLE = 15000
EPOCHS = 50

data_dir = './data_conversion/datasets/train'
demo = load_mimic_ehr_sequence(input_dir=data_dir, n_sample=N_SAMPLE)
seqdata = SequencePatient(data={'v':demo['visit'], 'y':demo['mortality'], 'x':demo['feature'],},
    metadata={
        'visit':{'mode':'dense'},
        'label':{'mode':'tensor'}, 
        'voc':demo['voc'],
        'max_visit':20,
        }
    )


'''
Create the model
'''

# Set eval step to be greater than the total required steps to avoid evaluating
number_samples = len(seqdata.visit)
total_steps = ceil(number_samples / batch_size) * EPOCHS
eval_step = total_steps + 1

# Create the model
model = PromptEHR(
    code_type=demo['order'],
    n_num_feature=demo['n_num_feature'],
    cat_cardinalities=demo['cat_cardinalities'],
    num_worker=0,
    eval_step=eval_step,
    epoch=EPOCHS,
    batch_size=batch_size,
    # device=[1,2],
    output_dir='./promptEHR_logs'
)

'''
Train the model
'''
try:
    model.fit(
        train_data=seqdata
        # val_data=seqdata,
    )
except Exception as e:
    print('CAUGHT EXCEPTION:')
    print(e)
finally:
    print('Saving the model...')
    model.save_model('./model')
    print('Done!')