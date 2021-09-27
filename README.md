# BIDS fNIRS Example Dataset

[![DOI](https://zenodo.org/badge/294376526.svg)](https://zenodo.org/badge/latestdoi/294376526)

**The fNIRS BIDS specification is a work in progress. Expect changes while the BEP is in developement.**

Example fNIRS dataset that is formated according to the [BIDS specification](https://bids-specification--802.org.readthedocs.build/en/802/03-modality-agnostic-files.html).

This repository provides an example dataset demonstrating how a BIDS dataset should be stored.
And also demonstrates how to convert measurements obtained using a NIRx device to BIDS using [MNE-BIDS](https://mne.tools/mne-bids/stable/index.html) (see branches below for script details).


## Experiment Description

This experiment examines how the motor cortex is activated during a finger tapping task.
Participants are asked to either tap their left thumb to fingers, tap their right thumb to fingers, or nothing (control).
Tapping lasts for 5 seconds as is propted by an auditory cue.
Sensors are placed over the motor cortex as described in the montage section in the link below, short channels are attached to the scalp too.
Further details about the experiment (including presentation code) can be found at [rob-luke/experiment-fNIRS-tapping](https://github.com/rob-luke/experiment-fNIRS-tapping) 


## Data Description

The dataset contains measurements from 5 participants. All details have been anonymised by hand in the raw data. Alternatively the `anonymise` argument could be used when [writing](https://mne.tools/mne-bids/stable/generated/mne_bids.write_raw_bids.html#mne_bids.write_raw_bids) the BIDS dataset.



## How to use this repository

I have used branches in this repository to describe the steps taken to convert this data to the BIDS format.
Using the GitHub interface you can select the branch you wish to view.
The branches are...

* [00-Raw-data](https://github.com/rob-luke/BIDS-NIRS-Tapping/tree/00-Raw-data): Contains just the raw recordings
* [01-Raw-to-SNIRF](https://github.com/rob-luke/BIDS-NIRS-Tapping/tree/01-Raw-to-SNIRF): Converts the original data to snirf, but not BIDS.
* [02-Raw-to-BIDS](https://github.com/rob-luke/BIDS-NIRS-Tapping/tree/02-Raw-to-BIDS): Converts the original data to BIDS (or as close as can be automated, before manual editing and movement to master).
* [master](https://github.com/rob-luke/BIDS-NIRS-Tapping): Dataset in BIDS format.

Branches `00` and `01` are only included for interested researchers. To generate the data in master use branch `02`, then remove the sourcedata directory and manually enter the author in to `dataset_description.json`.

