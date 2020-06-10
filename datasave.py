#measure total height of pile as function of time

import numpy as np

import matplotlib.pyplot as plt

import pickle as p

import OS

L = [4, 8, 16, 32, 64, 128, 256] #,512]

#run M times for each system size n save each system size in a different file
# use f strings
# pickle to save and read
# only save up to about 1 or 2 times the critial time

N = 100000

M = 10

realisations = []

# to reach steady state N ~ L^2, need N = 270,000 for L = 512

p1 = 0.5
p2 = 0.5

for l in L:

    for jg in range(M): # the number of realisations

        #open a file named l

        fileout = open(f"{l}_{jg}","wb")
    
        i = 0

        h1 = []

        t = []

        tc = []

        sandbox = OS.box(l, N, p1,p2)

        while i <= N:

            #drive

            sandbox.drive()

            sandbox.relax()

            tt = i
            
            if sandbox.steady() == True:

                tc.append(i)

                tcr = tc[0]
                
                #set it to run until 1 or 2 mor t_cs?
                #if i >= 3*tc[0]:
                    
                    #i = N + 1
            else:

                tcr = ''

            #saves as box object, height, time, crit time, realisation, avalanche size

            realisations.append([sandbox,sandbox.sites()[0].height(),tt,tcr,jg,sandbox.s()])

            i += 1           

        p.dump(realisations, fileout)

        realisations.clear()

        fileout.close()

        print('done: ' + f"{l}_{jg}" )
