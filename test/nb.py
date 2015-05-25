from baffin.algorithm import *

nb = algorithm.NaiveBayes()
nb.loadMeasurements("./pima.csv")
nb.train()
nb.predict()