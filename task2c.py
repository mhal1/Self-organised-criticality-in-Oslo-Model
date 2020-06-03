#measure total height of pile as function of time

import numpy as np

import matplotlib.pyplot as plt

import pickle as p

import OS

l = [4, 8, 16,32,64,128,256]

M = 10

# need to average heights over realisations,
#each realisation average the height of all at each time

ha = 0

#avg height
ht = []

tth = []

tdt = []

tdn = []

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

    #t_min = real[0][-1][3]
    
    tloop = range(0,100000,1)#range(int(1.5*t_min))

    for i in tloop: #each time as each entry corresponds to a time

        ha = 0

        ttc = 0
        
        for k in real:
            
            ha += k[i][1]/M

            ttc += k[-1][3]/M

        ht.append(ha) # avg added to list

        tth.append(i)

    #data collapse dividing by system size and time by critical time


    #plt.plot(np.array(tth)/ttc,np.array(ht)/q,label = q)#,s=1)


    ht[0] = 0 # forgot to add initial sandbox when saving data
    
    plt.rcParams.update({'font.size': 32})
    
    plt.loglog(np.array(tth)/q**2,np.array(ht)/q,label = q)
    
    print('done')
    
    ht.clear()

    tth.clear()
plt.rcParams.update({'font.size': 20})
plt.legend()
plt.rcParams.update({'font.size': 32})
plt.xlabel('Number of grains added/$L^2$')

plt.ylabel('Height of pile')

plt.title('Pile heights vs time scaled by $L^2$')

plt.axvline(x=1,linestyle = '--')

plt.show()


