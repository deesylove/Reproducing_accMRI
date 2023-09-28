# Reproducing_accMRI
### Reproducing accMRI's self-supervised k-space data corruption detector

This code aims to reproduce the self-supervised k-space data corruption discriminator from Michael Yao and Michael Hansen's "A Path Towards Clinical Adaptation of Accelerated MRI". This is a graduate assignment for CS 598 "Deep Learning for Healthcare".

# Using this Repository
## Data Download Instruction

In order to access the data for training this model, one can apply for access via NYU's open fastMRI Dataset, found here: https://fastmri.med.nyu.edu/. 

Once the data links are recieved (via email), the data can be downloaded from the provided urls via wget or curl commands, for example: 

```
curl -C - "https://fastmri-dataset.s3.amazonaws.com/v2.0/knee_singlecoil_train.tar.xz?AWSAccessKeyId=keyhereSignature=signaturehereExpires=numericaldate" --output knee_singlecoil_train.tar.xz
```
(note that the above link will not work, a genuine link must be applied for and recieved via the NYU site above).

## Prior to running the model

Prior to running the model, clone this repository or the original via the following commands:

```
git clone https://github.com/dcloveUIUC/Reproducing_accMRI
cd Reproducing_accMRI
```

OR 


```
git clone https://github.com/michael-s-yao/accMRI
cd accMRI
```


## Dependencies
Once in the correct folder, activate a python virtual environment and install the dependencies. Note that we have modified the dependencies in `Reproducing_accMRI` because we found various incompatibilities in the original. For example:

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

If running this model with the entire dataset, the data must be structured as follows:

```
└── data
    ├── knee       
        ├── knee_multicoil_train
        ├── knee_multicoil_val
        ├── knee_multicoil_test
        ├── knee_singlecoil_train
        ├── knee_singlecoil_val
        ├── knee_singlecoil_test
    ├── brain      
        ├── brain_multicoil_train
        ├── brain_multicoil_val
        ├── brain_multicoil_test
        ├── brain_singlecoil_train
        ├── brain_singlecoil_val
        ├── brain_singlecoil_test
```

## Training Code + Commands

To check if your system has access to a GPU (important to know for running this code), we've added a small program to print out whether the hardware your system can access is currently a GPU or CPU. Use that by running ```python cuda_check.py```.


In order to train this model, run the `main.py` file from the `discriminator` folder. Use input `python main.py --help` as an input to see the full range of commands. See below for a possible example:

```
cd discriminator/
python main.py --data_path ../data/knee/ --model CNN --num_gpus 1

```
In order to run inference on the model, one should create a `save_path` to save results and then run run the `infer.py` file from the same folder. Using `python infer.py --help` will yield the following as possible inputs. 
```
[-h] --data_path DATA_PATH [--coil_compression COIL_COMPRESSION] [--cache_path CACHE_PATH] [--threshmin THRESHMIN] [--model MODEL] [--reconstructor RECONSTRUCTOR]
                [--gt_correlation_map GT_CORRELATION_MAP] [--save_path SAVE_PATH] [--seed SEED] [--center_crop CENTER_CROP CENTER_CROP] [--rotation ROTATION ROTATION] [--center_frac CENTER_FRAC]  
                [--cpu] [--use_deterministic] [--accuracy_by_line]
```

As a sample input, one could use: 

```
python infer.py --data_path ../data/knee --model ../discriminator/lightning_logs/version_50/checkpoints/last.ckpt --save_path ../inference_results/ --accuracy_by_line
```

This will results in running inference on the model and saving results in the `save_path` input, including the `heatmap.pkl` file which has the aggregated results. 

See the file notebook_summary.ipynb for additional information.

See the paper's original author's GitHub Repository here: https://github.com/michael-s-yao/accMRI 
