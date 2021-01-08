from scipy.stats import norm
# norm.ppf()
# norm.cdf()
d = norm.pdf(1,1,1)
c = norm.cdf(1,1,1)
p = norm.ppf(q=0.2)


print(d,c,p)

