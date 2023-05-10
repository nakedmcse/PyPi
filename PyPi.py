import time
import numpy as np

#Calculate pi to a given number
def Leibniz(iterations):
    n = 1
    for i in range(2,iterations - 1):
        term = ((-1.0) ** (i - 1.0)) / ((2 * i) - 1.0)
        n = n + term 
    return n*4

def LeibnizNP(iterations):
    i = np.arange(0, iterations)
    term = ((-1.0) ** i) / ((2 * i) + 1.0)
    n = np.sum(term)
    return n*4

def LeibnizTurbo(iterations):
    n = 1
    topterm = -1.0
    for i in range(2,iterations - 1):
        bottomterm = i << 1  #Fast bitwise x2 whilst i still int
        term = topterm / (bottomterm - 1.0)
        n = n + term 
        topterm = -topterm  #Flip top between 1 and -1 without exponentiating
    return n*4

def LeibnizTurboNP(iterations):
    topterm = np.ones(iterations)
    topterm[1::2] = -1
    bottomterms = np.arange(0, iterations*2, 2) + 1
    terms = topterm / bottomterms
    n = np.sum(terms)
    return n*4

#Main
print()
print("Starting Leibniz Approximation")
start_time = time.time()
print(LeibnizTurboNP(100000000))
end_time = time.time()

elapsed = end_time - start_time
print(f"Elapsed Time: {elapsed:.4f} seconds")
print()
print()
