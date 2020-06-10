import logbin as lb

import numpy as np

import matplotlib.pyplot as plt

import pickle as p

import collections

# avalanche size is the number of topples which happen before next grain is
# added

# only measure after critical time is reached

l = [4,8,16,32,64,128,256]

avh = [] # average height

for j in l:
    
    filein =  open(f"{j}_0", "rb")

    sandbox = p.load(filein)

    ah = 0

    sh1 = 0

    t = 0

    for i in sandbox:

        if i[3] != '':

            ah += i[1]

            t += 1

    avh.append(ah/t)
    
# now have list of avg heights

#need to estimate a_0, w_1

#plot ln(1-avh/a_o*L) until get a straight line

# gradient = -w_1

#y-intercept = ln(a_1)

#a_0 > 0

#a_0 ~ <z> from before so should be around 1.5

#a_0 > <h>/L

d = 0

ao = []

for g in avh:

    ao.append(g/l[d])

    d+=1

#a_0 = np.arange(1.73,2,0.01)

#


#plot these as subplots showing a_0 value as on other task


#


##for i in a_0:
##
##    plt.figure()
##
##    y = []
##
##    x = []
##
##    k = 0
##
##    for j in avh:
##
##        #print(j / (i*l[k]))
##        
##        f = np.log(1 - ( j / (i*l[k]) ) )
##
##        #print(f)
##
##        y.append(f)
##
##        x.append(np.log(l[k]))
##
##        k += 1
##
##    plt.scatter(x,y)
##
##    plt.title(str(i))
##
##plt.show()

b = max(ao)

a_0 = np.arange(b+0.01,1.75,0.00001)

##fig, axs = plt.subplots(2,int(len(a_0)/2), figsize=(16, 5), facecolor='w', edgecolor='k')
##fig.subplots_adjust(hspace = 0.1, wspace=0.25)
##
##axs = axs.ravel()

r = []

mg = []

mger = []

for i in range(len(a_0)):

    y = []

    x = []

    k = 0

    for j in avh:
        
        f = np.log(1 - ( j / (a_0[i]*l[k]) ) )

        y.append(f)

        x.append(np.log(l[k])) #ln(L)

        k += 1

##    axs[i].scatter(x,y)
##    axs[i].set_title('a = ' + str(a_0[i]))
##    
##    axs[i].set_xlabel('ln(L)')
##    axs[0].set_ylabel('y')
##
##    plt.title(str(i))

    x2 = np.array(x)

    y2 = np.array(y)

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

    r.append(r_value)

    mg.append(m)

    # errors on fit parameters

    p, V = np.polyfit(x2, y2, 1, cov=True)

    mger.append(np.sqrt(V[0][0]))
    
plt.rcParams.update({'font.size': 32})
plt.scatter(a_0,r, s =1)


plt.xlabel('a_0 value')

plt.ylabel('r value')

plt.title('Linear regression vs. a_0')

plt.axvline(x= a_0[r.index(max(r))] ,linestyle = '--')

# gradient at best r value

mbest = mg[r.index(max(r))]

w1 = -1*mbest

w1er = mger[r.index(max(r))]

print("w_1: {} +/- {}".format(w1, w1er))

print('a_0 = ' + str(a_0[r.index(max(r))]))

print('w1 = ' +str(w1))

plt.show()










