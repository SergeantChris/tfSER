import pandas as pd
import csv
import random

with open('train_data.csv', 'r') as f1, open('train_labels.csv', 'r') as f2, open('train_joined.csv', 'w') as out:
    writer = csv.writer(out)
    r1, r2 = csv.reader(f1), csv.reader(f2)
    while True:
        try:
            writer.writerow(next(r1)+next(r2))
        except StopIteration:
            break

with open('test_data.csv', 'r') as f1, open('test_labels.csv', 'r') as f2, open('test_joined.csv', 'w') as out:
    writer = csv.writer(out)
    r1, r2 = csv.reader(f1), csv.reader(f2)
    while True:
        try:
            writer.writerow(next(r1)+next(r2))
        except StopIteration:
            break
#synenwsh data kai labels gia ta train kai test sets gia na mh xathei
#h antistoixhsh kata to shuffling

fid = open('train_joined.csv', 'r')
train = fid.readlines()
fid.close()
random.shuffle(train)
fid = open('train_joinedSFL.csv', 'w')
fid.writelines(train)
fid.close()

fid = open('test_joined.csv', 'r')
test = fid.readlines()
fid.close()
random.shuffle(test)
fid = open('test_joinedSFL.csv', 'w')
fid.writelines(test)
fid.close()
#shuffling gia na tyxaiopoihthei h seira

with open('train_joinedSFL.csv', 'r') as s, open('train_dataSFL.csv', 'w') as d1, open('train_labelsSFL.csv', 'w') as d2:
    reader = csv.reader(s)
    w1 = csv.writer(d1)
    w2 = csv.writer(d2)
    for row in reader:
        w1.writerow((row[:-1]))
        w2.writerow((row[-1]))
		
with open('test_joinedSFL.csv', 'r') as s, open('test_dataSFL.csv', 'w') as d1, open('test_labelsSFL.csv', 'w') as d2:
    reader = csv.reader(s)
    w1 = csv.writer(d1)
    w2 = csv.writer(d2)
    for row in reader:
        w1.writerow((row[:-1]))
        w2.writerow((row[-1]))
#eggrafh se xwrista data kai label files