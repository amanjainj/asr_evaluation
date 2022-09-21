Source code to process japanese ASR datasets and evaluate popular speech-to-text APIs on them.

## Setup and Installation
Install requirements using pip (in virtual environment if required)
```
pip install -r requirements.txt
```

## Download datasets
Download the CommonVoice dataset from [here](https://dev.commonvoice.allizom.org/en/datasets), unzip it, and place it in a directory of your choice

## Run scripts
- Prepare dataset
```
python3 commonvoice_dataset.py --data_root <absolute path to the root directory of the downloaded dataset> --output_path <path to store the processed output dataset>
```
- Run the evaluation script
```
python3 --dataset_path <path to the processed dataset output above> --output_path <path to store the ASR results>
```
