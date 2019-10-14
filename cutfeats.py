import csv

with open('train_dataSFL.csv', 'r') as s, open('train_dataSFLCUT2.csv', 'w') as d:
    reader = csv.reader(s)
    writer = csv.writer(d)
    for row in reader:
        writer.writerow((row[:3]+row[8:21]+row[34:37]+row[42:55]))
		
with open('test_dataSFL.csv', 'r') as s, open('test_dataSFLCUT2.csv', 'w') as d:
    reader = csv.reader(s)
    writer = csv.writer(d)
    for row in reader:
        writer.writerow((row[:3]+row[8:21]+row[34:37]+row[42:55]))
#symmetrikh apokoph twn ligotero xrhsimwn xarakthristikwn