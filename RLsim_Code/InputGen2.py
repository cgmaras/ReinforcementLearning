import numpy as np
import os
import random

# with open('new_input', 'w') as f1:
# 	with open('workymcworker.inp', 'r+') as f:
# 		contents = f.readlines()
# 		for x in contents:
# 			print(x)
# 		f1.writelines(contents)
filename3 = '/home/cgmaras/Python/RLsim_Code/user_input.py'
os.makedirs('Queue')
with open(filename3) as f:
    for i in range(6):
        line = f.readline();
        Runs = line
with open(filename3) as f:
    for i in range(18):
        line2 = f.readline();
        filename2 = line2.strip('\n')


with open(filename2) as search:
    lines = search.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()

# reflector and baffle positions
Reflector = ["1,9","2,9","3,8","3,9","4,8","5,7","5,8","6,6","6,7","7,5","7,6","8,3","8,4","8,5","9,1","9,2","9,3"]
Baffle = ["4,9","5,9","6,9","7,9","8,9","9,9","9,4","9,5","9,6","9,7","9,8","8,6","8,7","8,8","7,7","7,8","6,8"]

# creating dictionaries for each position in core
main, row = {}, {}
x = int(Runs)                                               # number of different LPs to be made
for k in range(x):
    for i in range(1,10):
        for j in range(1,10):
            name = str(i) + "," + str(j)
            main[name] = {}
            if name in Reflector:                   # using flag to determine fuel, reflector, or baffle
                main[name]['Flag'] = 1
            elif name in Baffle:
                main[name]['Flag'] = 0
            else:
                main[name]['Flag'] = 2

            if main[name]['Flag'] == 2:
                main[name]['Fuel Type'] = random.randint(2,6)           # fuel type based on 412/512 project description, using random dist for now
                main[name]['BU'] = 0                                    # assembly averaged burnup (MWD/MTU)
                if main[name]['Fuel Type'] == 2:
                    main[name]['Enrichment'] = 2.0                          # assembly averaged enrichment (u235 w/o)
                    main[name]['BP'] = 0                                    # number of burnable poison rods in assembly
                elif main[name]['Fuel Type'] == 3:
                    main[name]['Enrichment'] = 2.5
                    main[name]['BP'] = 0
                elif main[name]['Fuel Type'] == 4:
                    main[name]['Enrichment'] = 2.5
                    main[name]['BP'] = 16
                elif main[name]['Fuel Type'] == 5:
                    main[name]['Enrichment'] = 3.2
                    main[name]['BP'] = 0
                else:
                    main[name]['Enrichment'] = 3.2
                    main[name]['BP'] = 16
            elif main[name]['Flag'] == 1:
                main[name]['Fuel Type'] = 1
                main[name]['BU'] = 0
                main[name]['Enrichment'] = 0
                main[name]['BP'] = 0
            else:
                main[name]['Fuel Type'] = 0
                main[name]['BU'] = 0                # non-fuel filling with zeros
                main[name]['Enrichment'] = 0
                main[name]['BP'] = 0
        # print(main)
        row[i] = '\'FUE.TYP\'  '+ str(i) +',   '
        for j in range(1,10):
            row[i] += str(main[str(i) + "," + str(j)]['Fuel Type']) + '   '
        row[i] = row[i][:-3] + '/' + '\n'

    with open('/home/cgmaras/Python/RLsim_Code/Queue/new_core' + str(k+1) + '.inp', 'w') as f:
    	for i in range(2):
    		f.writelines(lines[i] + '\n')
    	for i in range(1,10):
    		f.writelines(row[i])
    	for i in range(11,20):
    		f.writelines(lines[i] + '\n')

main

###############################################################################
# above needs to be pulled and used to write like below
###############################################################################

# reading SIMULATE base input file
# filename2 = 'C:/Users/cgmaras/Desktop/Python/base.inp'
# with open(filename2, 'r') as search:
#     lines = search.readlines()
#     for i in range(len(lines)):
#         lines[i] = lines[i].rstrip()
#
# # creating core LP map
# loading = {'core1':2, 'core2':6,'core3':3,'core4':4}
# print(list(loading.keys()))
# for core in list(loading.keys()):
# 	input = np.zeros((9,9))
# 	for i in range(9):
# 	    input[i] = lines[i+2][16:49].split()
#
# 	for i in range(2,8):
# 		input[input==i]=loading[core]
#
# # converting input array to strings for building new input file
# 	input_string = {}
# 	for i in range(9):
# 		input_string[i] = ''
# 		for j in range(9):
# 			input_string[i] += (str(int(input[i,j])) + '   ')
# 		input_string[i] = input_string[i][:-3]
#
# # writing new SIMULATE input files
# 	with open('C:/Users/cgmaras/Desktop/Python/Core Queue/new_' + core + '.inp', 'w') as f:
# 		for i in range(2):
# 			f.writelines(lines[i] + '\n')
# 		for i in range(9):
# 			f.writelines('\'FUE.TYP\'  '+ str(i+1) +',   ' + input_string[i] + '/' + '\n')
# 		for i in range(11,20):
# 			f.writelines(lines[i] + '\n'
