import csv
from measurement import Measurement

class Dataset(object):

  def __init__(self, filename, options = {}):
    self.measurements = self.loadFile(filename)


  def loadFile(self, filename):
    rawMeasurements = list(csv.reader(open(filename, "rb")))
    measurements    = list()
    for i in range(len(rawMeasurements)):
      rawMeasurements[i] = [float(x) for x in rawMeasurements[i]]
      measurements.append(Measurement(rawMeasurements[i]))
    return measurements


#filename = "/Users/jonah/Projects/baffin/test/pima.csv"
#set = Dataset(filename)
#for i in set.measurements:
#  print(i.getClass())