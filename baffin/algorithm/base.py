class Algorithm(object):

  ALGORITHM_TYPES = {
    0 : "NAIVEBAYES"
  }

  def __init__(self, type, options = {}):
    if type in self.ALGORITHM_TYPES:
      self.type = type
  def classify(self):
    self.notImplementedException()
