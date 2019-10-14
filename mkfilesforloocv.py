import csv

with open('train_dataSFLCUT2.csv', 'r') as d1, open('test_dataSFLCUT2.csv', 'r') as d2, open('dataSFLCUT2.csv', 'w') as da:
	writer = csv.writer(da)
	r1, r2 = csv.reader(d1), csv.reader(d2)
	for row in r1:
		writer.writerow(row)
	for row in r2:
		writer.writerow(row)
		
with open('train_labelsSFL.csv', 'r') as l1, open('test_labelsSFL.csv', 'r') as l2, open('labelsSFL.csv', 'w') as la:
	writer = csv.writer(la)
	r1, r2 = csv.reader(l1), csv.reader(l2)
	for row in r1:
		writer.writerow(row)
	for row in r2:
		writer.writerow(row)
#synenwsh test kai train files gia data kai labels