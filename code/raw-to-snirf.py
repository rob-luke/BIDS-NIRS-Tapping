# Import libraries
import os
import mne
from mne_nirs.io.snirf import write_raw_snirf
from mne_bids import write_raw_bids, make_bids_basename, make_bids_folders

# Loop over each participant
for sub in range(1, 6):
    subject_id = "%02d" % sub

    # Find source data
    fname = make_bids_folders(subject=subject_id, kind='nirs',
                              bids_root='../sourcedata', make_dir=False)
    fname = fname + "/" + next(os.walk(fname))[1][0]

    # Read source data
    raw = mne.io.read_raw_nirx(fname, preload=False)

    # Create BIDS directory and file name
    bids_dirname = make_bids_folders(subject=subject_id, kind='nirs',
                                     make_dir=True, bids_root='..')
    bids_basename = make_bids_basename(subject=subject_id,
                                       task="tapping", suffix='nirs.snirf')
    bids_fname = bids_dirname + "/" + bids_basename

    # Write as SNIRF
    write_raw_snirf(raw, bids_fname)
