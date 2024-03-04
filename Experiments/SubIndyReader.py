import numpy as np
import os
indy_path = "../sub-indy/"
binned_file_root = "binned_array/"
binned_arr_01ms = "spike_binned_01ms.npy"
binned_file_path = indy_path+binned_file_root+binned_arr_01ms


def resample(bin=1)->np.ndarray:
    """resample the 2D-binned array and return"""
    file_path = indy_path+binned_file_root+"spike_binned_"+str(bin).zfill(2)+"ms.npy"
    if os.path.exists(file_path):
        return np.load(file_path)
    else:
        bsa_01 = np.load(binned_file_path)
        seg_n = bsa_01.shape[0] / bin
        segs = np.array_split(bsa_01, seg_n, axis=0)
        segs = [np.sum(sb, axis=0) for sb in segs]
        segs = np.array(segs)
        np.save(file_path, segs)
        return segs


def smooth(window=10):
    """smooth the spike counts"""


def segment(timestart: np.ndarray, timestop: np.ndarray):
    """cut the spike trains into segements"""


"""
(-0.7819471847315127,
 array([ 62, 113,   1,  49,  64,   5,  73,  35,  72,  67], dtype=int64))
(-1.000185445846001,
 array([ 62,  45,  77,  64,  42,  43,  67,  72, 126,  35], dtype=int64))
(1.8166077850744435,
 array([ 86,   3,  43, 126,  89,  64,  49,  35,  72,  67], dtype=int64))
(-1.0746399529451147,
 array([ 64,  79,  34,  49,  35,   5,   1, 126,  72,  67], dtype=int64))
(2.594195397029429,
 array([100, 113,   7,  49,  92,   1,  35,   5,  72,  67], dtype=int64))
(-0.7192426659857017,
 array([17, 42, 90, 49, 67, 73,  5, 64, 72, 35], dtype=int64))
(-2.0658223612968967,
 array([35, 62,  5, 76, 73, 72, 83, 64, 67,  1], dtype=int64))
(-0.895250091536794,
 array([ 64,  90,  49,   3,  75, 113,  67,  72,  35,   5], dtype=int64))
(-0.7819471847315127,
 array([ 62, 113,   1,  49,  64,   5,  73,  35,  72,  67], dtype=int64))

"""
