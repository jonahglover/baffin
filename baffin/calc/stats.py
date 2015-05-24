import scipy.stats
import math

def pNorm(x, mu, std):
	return scipy.stats.norm(mu, std).pdf(x)


def mean(data):
  return sum(data)/float(len(data))

def sd(data):
  mean = mean(data)
  variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
  return math.sqrt(variance)