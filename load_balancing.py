import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import random


qd = [10 * i for i in range(10)]

loops = 10000

max_loading = []
loop_max = []


for qdx in qd:

    prob = [0 for i in range(8)]
    loop_max = []
    for idx in range(loops):

        cmd = [int(8 * random.random()) for i in range(qdx)]

        for i in range(len(cmd)):
            prob[cmd[i]] += 1

        max_load = max(prob)
        #print('%.5f' % max_load)
        prob = [0 for i in range(8)]

        loop_max.append(max_load)

    max_loading.append(max(loop_max))


plt.figure()
plt.plot(qd, max_loading)
plt.show()

print(max_loading)
