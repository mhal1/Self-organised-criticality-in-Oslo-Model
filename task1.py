#oslo model

import numpy as np

import matplotlib.pyplot as plt

import OS

#selecting z_i threshold wwith probability 0.5
#produces an array of threshold slopes {1,2} p = 0.5
#all sites i have a defined threshold

#loop for driving and realxing

L = 16

N = 4000

#test 1: check time average of L = 16 is 26.5

#test 2: check time average of L = 32 is 53.9

p1 = 0.5
p2 = 0.5

for l in [16, 32]:

    i = 0

    tc = []

    h1 = []

    t = []

    sandbox = OS.box(l, N, p1,p2)
    
    while i <= N:

        #drive

        sandbox.drive()

        sandbox.relax()

        if sandbox.steady() == True:

            h = 0
            
            tc.append(i)

            for k in sandbox.sites():

                h += k.z_i()
            
            h1.append(h)

            t.append(i)

        i += 1
        
    print('')

    print('For threshold probability = 0.5 and L = ' + str(l) + ':')
    
    print('Average height over time = '+str(np.sum(h1)/len(t)) )

    #plt.scatter(t,h1, s = 2)

    #plt.show()

#test 3: check that the height is L for p=1 for z_ith = 1 -> all slopes should be 1 at steady state (when last site is relaxed) this is due to h = L <z>

for l in [16, 32]:

    i = 0

    tc = []

    h1 = []

    hh = []

    t = []

    z = 'box' + str(l)

    z = OS.box(L=l, N=N, p1=1,p2=0)
    
    while i <= N:

        #drive

        z.drive()

        z.relax()

        if z.steady() == True:

            h = 0
            
            tc.append(i)

            for k in z.sites():

                h += k.z_i()

            h1.append(h)

            t.append(i)

        i += 1

    for k in z.sites():

        hh.append(k.height())
        
    print('')
    
    print('For L = ' + str(l) + ' and probability = 1 of z threshold = 1:')

    print('Sum of heights = '+str(np.sum(hh)) )
    
    print('Critical time = ' + str(tc[0]))
    
    print('Height = '+str(h1[0]) )

    if tc[0] == np.sum(hh):

        print('Critical time is equal to the sum of heights of each site as expected.')

#test 4: check 2L for p=1 for z_ith = 2. this is due to h = L <z>

for l in [16, 32]:

    i = 0

    tc = []

    h1 = []

    hh =  []

    t = []

    z = 'box' + str(l)

    z = OS.box(L=l, N=N, p1=0,p2=1)
    
    while i <= N:

        #drive

        z.drive()

        z.relax()

        if z.steady() == True:

            h = 0
            
            tc.append(i)

            for k in z.sites():

                h += k.z_i()

            h1.append(h)

            t.append(i)

        i += 1

    for k in z.sites():

        hh.append(k.height())
        
    print('')
    
    print('For L = ' + str(l) + ' and probability = 1 of z threshold = 2:')

    print('Height = '+str(h1[0]) )

    print('Sum of heights = '+str(np.sum(hh)) )
    
    print('Critical time = ' + str(tc[0]))

    if tc[0] == np.sum(hh):

        print('Critical time is equal to the sum of heights of each site as expected.')


#test 5: t_critical should be the sum of the heights as this will give the number of grains in the pile


#--------------------------------------------------------------------------------

#this gives plot of sand pile visually

#hh = []

#for j in sandbox.sites():

#    hh.append(j.height())
    

#print('tc = ' + str(tc[0]))

#print('sum heights = ' + str(np.sum(hh)))

#plt.scatter(range(1,L+1),hh)

#plt.show()

#--------------------------------------------------------------------------------



    




    
