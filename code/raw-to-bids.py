import os
import numpy as np
import mne
from mne_nirs.io.snirf import write_raw_snirf
from mne_bids import write_raw_bids, BIDSPath, print_dir_tree

trial_type = {'Control': 1, 'Tapping/Left': 2,
              'Tapping/Right': 3, 'ExperimentEnds': 15}
stimulus_duration = 5

# Loop over each participant
for sub in range(1, 6):
    subject_id = "%02d" % sub

    # Find source data
    bpath = BIDSPath(subject=subject_id, task='tapping', datatype='nirs',
                     root='../sourcedata')
    dname = str(bpath.directory)
    fname = dname + "/" + next(os.walk(dname))[1][0]

    # Read source data
    raw = mne.io.read_raw_nirx(fname, preload=False)

    # Create BIDS path and write to file
    snirf_path = dname + "/" + bpath.basename + ".snirf"
    write_raw_snirf(raw, snirf_path)

    # Read source data
    raw = mne.io.read_raw_snirf(snirf_path, preload=False)
    raw.annotations.duration = np.ones(raw.annotations.duration.shape) * \
                               stimulus_duration
    raw.info['line_freq'] = 50  # specify line frequency as required by BIDS
    events, event_id = mne.events_from_annotations(raw,
                                                   {'1.0': 1, '15.0': 15,
                                                    '2.0': 2, '3.0': 3})

    bids_path = BIDSPath(subject=subject_id, task='tapping',
                         datatype='nirs', root='../')
    write_raw_bids(raw, bids_path, overwrite=True)
