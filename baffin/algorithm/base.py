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

    # TODO: move this into a service
    print("reading data...")
    self.readData(options["filename"])
    print("partitioning data...")
    self.partitionData(options["ratio"])
    print("data processing complete!"

  def train(self):
    self.notImplementedException()

  def readData(self, filename):
    # TODO it would be nice to have an actual datatype rather than just a vector
    # maybe something like "Measurement"
    self.data = io.loadDataset(filename)

  def partitionData(self, ratio):
    self.trainingData, self.testData = process.partitionData(self.data, ratio)