#!/usr/bin/env python3

import os
from glob import glob
import mne
from mne_nirs.io.snirf import write_raw_snirf
from mne_bids import write_raw_bids, BIDSPath


# There are the values you are likely to need to change
root = "../sourcedata"  # Where is the raw data directly from the machine stored?
task = "tapping"        # Set to whatever the name of your experiment is
stimulus_duration = 5
trigger_info = {'1.0': 'Control',
                '2.0': 'Tapping/Left',
                '3.0': 'Tapping/Right'}

# Extract information from organised folders containing raw source data
subject_dirs = glob(os.path.join(root, "sub-*"))
subjects = [subject_dir.split("-")[-1] for subject_dir in subject_dirs]
sessions = [None]  # Only a single session per subject, so this optional field is not used

# Create a BIDSPath object for handling paths for us
dataset = BIDSPath(root=root,
                   task=task,
                   datatype='nirs',
                   suffix="nirs",
                   extension=".snirf")

print("\n\nConverting raw NIRx data to BIDS format.\n")
print(f"Processing data stored at {root} = {os.path.abspath(root)}")
print(f"Found subjects: {subjects}")
print(f"Found sessions: {sessions}")


def find_subfolder_with_data(sub_dir):
    """This function returns the first directory in a folder"""
    d_name = str(sub_dir.directory)
    return d_name + "/" + next(os.walk(d_name))[1][0]


# Loop over each participant
for sub in subjects:

    # Find source data
    b_path = dataset.update(subject=sub)
    f_name = find_subfolder_with_data(b_path)

    # Read source data
    raw = mne.io.read_raw_nirx(f_name, preload=False)

    # Create BIDS path and write to file
    snirf_path = dataset.fpath
    print(f"  Recoding NIRx data as snirf in temporary location: {snirf_path}")
    write_raw_snirf(raw, snirf_path)

    # Read source data
    raw = mne.io.read_raw_snirf(snirf_path, preload=False)

    raw.annotations.set_durations(stimulus_duration)
    raw.annotations.rename(trigger_info)

    raw.info['line_freq'] = 50  # Hangover from EEG

    # Now we write the correctly formatted files to the base directory (not back in to source data)
    bids_path = dataset.copy().update(root='../')
    write_raw_bids(raw, bids_path, overwrite=True)

    print("  Cleaning up temporary files\n")
    os.remove(snirf_path)
