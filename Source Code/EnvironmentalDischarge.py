import math as m
import pandas as pd
import numpy as np
from Parsers import *


data = excelParser('Data/FlowData.xlsx', None)
allperiod = data['All period']
allperiod.rename(columns={'IN [m3/s]':'IN'},inplace=True)
# print(allperiod)


def f1():
    Mean = allperiod.IN.mean()
    final = Mean*0.5
    return(final)

def f2():

    Mean = allperiod.IN.mean()
    Q25 = np.percentile(allperiod.IN, 75)  # Q3
    Q75 = np.percentile(allperiod.IN, 25)  # Q1
    return(Q25)

def f3():
    Q50 = np.percentile(allperiod.IN, 50)  # median
    integral = np.zeros(len(allperiod.IN))
    for i in range(len(allperiod.IN)):
        if allperiod.IN[i] < Q50:
            integral[i] = allperiod.IN[i]
        else:
            integral[i] = Q50
    Vp = integral.sum()
    Vt = allperiod.IN.sum()
    IRH = Vp/Vt
    if IRH > 0.7:
        formula3 = np.percentile(allperiod.IN, 85)
    else:
        formula3 = np.percentile(allperiod.IN, 75)
    return(formula3)

def f6():
    Q95 = np.percentile(allperiod.IN, 5)
    som7 = np.zeros(len(allperiod.IN)-7)
    for i in range(len(allperiod.IN)-7):
        som7[i] = (allperiod.IN[i]+allperiod.IN[i+1]+allperiod.IN[i+2]+allperiod.IN[i+3]+allperiod.IN[i+4]+allperiod.IN[i+5]+allperiod.IN[i+6])
        mini = min(som7)
    Mean = allperiod.IN.mean()
    formula3 = max(Q95,mini,Mean)
    return(formula3)
