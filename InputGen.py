import numpy as np

# with open('New_Input', 'w') as f1:
# 	with open('workymcworker.inp', 'r+') as f:
# 		contents = f.readlines()
# 		for x in contents:
# 			print(x)
# 		f1.writelines(contents)

filename2 = 'base.inp'
with open(filename2, 'r') as search:
    lines = search.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()





loading = {'core1':2, 'core2':6,'core3':3,'core4':4}
for core in list(loading.keys()):
	input = np.zeros((9,9))
	for i in range(9):
	    input[i] = lines[i+2][16:49].split()

	for i in range(2,8):
		input[input==i]=loading[core]

	# converting input array to strings for building new input file
	input_string = {}
	for i in range(9):
		input_string[i] = ''
		for j in range(9):
			input_string[i] += (str(int(input[i,j])) + '   ')
		input_string[i] = input_string[i][:-3]


	with open('./Core Queue/new_' + core + '.inp', 'w') as f:
		for i in range(2):
			f.writelines(lines[i] + '\n')
		for i in range(9):
			f.writelines('\'FUE.TYP\'  '+ str(i+1) +',   ' + input_string[i] + '/' + '\n')
		for i in range(11,20):
			f.writelines(lines[i] + '\n')
