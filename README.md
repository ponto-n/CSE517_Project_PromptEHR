# CSE517 Course Project: PromptEHR 

# Installation

To seperate the packages for this project from other python environments on the system, create a new conda environment. Our scripts were all based on python 3.9:
```
conda create --name cse517 python=3.9
conda activate cse517
```
Install the base package requirements:
```
pip install -r requirements.txt
```
Install pytorch with pip by following the instructions on the [Pytorch website](https://pytorch.org/), the command should look something like:
```
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
```
The [PyTrial package](https://pytrial.readthedocs.io/en/latest/install.html) should have been installed with the `requirements.txt` file. PyTrial contains the most up-to-date code for PromptEHR. In case the package wasn't properly installed previously:
```
pip install pytrial
```

Full documentation of the group's setup process can be found [here](./setup.md).

# Preprocessing

More information about converting the CSV files from the MIMIC-III dataset into the files required for training can be found in [this markdown file](./data_conversion/README.md).

# Training

To train the model using the hyperparameters from the PromptEHR paper, simply run the [training script](./train.py):
```
python train.py
```
Some parameters such as the number of epochs, batch size, number of training samples, and evaluation frequency can be updated by changing the constants definined in the `train.py` file. 

# Evaluation

The code to evaluate the perplexity, privacy, and utility of the models is in the `evaluate.ipynb` notebook file. This file assumes there is a fully trained model in the folder `./model_50_epochs_30k_samples` and a partially trained model in the folder `./model_20_epochs_15k_samples`. These folders are ignored by git as they are too large to push to the repository.


---
## Useful Links
[CSE 517 Project Instructions](https://nasmith.github.io/NLP-winter22/assets/docs/project-517.pdf) \
[PromptEHR Paper](https://preview.aclanthology.org/emnlp-22-ingestion/2022.emnlp-main.185.pdf) \
[PromptEHR GitHub](https://github.com/RyanWangZf/PromptEHR)\
[Reproducibility Report](https://drive.google.com/file/d/1mR8rUyazhtazs4RHtBYVAeOO7tpZJA59/view)
