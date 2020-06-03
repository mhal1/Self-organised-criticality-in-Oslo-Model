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

    #count the number of piles with height h and divide by total number of
    #configs

    d = collections.Counter(ph)
    
    n, pn = np.array(list(d.keys())), np.array(list(d.values()))/(sum(list(d.values())))

    plt.rcParams.update({'font.size': 30})
    
    plt.scatter(n,pn,label = j, s=170, marker = '.')

plt.legend(loc=(0.85, 0.43), handlelength=1.0, fontsize=25)

plt.xlabel('System height')

plt.ylabel('Probability of height')

plt.xlim([0, max(n)])
plt.ylim([0, 0.5])

plt.title('Probability of heights for different L')
    
plt.show()


###### data collapse ###### ###### ###### ###### ###### ###### ###### 


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

    #count the number of piles with height h and divide by total number of
    #configs

    d = collections.Counter(ph)
    
    n, pn = np.array(list(d.keys())), np.array(list(d.values()))/(sum(list(d.values())))

    plt.rcParams.update({'font.size': 30})

    hscaled = (n - np.array([(ah/t)]*len(n)))/sdd

    #hscaled = n
    
    plt.scatter(hscaled,pn*sdd,label = j, s=100, marker = '.')

plt.legend(loc=(0.65, 0.43), handlelength=1.0, fontsize=25)

plt.xlabel('Scaled system height')


plt.ylabel('$\\sigma_hP_h$')

plt.title('Data collapse for probability of heights')
    
plt.show()







