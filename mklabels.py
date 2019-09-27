from os import listdir
from os.path import isfile, join
import csv

all_labels_arr = [f[10:11] for f in listdir("/mnt/c/Users/Chris/Documents/SpeechEmotionRecog/WAVE") if isfile(join("/mnt/c/Users/Chris/Documents/SpeechEmotionRecog/WAVE", f))]
train_labels_arr = [str(int(x)-1) for x in all_labels_arr[:1200]]
test_labels_arr = [str(int(x)-1) for x in all_labels_arr[1200:]]

with open('train_labels.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(train_labels_arr)
csvFile.close()
with open('test_labels.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(test_labels_arr)
csvFile.close()

