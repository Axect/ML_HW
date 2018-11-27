#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt

xn=np.array([1896,1900,1904,1906,1908,1912,1920,1924,1928,1932,1936,1948,1952,1956,1960,\
1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008],dtype=np.float64)
tn=np.array([12.0,11.0,11.0,11.2,10.8,10.8,10.8,10.6,10.8,10.3\
,10.3,10.3,10.4,10.5,10.2,10.0,9.95,10.14,10.06,10.25,9.99,9.92\
,9.96,9.84,9.87,9.85,9.69],dtype=np.float64)
xntn=xn*tn
xn_2=xn*xn

w1 = (xntn.mean()-xn.mean()*tn.mean())/(xn_2.mean()-xn.mean()*xn.mean())
w0 = tn.mean()-w1*xn.mean()
def query(input_data):
    return w1*input_data + w0
print ("{:.3f} {:.3f}x".format(w0, w1))
print (w0+w1*2012,w0+w1*2016)

x = np.linspace(1900, 2100)

plt.plot(x,query(x))
plt.xlabel("Year")
plt.ylabel("Wining Time")
plt.title('Short Range Running Contest')
plt.show()