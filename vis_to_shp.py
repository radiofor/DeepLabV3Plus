# -*- coding: utf-8 -*-
import sys
sys.path.append(r'F:\Projects\Win10\GATL')
import os
import shutil
import numpy as np
from skimage import io
from geotiff import Management as gatl_gtifman
from shapefile import Management as gatl_shpman
from shapefile import Geoprocessing as gatl_shpgpr


wf_dir = r'G:\ResearchArea\Nepal\QGIS\WorldFile'
voc_dir = r'G:\ResearchArea\Nepal\VOC_L'
ds_name = 'val'
index_dir = os.path.join(voc_dir, 'Index')
index_path = os.path.join(index_dir, ds_name + '.txt')
vis_dir = os.path.join(voc_dir, 'vis_log', ds_name)
segm_dir = os.path.join(voc_dir, 'segm_' + ds_name)
segm_gtif_dir = os.path.join(segm_dir, 'gtif')
segm_shp_dir = os.path.join(segm_dir, 'shp')
if os.path.exists(segm_dir):
    shutil.rmtree(segm_dir)
os.mkdir(segm_dir)
os.mkdir(segm_gtif_dir)
os.mkdir(segm_shp_dir)
segm_shp_path = os.path.join(segm_dir, 'segm_' + ds_name + '.shp')

index = []
with open(index_path, 'r') as f:
    line = f.readline().replace('\n', '')
    while line:
        index.append(line)
        line = f.readline().replace('\n', '')

for fname in os.listdir(vis_dir):
    file_path = os.path.join(vis_dir, fname)
    mname, suffix = os.path.splitext(fname)
    idx, cls = mname.rsplit('_', 1)
    if cls == 'prediction':
        img_arr = io.imread(file_path)
        img_size = [x for x in img_arr.shape]
        zeros_arr = np.zeros(img_size, np.uint8)
        if (img_arr == zeros_arr).all():
            os.remove(file_path)
        else:
            idx = int(idx)
            os.rename(file_path, os.path.join(vis_dir, index[idx] + suffix))
    elif cls == 'image':
        os.remove(file_path)

gatl_gtifman.create_by_image_and_worldfile(vis_dir, wf_dir, '.png', '.jpw', 'epsg:3857', segm_gtif_dir)
gatl_gtifman.set_nodata_value(segm_gtif_dir, 0)
gatl_gtifman.convert_to_shapefile(segm_gtif_dir, [1], segm_shp_dir)
gatl_shpman.merge(segm_shp_dir, segm_shp_path)
gatl_shpgpr.disolve(segm_shp_path, segm_dir, ['FID'], None, 'first')
