#!/usr/bin/env python3

# This script is to be run to confirm the created SNIRF
# files are valid according to the specification.

from mne_bids import BIDSPath, read_raw_bids
import pysnirf2


for sub in range(1, 6):  # Loop from first to fifth subject
    ID = '%02d' % sub  # Tidy the subject name

    # Create path to file based on experiment info
    bids_path = BIDSPath(subject=ID, task="tapping",
                         root='..',
                         datatype="nirs", suffix="nirs", extension=".snirf")

    v = pysnirf2.validateSnirf(str(bids_path))	

    if v:
        print(f"File {ID} is valid")
    else:
        print(f"!!!File {ID} is NOT valid!!!")
