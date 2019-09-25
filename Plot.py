import os
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

filename = './Outputs/new_core1.out'

fdh_2d = {}
with open(filename, 'r') as search:
    lines = search.readlines()
    state_line, fdh, boron = {}, {}, {}
    EFPD = []
    counter = 0
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
        if lines[i].startswith(' Output Summary'):
            state_line[counter] = i
            EFPD.append(float(lines[i+3][86:91]))
            fdh[EFPD[counter]] = float(lines[i+12][93:98])
            boron[EFPD[counter]] = float(lines[i+14][36:43])
            counter += 1
    counter = 0
    for i in range(len(lines)):
        if lines[i].startswith(' PIN.EDT 2PIN'):
            j = 0
            fdh_2d[EFPD[counter]] = np.zeros((8,8))
            fdh_2d[EFPD[counter]] = np.full([8,8], np.nan)
            for j in range(8):
                temp = lines[i+j+3][5:59].split()
                for k in range(len(temp)):
                    fdh_2d[EFPD[counter]][j][k] = temp[k]
            counter += 1


plot = True
if plot:
    fig, ax = plt.subplots(figsize=(8,8))
    im = ax.imshow(fdh_2d[EFPD[0]], cmap='jet')
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    fig.colorbar(im, cax)
    for i in range(8):
        for j in range(8):
            if not np.isnan(fdh_2d[EFPD[0]][i, j]):
                text = ax.text(j, i, fdh_2d[EFPD[0]][i, j], ha="center", va="center", color="black")
    ax.grid(False)
    fig.tight_layout()
    plt.show()



filename2 = './Outputs/new_core1.out'
with open(filename2, 'r') as search:
    lines = search.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()

input = np.zeros((8,8))
for i in range(8):
    input[i] = lines[i+2][16:48].split()
input[input==0]='nan'
input[input==1]='nan'

plot = True
if plot:
    fig, ax = plt.subplots(figsize=(8,8))
    im = ax.imshow(input, cmap='rainbow')
    fig.colorbar(im, cax)
    for i in range(8):
        for j in range(8):
            if not np.isnan(input[i, j]):
                text = ax.text(j, i, input[i, j], ha="center", va="center", color="black")
    ax.grid(False)
    fig.tight_layout()
    plt.show()

#cmap='brg'
