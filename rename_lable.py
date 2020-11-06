# -*- coding: utf-8 -*-
import os


idx_path = r'G:\RockGlacier\Himalaya\VOC\Index\val.txt'
lbl_dir = r'G:\RockGlacier\Himalaya\VOC\Label'
lbl_names = [x for x in os.listdir(lbl_dir)]

idx_names = []
with open(idx_path, 'r') as f:
    line = f.readline()
    while line:
        idx_names.append(line.strip() + '.png')
        line = f.readline()

for lbl_name, idx_name in zip(lbl_names, idx_names):
    src_path = os.path.join(lbl_dir, lbl_name)
    dst_path = os.path.join(lbl_dir, idx_name)
    os.rename(src_path, dst_path)
