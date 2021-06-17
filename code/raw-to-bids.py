import os
import numpy as np
import mne
from mne_nirs.io.snirf import write_raw_snirf
from mne_bids import write_raw_bids, BIDSPath, print_dir_tree

# There are the values you are likely to need to change
event_codes = {'1.0': 1, '15.0': 15, '2.0': 2, '3.0': 3}
trial_type = {1: 'Control', 2: 'Tapping/Left', 3: 'Tapping/Right', 4: 'ExperimentEnds'}
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

    # Set the annotations up correctly. This is currently a bit hacky
    events, event_id = mne.events_from_annotations(raw, event_codes)
    raw.set_annotations(mne.annotations_from_events(events, raw.info['sfreq'],
                                                    event_desc=trial_type))
    raw.annotations.duration = np.ones(raw.annotations.duration.shape) * \
                               stimulus_duration

    # specify line frequency as required by BIDS
    raw.info['line_freq'] = 50

    bids_path = BIDSPath(subject=subject_id, task='tapping',
                         datatype='nirs', root='../')
    write_raw_bids(raw, bids_path, overwrite=True)
