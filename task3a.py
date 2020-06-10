import logbin as lb

import numpy as np

import matplotlib.pyplot as plt

import pickle as p

import interpolation as inter

# avalanche size is the number of topples which happen before next grain is
# added

# only measure after critical time is reached
plota = False

plotb = True

if plota == True:

    l = [256]
    
else:

    l = [4,8,16,32,64,128,256]

for j in l:
    
    filein =  open(f"{j}_0", "rb")

    sandbox = p.load(filein)

    s = []

    sp = []

    for i in sandbox:

        if i[3] != '':

            s.append(i[-1])

    pr = lb.logbin(s, scale = 1.6) # contains x and y, x in coord, y is prob

    p2 = lb.logbin(s, scale = 1.) # no scaling of bins 

    ###################################################################################

    # a values testing

    if plota == True:

        a = np.arange(1.1,2,0.25)

        plt.rcParams.update({'font.size': 27})

        fig, axs = plt.subplots(2,2, figsize=(20, 8), facecolor='w', edgecolor='k')
        fig.subplots_adjust(hspace = 0.7, wspace=0.5)

        axs = axs.ravel()

        j = 0
        
        for i in range(len(a)):
            axs[i].scatter(np.log(lb.logbin(s, scale = a[i])[0]),np.log(lb.logbin(s, scale = a[i])[1]),s =90)
            axs[i].set_title('a = ' + str(a[i]))
            axs[i].set_xlabel('Ln(N)')
            axs[i].set_ylabel('Ln(P)')
            j+=1
                          
    ###################################################################################

        print('done')

    elif plotb == True:
    
        #plt.scatter(np.log(pr[0]),np.log(pr[1]), label = j,s =3)

        plt.rcParams.update({'font.size': 32})

        #plt.loglog(pr[0],pr[1], label = j)#,s =1)

        a = inter.interp(np.log(pr[0]),np.log(pr[1]))

        plt.rcParams.update({'font.size': 32})

        plt.scatter(a[0],a[1], s = 1,c = 'black')

        plt.scatter(np.log(pr[0]),np.log(pr[1]),s=100 , label = j)

        #plt.scatter(np.log(p2[0]),np.log(p2[1]), s =1, label = 'No scaling (a = 1)')

        plt.xlabel('ln(Avalanche size s)')

        plt.ylabel('ln(Probability of avalanche s)')

        plt.title('Probabilities of avalanche s for different L')

        plt.legend()

        print('done')

plt.show()
