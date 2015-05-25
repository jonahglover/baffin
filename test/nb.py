from baffin.algorithm import *

nb = algorithm.NaiveBayes()
nb.loadMeasurements("./mammographic_masses.csv")
nb.train()
nb.predict()