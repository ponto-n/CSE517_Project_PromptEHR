from promptehr import SequencePatient
from promptehr import load_synthetic_data
from promptehr import PromptEHR

# init model
model = PromptEHR()
model.from_pretrained()

# load input data
demo = load_synthetic_data(n_sample=10) # we have 10,000 samples in total

# build the standard input data for train or test PromptEHR models
seqdata = SequencePatient(data={'v':demo['visit'], 'y':demo['y'], 'x':demo['feature'],},
    metadata={
        'visit':{'mode':'dense'},
        'label':{'mode':'tensor'}, 
        'voc':demo['voc'],
        'max_visit':20,
        }
    )
# you can try to fit on this data by
# model.fit(seqdata)

# start generate
# n: the target total number of samples to generate
# n_per_sample: based on each sample, how many fake samples will be generated
# the output will have the same format of `SequencePatient`
fake_data = model.predict(seqdata, n=10, n_per_sample=10)