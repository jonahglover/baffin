from baffin.algorithm import *

nb = algorithm.NaiveBayes({
  "filename" : "/Users/jonah/Projects/baffin/test/pima.csv",
  "ratio"    : .67
})

nb.train()
