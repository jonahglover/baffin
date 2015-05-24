import csv

def loadDataset(filename):
	dataset = list(csv.reader(open(filename, "rb")))
	for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
	return dataset
