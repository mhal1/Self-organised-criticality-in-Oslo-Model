import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import logbin as lb

import interpolation as inter

import numpy as np

import pickle as p
 
plt.ion()

fig = plt.figure()

ax = fig.add_subplot(111)

l = [4,8,16,32,64,128,256]

for j in l:
    
    filein =  open(f"{j}_0", "rb")

    sandbox = p.load(filein)

    s = []

    sp = []

    for i in sandbox:

        if i[3] != '': # only adds after t >t_c

            s.append(i[-1])
            
    pr = lb.logbin(s, scale = 1.55) # contains x and y, x in coord, y is prob

    sp = (pr[0]**1)*pr[1]# gives sP(s,L) for data collapse part 3b

    plt.loglog(pr[0]/j**1,sp, label = j)#pr[0]/(j**2.25),sp, label = j)

    
    'line + str(j),' = ax.plot(x, y, 'b-')

    #plt.scatter(np.log(pr[0]/j**2.08),np.log(sp), label = j, s = 3)

    #plt.plot(np.log(pr[0]/j**2.2),np.log(sp), label = j)
    
    #tau_s = 1.55, D = 2.25plt.legend()


for phase in np.linspace(0, 10*np.pi, 100):

    plt.pause(0.1)
    
    line1.set_ydata(np.sin(0.5 * x + phase))

    plt.pause(0.1)
    
    fig.canvas.draw()

    plt.pause(0.1)
