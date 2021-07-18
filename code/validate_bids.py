#!/usr/bin/env python3

# This script is to be run after raw_to_bids.py and it will ensure
# that each file can be read after conversion to BIDS

from mne_bids import BIDSPath, read_raw_bids

def load_data(bids_path):

    raw_intensity = read_raw_bids(bids_path=bids_path, verbose=False)
    raw_intensity.load_data()
    return 1


for sub in range(1, 6):  # Loop from first to fifth subject
    ID = '%02d' % sub  # Tidy the subject name

    # Create path to file based on experiment info
    bids_path = BIDSPath(subject=ID, task="tapping",
                         root='..',
                         datatype="nirs", suffix="nirs", extension=".snirf")

    assert load_data(bids_path)