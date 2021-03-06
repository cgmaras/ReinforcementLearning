import os
import numpy as np

filename = './Outputs/new_core1.out'
os.system('clear')

fdh_2d = {}
with open(filename, 'r') as search:
    lines = search.readlines()
    state_line, Fdh, boron, Fq = {}, {}, {}, {}
    counter = 0
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
        if lines[i].startswith(' Output Summary'):
            state_line[counter] = i
            counter += 1
            EFPD = float(lines[i+3][86:91])
            Fdh[EFPD] = float(lines[i+12][93:98])
            boron[EFPD] = float(lines[i+14][36:43])



index1 = 0
index2 = 0
for i in range(len(lines)):
    if lines[i].startswith(' Max. Node-Averaged  Peaking Factor'):
        Fq[list(Fdh.keys())[index1]] = float(lines[i][38:43])
        index1 += 1
    if lines[i].startswith(' PIN.EDT 2PIN'):
        j = 0
        fdh_2d[list(Fdh.keys())[index2]] = np.zeros((8,8))
        fdh_2d[list(Fdh.keys())[index2]] = np.full([8,8], np.nan)
        for j in range(8):
            temp = lines[i+j+3][5:59].split()
            for k in range(len(temp)):
                fdh_2d[list(Fdh.keys())[index2]][j][k] = temp[k]
        index2 += 1



print(' EFPD     Boron(ppm)     Fdh           Fq')
for i in list(Fdh.keys()):
    print(('%5s' + '     '  + '%6s' + '        ' + '%6s' + '        ' + '%6s') % (i, boron[i], Fdh[i], Fq[i]))

print(' ')
print(' ')
print('-------------------------- Fdh ---------------------------')


for i in list(boron.keys()):
    check = fdh_2d[i]==max(list(Fdh.values()))
    if check.any():
        break

print(fdh_2d[i])
