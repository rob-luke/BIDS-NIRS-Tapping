import os.path as op

import mne
from mne.datasets import sample

from mne_bids import (write_raw_bids, read_raw_bids,
                      BIDSPath, print_dir_tree)


# Import libraries
import os
import mne
from mne_nirs.io.snirf import write_raw_snirf
from mne_bids import BIDSPath

trial_type = {'Control': 1, 'Audio/Noise': 2, 'Audio/IAC050': 3}

# Loop over each participant
for sub in range(1, 6):
    subject_id = "%02d" % sub

    # Find source data
    dname = BIDSPath(subject=subject_id, task='tapping', datatype='nirs',
                     root='../')
    dname = str(dname.directory)
    fname = dname + "/" + next(os.walk(dname))[1][0]

    # Read source data
    raw = mne.io.read_raw_nirx(fname, preload=False)
    raw.info['line_freq'] = 50  # specify line frequency as required by BIDS


    # # Create BIDS path and write to file
    # bids_path = BIDSPath(subject=subject_id, task='tapping', datatype='nirs',
    #                      root='..', suffix='nirs', extension='.snirf').mkdir()
    #
    # events, event_id = mne.events_from_annotations(raw)
    #
    # write_raw_bids(raw, bids_path, events_data=events,
    #                event_id=trial_type, overwrite=True)



print_dir_tree("../sub-01")