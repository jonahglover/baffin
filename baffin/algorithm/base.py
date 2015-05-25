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

  def train(self):
    self.notImplementedException()

  def loadMeasurements(self, filename):
    self.dataset = data.DataSet()
    self.dataset.loadFile(filename)


