import random

def partitionData(dataset, ratio):
  trainingData = []
  testData     = list(dataset)
  while len(trainingData) < int(len(dataset)*ratio):
    trainingData.append(testData.pop(random.randrange(len(testData))))
  return [trainingData, testData]
