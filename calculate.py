#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 13:06:57 2019

@author: user
"""
import scipy
import scipy.constants as sc
import numpy as np
import statistics
import math
n = 2
h = sc.h
c = sc.c
E = 35 * sc.electron_volt * 1000
f = E/h
lambdaval = c / f
dd = 564 / math.pow(10,12)
xe = np.arcsin((n * lambdaval)/(dd))
theta = (n * lambdaval)/(dd)
#%%
from scipy.stats import linregress
import matplotlib.pyplot as mt
x = [5.16,7.70,13.4,15.0,20.20,22.7]
y = [6.436,7.269,12.95,14.66,19.65,22.31]
#mt.scatter(x,y)
#slope,intercept,rvalue,pvalue,stderr=linregress(x,y)
#fit=np.polyfit(x,y,1)
#bfl=np.poly1d(fit)
#mt.plot(x,bfl(x),color="red")
slope = [15.17,33.37,33.95,83.22,140.48,188.58]
intercept = [-125.01,-234.08,-196.78,-443.34,-734.25,-942.39]
charger = sc.elementary_charge
voltages = np.array([15,18,21,24,27,30]) * 1000 * sc.electron_volt * sc.elementary_charge
veri = []
h = np.array([])
for i in range(len(slope)):
    veri.append(sc.c / (-1 * (intercept[i]/slope[i])))
slope,intercept,rvalue,pvalue,stderr=linregress(veri,voltages)
fit=np.polyfit(veri,voltages,1)
bfl=np.poly1d(fit)
mt.plot(veri,bfl(veri),color="red")
mt.scatter(veri,voltages)