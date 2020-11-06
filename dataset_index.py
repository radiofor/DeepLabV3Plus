# -*- coding: utf-8 -*-
import os


ds_name = 'val'
idx_dir = r'G:\RockGlacier\Himalaya\VOC\Index'
data_dir = r'G:\RockGlacier\Himalaya\QGIS\Google\1'
data_names = [os.path.splitext(x)[0] for x in os.listdir(data_dir)]

with open(os.path.join(idx_dir, ds_name + '.txt'), 'w') as f:
    for data_name in data_names:
        f.write(data_name + '\n')