# -*- coding: utf-8 -*-
import os
import random
import shutil


fatherFolder = r'G:\RockGlacier\India\Himachal'
index_path = os.path.join(fatherFolder, r'VOC\Index')
dataList = os.listdir(r'G:\RockGlacier\India\Himachal\QGIS\Google')
if os.path.exists(index_path):
    shutil.rmtree(index_path)
os.mkdir(index_path)

train_path = os.path.join(fatherFolder, r'VOC\train_log')
if os.path.exists(train_path):
    shutil.rmtree(train_path)
os.mkdir(train_path)

val_path = os.path.join(fatherFolder, r'VOC\vis_log')
if os.path.exists(val_path):
    shutil.rmtree(val_path)
os.mkdir(val_path)

eval_path = os.path.join(fatherFolder, r'VOC\eval_log')
if os.path.exists(eval_path):
    shutil.rmtree(eval_path)
os.mkdir(eval_path)

random.shuffle(dataList)
dataCount = len(dataList)
trainRate = 0
valRate = 1 - trainRate
with open(os.path.join(fatherFolder, r'VOC\Index\trainval.txt'), 'w') as trainvalf:
    for i in range(dataCount):
        trainvalf.write(dataList[i].split('.')[0] + '\n')
with open(os.path.join(fatherFolder, r'VOC\Index\train.txt'), 'w') as trainf:
    for i in range(int(dataCount * trainRate)):
        trainf.write(dataList[i].split('.')[0] + '\n')
with open(os.path.join(fatherFolder, r'VOC\Index\val.txt'), 'w') as valf:
    for i in range(int(dataCount * trainRate), dataCount):
        valf.write(dataList[i].split('.')[0] + '\n')
with open(os.path.join(fatherFolder, r'VOC\count.txt'), 'w') as countf:
    countf.write('trainval:' + str(dataCount) + '\n')
    countf.write('train:' + str(int(dataCount * trainRate)) + '\n')
    countf.write('val:' + str(dataCount - int(dataCount * trainRate)) + '\n')
