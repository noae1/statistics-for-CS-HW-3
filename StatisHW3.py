import math
import matplotlib.pyplot as plt
from scipy.stats import geom
from scipy.stats import poisson
import numpy as np
import pandas as pd


# a
p =  poisson.ppf(q=0.9, mu=20)
print (p)

# b
p =  poisson.ppf(q=0.1, mu=20)
print (p)

# c
IQR = poisson.ppf(q=0.75, mu=20) - poisson.ppf(q=0.25, mu=20)
print (IQR)

# d
under16 = poisson.cdf(16 ,20)
print (under16)

# e
print (1/under16)

# f
print (geom.ppf(q=0.75, p=under16))