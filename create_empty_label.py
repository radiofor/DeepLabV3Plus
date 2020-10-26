# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(r'F:\Projects\Win10\GATL')
import fileman
from skimage import io
import numpy as np


img_dir = r'G:\RockGlacier\Nyenchenthanglha\GaoFen-1\JPG'
img_suffix = '.jpg'
lbl_dir = r'G:\RockGlacier\Nyenchenthanglha\GaoFen-1\Label'
lbl_suffix = '.png'

file_paths = fileman.get_all_files(img_dir, img_suffix)
for file_path in file_paths:
    img_ds = io.imread(file_path['path'])
    zeros_arr = np.zeros(img_ds.shape, np.uint8)
    lbl_path = os.path.join(lbl_dir, file_path['mname'] + lbl_suffix)
    io.imsave(lbl_path, zeros_arr)
