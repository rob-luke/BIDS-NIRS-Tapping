# BIDS-NIRS-Tapping

Example NIRS BIDS dataset

**The NIRS BIDS specification is a work in progress. This repository will change while the BEP is in developement.**

## Experiment Description

This experiment examines how the motor cortex is activated during a finger tapping task.
Participants are asked to either tap their left thumb to fingers, tap their right thumb to fingers, or nothing (control).
Tapping lasts for 5 seconds as is propted by an auditory cue.
Sensors are placed over the motor cortex as described in the montage section in the link below, short channels are attached to the scalp too.

The code to conduct the experiment can be found here... https://github.com/rob-luke/experiment-fNIRS-tapping


## Data Description

The dataset contains measurements from 5 participants. All details have been anonymised.



## How to use this repository

I have used branches in this repository to describe the steps taken to convert this data to the BIDS format.
Using the GitHub interface you can select the branch you wish to view.
The branches are...

* [00-Raw-data](https://github.com/rob-luke/BIDS-NIRS-Tapping/tree/00-Raw-data): Contains just the raw recordings
* [01-Raw-to-SNIRF](https://github.com/rob-luke/BIDS-NIRS-Tapping/tree/01-Raw-to-SNIRF): Converts the original data to snirf, but not BIDS.
* [02-Raw-to-BIDS](https://github.com/rob-luke/BIDS-NIRS-Tapping/tree/02-Raw-to-BIDS): Converts the original data to BIDS (or as close as can be automated, before manual editing and movement to master).
* [master](https://github.com/rob-luke/BIDS-NIRS-Tapping): Dataset in BIDS format.

