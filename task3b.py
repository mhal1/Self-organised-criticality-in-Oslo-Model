import logbin as lb

import interpolation as inter

import numpy as np

import matplotlib.pyplot as plt

import pickle as p

l = [32,64,128,256]

# avalanche size is the number of topples which happen before next grain is
# added

# only measure after critical time is reached

for j in l:
    
    filein =  open(f"{j}_0", "rb")

    sandbox = p.load(filein)

    s = []

    sp = []

    for i in sandbox:

        if i[3] != '': # only adds after t >t_c

            s.append(i[-1])
            
    pr = lb.logbin(s, scale = 1.8) # contains x and y, x in coord, y is prob

    D = 1#2.235

    t_s = 1.561

    sp = (pr[0]**t_s)*pr[1]# gives sP(s,L) for data collapse part 3b

##    plt.loglog(pr[0]/j**D,sp, label = j)#pr[0]/(j**2.25),sp, label = j)
##
##    plt.scatter(pr[0]/j**D,sp, label = j, s = 10)

    a = inter.interp(np.log(pr[0]/j**D),np.log(sp))

    plt.rcParams.update({'font.size': 32})

    plt.scatter(a[0],a[1], s = 10)

    plt.rcParams.update({'font.size': 32})

    plt.scatter(np.log(pr[0]/j**D),np.log(sp), label = j, s = 100)

    #plt.plot(np.log(pr[0]/j**2.2),np.log(sp), label = j)
    
    #tau_s = 1.55, D = 2.25

plt.legend()

plt.title('Data collapse for $P_N$')

plt.xlabel('ln($sL^{-' + str(D) + '}}$)')

plt.ylabel('ln($s^{' + str(t_s) + '}P_N$)')

plt.show()

