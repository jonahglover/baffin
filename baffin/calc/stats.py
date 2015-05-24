import scipy.stats
 
def pNorm(x, mu, std):
	return scipy.stats.norm(mu, std).pdf(x)

