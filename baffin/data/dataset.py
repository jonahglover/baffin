import csv
import random
import numpy

from measurement import Measurement

class DataSet(object):

  def __init__(self, measurements = list()):
    self.measurements = measurements

  def loadFile(self, filename):
    rawMeasurements = list(csv.reader(open(filename, "rb")))
    self.measurements    = list()
    for i in range(len(rawMeasurements)):
      rawMeasurements[i] = [float(x) for x in rawMeasurements[i]]
      self.measurements.append(Measurement(rawMeasurements[i]))

  def splitMeasurements(self, ratio):
    trainSize = int(len(self.measurements)*ratio)
    trainData = list()
    testData  = list(self.measurements)
    while len(trainData) < trainSize:
      trainData.append(testData.pop(random.randrange(len(testData))))
    self.trainData = DataSet(trainData)
    self.testData  = DataSet(testData)

  def summarize(self, data):
    rawData   = [ m.data for m in data ]
    summaries = [{ "mean" : numpy.mean(attribute), "sd" : numpy.std(attribute)} for attribute in zip(*rawData)]   
    return summaries

  def classifyMeasurements(self):
    measurements = {}
    for m in self.measurements:
      if m.getClass() not in measurements:
        measurements[m.getClass()] = list()
      measurements[m.getClass()].append(m)
    return measurements

  def classSummary(self):
    classifedMeasurements = self.classifyMeasurements()
    summaries = {}
    for classValue, instances in classifedMeasurements.iteritems():
      summaries[classValue] = self.summarize(instances)
    return summaries
  