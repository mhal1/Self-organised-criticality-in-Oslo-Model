#measure total height of pile as function of time

import numpy as np

import matplotlib.pyplot as plt

import pickle as p

import OS

l = [4, 8, 16,32,64,128,256]

M = 10


# average slope for use in theoretical calculation of critical time


real = []

za = []
    
filein =  open(f"256_9", "rb")

fl = p.load(filein)

n1 = 0

n2 = 0

for x in fl[-1][0].sites():

    if x.z_i() == 1:

        n1 += 1
        
    elif x.z_i() == 2:

        n2 += 1
        
avgz = (n1+2*n2)/256

print(avgz)

# need to average heights over realisations,
#each realisation average the height of all at each time

ha = 0

#avg height
ht = []

tth = []

tdt = []

tdn = []

za = []

for q in l:

    #for each realisation take the height at the time

    #first of all open all realisations and use the time check to be the minimum of all
    #realisations, each run will have a slightly different time so to use in loop
    #use the minimum as this will work for all

    real = []

    #open all files
    
    for k in range(M):
        
        filein =  open(f"{q}_{k}", "rb")

        real.append(p.load(filein))

    t_min = real[0][-1][3]
    
    tloop = range(int(1.5*t_min))

    for i in tloop: #each time as each entry corresponds to a time

        ha = 0

        ttc = 0
        
        for k in real:
            
            ha += k[i][1]

            ttc += k[-1][3]/M

        ht.append(ha) # avg added to list

        tth.append(i)
##
##    print('numerical critical time = ' + str(ttc))

    tdn.append(ttc)

    theory = (avgz/2)*(q**2)*(1 + (1/q))

    tdt.append(theory)

    # task 2d
##
##    print('theoretical critical time = ' + str(theory))
    
    ht.clear()

    tth.clear()


# percentage difference

pd = []

for i in range(len(l)):

    pd.append(np.abs(100*(tdn[i]-tdt[i])/tdt[i]))

plt.figure()

plt.rcParams.update({'font.size': 30})

plt.scatter(l,tdn, c = 'g', s=600, label = 'Numerical', marker = '.')

plt.scatter(l,tdt, c = 'black',s=600, label = 'Theoretical',marker = '.')

plt.xlabel('System size')

plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

plt.ylabel('Critical time')

plt.title('Critical times for systems')

plt.legend()

plt.xlim(0,270)

plt.ylim(0,max(tdt)*1.2)

plt.figure()

plt.rcParams.update({'font.size': 30})

plt.scatter(l,pd,s=600, marker = 'x')

plt.xlim(0,260)

plt.xlabel('System size')

plt.ylabel('Percentage difference')

plt.title('Percentage difference between \n theoretical and numerical critical time')

plt.show()



    
