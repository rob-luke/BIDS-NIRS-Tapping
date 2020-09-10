# Import libraries
import os
import mne
from mne_nirs.io.snirf import write_raw_snirf
from mne_bids import BIDSPath

# Loop over each participant
for sub in range(1, 6):
    subject_id = "%02d" % sub

    # Find source data
    dname = BIDSPath(subject=subject_id, task='tapping', datatype='nirs',
                     root='../sourcedata')
    dname = str(dname.directory)
    fname = dname + "/" + next(os.walk(dname))[1][0]

    # Read source data
    raw = mne.io.read_raw_nirx(fname, preload=False)

    # Create BIDS path and write to file
    bids_path = BIDSPath(subject=subject_id, task='tapping', datatype='nirs',
                         root='..', suffix='nirs', extension='.snirf').mkdir()
    write_raw_snirf(raw, bids_path)
