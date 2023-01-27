Contains documentation of the steps while setting up and intially testing working
with the PromptEHR code.

---

## Steps to set up the environment 

* created Anaconda environment with Python version 3.9
```
conda create --name cse517 python=3.9
conda activate cse517
```

* copied requirements file from https://github.com/RyanWangZf/PromptEHR/blob/main/requirements.txt
* with the conda environments version of pip, ran:

```
pip install -r .\requirements.txt
pip install promptehr
```
* Seeing error 
```
ImportError: cannot import name 'GreedySearchOutput' from 'transformers.generation_utils'
```
* Fixed error by downloading different version of transformers package (updated the `requirements.txt` file):
```
pip uninstall transformers
pip install transformers==4.19.0
```

## Working with existing model
* Added example found on website to python file and ran
```
from promptehr import PromptEHR
model = PromptEHR()
model.from_pretrained()
```
* Saw loading bars, created a `./simulation/pretrained_promptEHR` folder containing:
```
config.json
data_tokenizer.pkl
latest.checkpoint.pth.tar
model_tokenizer.pkl
promptehr_config.json
promptEHR_pretrained.zip
```
* Got error:
```
AssertionError: Torch not compiled with CUDA enabled
```
* Went [here](https://developer.nvidia.com/cuda-downloads) and installed CUDA on my Windows 10 computer, then went [here](https://pytorch.org/get-started/locally/) for pytorch install command:

```
conda install pytorch torchvision torchaudio pytorch-cuda=11.6 -c pytorch -c nvidia
```

* Then retried 
```
from promptehr import PromptEHR
model = PromptEHR()
model.from_pretrained()
```

* Got error:
```
ImportError: cannot import name 'COMMON_SAFE_ASCII_CHARACTERS' from 'charset_normalizer.constant'
```
* Fixed by running:
```
pip uninstall charset_normalizer
```
* Untill it said all versions were uninstalled then ran
```
pip install charset_normalizer
```
* Tried rerunning:
```
from promptehr import PromptEHR
model = PromptEHR()
model.from_pretrained()
```
* Got a `RequestsDependencyWarning` that was fixed with:
```
pip install --upgrade requests==2.20.1
```