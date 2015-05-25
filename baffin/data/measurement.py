class Measurement(object):

  def __init__(self, data):
    self.data  = data
    self.classification = int(data.pop(-1)) # assume -1 is class of measurement

  def getClass(self):
    return self.classification

  def setPredictedClass(self, classValue):
    self.predictedClass = classValue