import math as m



def calcLCOE(capitalCosts, annualOperatingCost, annualElectricityGeneration, discountRate, numberOfYears):

    necessaryRevenue = capitalCosts + calcOperatingCosts(numberOfYears, annualOperatingCost, discountRate)
    revenue = calcRevenue(numberOfYears, annualElectricityGeneration, discountRate)
    return necessaryRevenue/revenue


def calcPWF(discountRate, nYears):
    presentWorthFactor = 1 / m.pow((1 + discountRate), nYears)
    return presentWorthFactor

def calcOperatingCosts(numberOfYears, annualOperatingCost, discountRate):
    costs = 0
    for i in range (1, numberOfYears+1):
        costs += annualOperatingCost * calcPWF(discountRate, i)
    print(costs)
    return costs

def calcRevenue(numberOfYears, annualElectricityGeneration, discountRate):
    revenue = 0
    for i in range (1, numberOfYears+1):
        revenue += annualElectricityGeneration * calcPWF(discountRate, i)

    return revenue


