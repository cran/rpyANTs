import sys
sys.path.append('/Users/dipterix/Dropbox (Personal)/projects/rpyANTs/inst/rpyants/rpyants')
from rpyants.utils.paths import normalize_path, ensure_dir, file_path, parse_bids_filename, to_bids_prefix, file_copy, ensure_basename, unlink
from rpyants.registration.halpern import halpern_coregister_ct_mri
from rpyants.utils.transforms import ants_AffineTransform_to_m44, M44_LPS_to_RAS
from rpyants.registration.yael import YAELPreprocess
import os
subject_code = "testtest2"
work_path = '/Users/dipterix/rave_data/raw_dir/testtest2/rave-imaging/'
# ct_path = '/Users/dipterix/rave_data/raw_dir/testtest/rave-imaging_old/sub-AnonSEEG_ses-postop_desc-preproc_CT.nii'
# mr_path = '/Users/dipterix/rave_data/raw_dir/testtest/rave-imaging_old/sub-AnonSEEG_ses-preop_desc-preproc_acq-ax_T1w.nii'
# template_path = "/Users/dipterix/rave_data/others/three_brain/templates/mni_icbm152_nlin_asym_09b/T1.nii.gz"
# template_name = 'MNI152NLin2009bAsym'
native_type = "T1w"
type = "CT"
verbose = True
kwargs = {}
self = YAELPreprocess(subject_code, work_path)
self._images
# self.set_image("CT", ct_path, overwrite = True)
# self.set_image("T1w", mr_path, overwrite = True)
# self.input_ct_path
# self.input_t1w_path
# path = "/Users/dipterix/rave_data/raw_dir/mni152_c/rave-imaging/fs/RAVE/atlases/Harvard_Oxford_Thr25_2mm_Whole_Brain_Makris_2006/lh/Superior_Temporal_Gyrus_posterior_division_L_T1.nii.gz"

# self.register_to_T1w("CT")
# self.map_to_template(
#     template_name = "MNI152NLin2009aAsym",
#     template_path = "/Users/dipterix/rave_data/others/three_brain/templates/mni_icbm152_nlin_asym_09a/T1.nii.gz",
#     template_mask_path = "/Users/dipterix/rave_data/others/three_brain/templates/mni_icbm152_nlin_asym_09a/T1_brainmask.nii.gz"
# )