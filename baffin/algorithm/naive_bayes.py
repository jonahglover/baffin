import scipy.stats

from base import Algorithm

class NaiveBayes(Algorithm):

  def __init__(self, options = {}):
    Algorithm.__init__(self, 0, options)

  def train(self, ratio = .67):
    self.dataset.splitMeasurements(ratio)
    self.trainingSummary = self.dataset.trainData.classSummary()

  def predict(self):
    correct = 0
    for i in range(len(self.dataset.testData.measurements)):
      measurement = self.dataset.testData.measurements[i]
       # for each measurements
      classProbabilities = {}
      for classValue, summary in self.trainingSummary.iteritems():
        classProbability = 1.0
        for attributeSummary, attribute in zip(summary, measurement.data):
          attributeProbability = scipy.stats.norm(attributeSummary["mean"], attributeSummary["sd"]).pdf(attribute)
          classProbability*=attributeProbability
        classProbabilities[classValue] = classProbability
      maxP   = -1
      pClass = -1
      
      for classValue, classProbability in classProbabilities.iteritems():
        if classProbability > maxP:
          pClass = classValue
          maxP   = classProbability
      
      measurement.setPredictedClass(pClass)
      if pClass == measurement.getClass():
        correct+=1

    print("Accuracy: " + str(100*(correct/float(len(self.dataset.testData.measurements)))) + "%")



