'''
This script is just to check if CUDA Pytorch is set up correctly
'''

import torch

# Using standard torch
print('Using standard torch:')
x = torch.rand(2, 3)
print(x)

print('\nUsing CUDA:')
# Check if cuda is avaliable
if torch.cuda.is_available():
    print("Torch CUDA set up!")

print(f'Found {torch.cuda.device_count()} GPUs')

