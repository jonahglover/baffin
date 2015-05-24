from baffin.data import *

class Algorithm(object):

  ALGORITHM_TYPES = {
    0 : "NAIVEBAYES"
  }

  def notImplementedException():
    raise Exception("not implemented")

  def __init__(self, type, options = {}):
    if type in self.ALGORITHM_TYPES:
      self.type = type
    else:
      self.notImplementedException()

    # read data
    print("reading data...")
    self.readData(options["filename"])
    print("partitioning data...")
    self.partitionData(options["ratio"])
    print("data processing complete!")

  def classify(self):
    self.notImplementedException()

  def readData(self, filename):
    self.data = io.loadDataset(filename)

  def partitionData(self, ratio):
    self.trainingData, self.testData = process.partitionData(self.data, ratio)