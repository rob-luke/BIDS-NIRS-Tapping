import os
import mne
from mne_bids import write_raw_bids, make_bids_basename, make_bids_folders


trial_type = {'Control': 1, 'Tapping/Left': 2, 'Tapping/Right': 3}


"""Test conversions of meas_date to datetime objects."""


# Loop over each participant
for sub in range(1, 2):
    subject_id = "%02d" % sub

    # Find source data
    fname = make_bids_folders(subject=subject_id, kind='nirs',
                              bids_root='../sourcedata', make_dir=False)
    fname = fname + "/" + next(os.walk(fname))[1][0]

    # Read source data
    raw = mne.io.read_raw_nirx(fname, preload=False)
    events, event_id = mne.events_from_annotations(raw)

    bids_basename = make_bids_basename(subject=subject_id,
                                       task="tapping", suffix='nirs.snirf')
    write_raw_bids(raw, bids_basename, "../", event_id=trial_type,
                   events_data=events, overwrite=True, verbose=True)
