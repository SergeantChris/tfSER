# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 18:58:26 2019

@author: Chris
"""
from pyAudioAnalysis import audioFeatureExtraction as aFE
import csv

def minmax(dataset):
    mm = list()
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        value_min = min(col_values)
        value_max = max(col_values)
        mm.append([value_min, value_max])
    return mm
#ypologismos min kai max se kathe sthlh (kathe feature)
	
def normalize(dataset, mm):
    for row in dataset:
        for i in range(len(row)):
            row[i] = (row[i] - mm[i][0])/(mm[i][1] - mm[i][0])
#ypologismos kanonikopoihmenwn timwn gia ola ta deigmata

(all_feat_vects, wavlist, feat_names) = aFE.dirWavFeatureExtraction("/mnt/c/Users/Chris/Documents/SpeechEmotionRecog/WAVE", 2, 0.5, 0.01, 0.0025)
#eksagwgh xarakthristikwn

mnms = minmax(all_feat_vects)
normalize(all_feat_vects, mnms)
#klhsh parapanw synarthsewn

train_feat_vects = all_feat_vects[:1200]
test_feat_vects = all_feat_vects[1200:]
#manual split se train set kai test set

with open('train_data.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(train_feat_vects)
csvFile.close()
with open('test_data.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(test_feat_vects)
csvFile.close()
#eggrafh se csv files
