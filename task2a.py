#measure total height of pile as function of time

import numpy as np

import matplotlib.pyplot as plt

import pickle as p

L = [4, 8, 16, 32, 64, 128, 256]

fig = plt.figure()

ax = plt.subplot(111)

font = {'size'   : 22}

plt.rc('font', **font)

for l in L:

    h1 = []

    t = []
    
    filein =  open(f"{l}_0", "rb")

    sandbox = p.load(filein)

    for i in sandbox:

        h1.append(i[1])

        t.append(i[2])

    ax.scatter(t,h1,label = l, s = 0.05)
    
# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.95, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

ax.set_xlabel('Number of grains added (scale * 10^5)')

ax.set_ylabel('Height of pile')

ax.set_title('Heights of sand piles')

for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
              ax.get_xticklabels() + ax.get_yticklabels()):
    item.set_fontsize(32)
    
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.xlim(0,max(t))
plt.ylim(0,500)
plt.show()
