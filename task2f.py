import logbin as lb

import numpy as np

import matplotlib.pyplot as plt

import pickle as p

import collections

import interpolation as interp

# avalanche size is the number of topples which happen before next grain is
# added

# only measure after critical time is reached

l = [4,8,16,32,64,128,256]

avh = [] # average height

sdh = [] # standard deviation of height

ph = []

for j in l:
    
    filein =  open(f"{j}_0", "rb")

    sandbox = p.load(filein)

    ah = 0

    sh1 = 0

    t = 0

    d,n,pn = 0,0,0

    ph = []

    for i in sandbox:

        if i[3] != '':

            ah += i[1]

            sh1 += i[1]**2

            ph.append(i[1])

            t += 1

    avh.append(ah/t)

    sdd = (sh1/t - (ah/t)**2)**0.5

    sdh.append(sdd)

#fit linear to log(sigma)vs log(L)

x2 = np.array(np.log(l))

y2 = np.array(np.log(sdh))

A = np.vstack([x2, np.ones(len(x2))]).T

m, c = np.linalg.lstsq(A, y2, rcond=None)[0]

# Polynomial Regression

def polyfit(x, y, degree):
    
    results = {}

    coeffs = np.polyfit(x, y, degree)

    # Polynomial Coefficients
     
    results['polynomial'] = coeffs.tolist()

    # r-squared
    
    p = np.poly1d(coeffs)
    
    # fit values, and mean
    
    yhat = p(x) 
    
    ybar = np.sum(y)/len(y)
    
    ssreg = np.sum((yhat-ybar)**2)
    
    sstot = np.sum((y - ybar)**2)
    
    results['determination'] = ssreg / sstot

    return results

r_value = polyfit(x2,y2,1)['determination']

print(r_value, m)

a = np.arange(0,max(x2)+1,1)

yy = []

for x in a:

    yy.append(m*x + c)

# error on gradient and intercept

p, V = np.polyfit(x2, y2, 1, cov=True)

print("alpha: {} +/- {}".format(p[0], np.sqrt(V[0][0])))

print("ln(a): {} +/- {}".format(p[1], np.sqrt(V[1][1])))

vb = interp.linearinter(a,yy)

x3 = vb[0]

y3 = vb[1]

plt.rcParams.update({'font.size': 28})

plt.scatter(x3, y3, s = 1, marker = "x", label = 'linear fit')

plt.rcParams.update({'font.size': 32})

plt.scatter(np.log(l),np.log(sdh), c = 'black' ,s = 900, marker = "+", label = 'data')

plt.xlabel('ln(L)')

plt.xlim(0,max(x3))

plt.ylabel('ln(standard deviation of height)')

plt.title('Standard deviation of heights')

plt.legend()
    
plt.show()



