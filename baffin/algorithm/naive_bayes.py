from base import Algorithm

class NaiveBayes(Algorithm):

  def __init__(self, options = {}):
    Algorithm.__init__(self, 0, options)

  def train(self):

    # separate into classes
    separatedData = {}
    for point in self.trainingData:
      if point[-1] not in separatedData:
        separatedData[point[-1]] = []
      separatedData[point[-1]].append(point)

    #
