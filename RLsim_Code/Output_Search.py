import os
import numpy as np
import time
import user_input
from user_input import Input
import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import math
dummy = Input()

def output():
    folder = './SimRuns'
    os.makedirs('Outputs')
    filename3 = './user_input.py'
    out = dummy.out
    print('Starting Delay')
    time.sleep(5)
    print('Ending Delay')
    should_restart = True
    while should_restart:
        for file in os.listdir(folder):
            should_restart = False
            if not os.path.isfile(os.path.join(folder,file,'PINPOW')):
                time.sleep(5)
                os.system('cp '+ os.path.join(folder,file,file+'.out') + ' ' + out)
            if os.path.isfile(os.path.join(folder,file,'PINPOW')):
                should_restart = True
                break



    filenames = os.listdir(out)

    #print(filenames)
    os.chdir(out)
    for filename in filenames:
        #filename = './Outputs/new_core1.out'
        print('\n')
        print(filename)


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
            if lines[i].startswith(' Output Summary'):
                Fq[sorted(list(Fdh.keys()))[index1]] = float(lines[i+14][93:98])
                index1 += 1
            if lines[i].startswith(' PIN.EDT 2PIN'):
                j = 0
                fdh_2d[sorted(list(Fdh.keys()))[index2]] = np.zeros((9,8))
                fdh_2d[sorted(list(Fdh.keys()))[index2]] = np.full([8,8], np.nan)
                for j in range(8):
                    temp = lines[i+j+3][5:59].split()
                    for k in range(len(temp)):
                        fdh_2d[sorted(list(Fdh.keys()))[index2]][j][k] = temp[k]
                index2 += 1


        print(' EFPD     Boron(ppm)     Fdh           Fq')
        for i in sorted(list(Fdh.keys())):
            print(('%5s' + '     '  + '%6s' + '        ' + '%6s' + '        ' + '%6s') % (i, boron[i], Fdh[i], Fq[i]))

        print(' ')
        print(' ')
        print('-------------------------- Fdh ---------------------------')


        for i in list(boron.keys()):
            check = fdh_2d[i]==max(list(Fdh.values()))
            if check.any():
                break

        print(fdh_2d[i])
        print(' ')
        print(' ')
    ################################# Second test ###############################
        statepoints = 0
        f =  open(filename,'r')
        line = f.readline()

        while line:
        	line = f.readline()
        	if 'Output Summary' in line:
        		statepoints += 1

        f.close()

        exp_avg = np.zeros(statepoints)   # GWd/MTU
        exp_cor = np.zeros(statepoints) # EFPD, GWd/MTU
        fdh     = np.zeros(statepoints)   #
        fq 		= np.zeros(statepoints)
        nodal 	= np.zeros(statepoints)
        boron	= np.zeros(statepoints)   # ppm

        # Parsing script for different variables
        f =  open(filename,'r')
        line = f.readline()

        n = -1
        while line:
        	line = f.readline()
        	if 'Output Summary' in line:
        		n = n + 1

        		f.readline()						  # 1
        		exp_avg[n] = f.readline().split()[18] # 2
        		exp_cor[n] = f.readline().split()[13]

        		for i in range(6):
        			f.readline()
        		nodal[n]      = f.readline().split()[13]
        		f.readline()
        		fdh[n]     = f.readline().split()[9]
        		f.readline()
        		boron[n]   = f.readline().split()[12]
        f.close()

        f =  open(filename,'r')
        line = f.readline()

        n = -1
        while line:
        	line = f.readline()
        	if 'Output Summary' in line:
        		n = n + 1

        		f.readline()						  # 1
        		exp_avg[n] = f.readline().split()[18] # 2
        		exp_cor[n] = f.readline().split()[13]

        		for i in range(6):
        			f.readline()
        		nodal[n]      = f.readline().split()[13]
        		f.readline()
        		fdh[n]     = f.readline().split()[9]
        		f.readline()
        		fq[n]   = f.readline().split()[15]


        print(exp_avg)
        print(exp_cor)
        print(nodal)
        print(fq)
        print(fdh)
        print(boron)
        print
        print
        fq_max = np.amax(fq)
        fdh_max = np.amax(fdh)
        boron_max = np.amax(boron)
        print(fq_max)
        print(fdh_max)
        print(boron_max)
        f.close()

        pdf_title = filename + '.pdf'
        n = 6
        with PdfPages(pdf_title) as pdf:
        	plt.rc('text',usetex=True)
        	plt.figure(figsize = (n,n))
        	plt.plot(exp_cor,fq,'r-o')
        	plt.title('Power Peaking over Cycle Length \n Max Value = %f' %np.amax(fq))
        	plt.xlabel('Exposure [EFPD]')
        	plt.ylabel('Power Peaking')
        	pdf.savefig()
        	plt.close

        	plt.rc('text',usetex=True)
        	plt.figure(figsize = (n,n))
        	plt.plot(exp_cor,fdh,'r-o')
        	plt.title('Radial Peaking over Cycle Length \n Max Value = %f' %np.amax(fdh))
        	plt.xlabel('Exposure [EFPD]')
        	plt.ylabel('F-delta-H')
        	pdf.savefig()
        	plt.close

        	plt.rc('text',usetex=True)
        	plt.figure(figsize = (n,n))
        	plt.plot(exp_cor,boron,'r-o')
        	plt.title('Critical Boron over Cycle Length \n Max Value = %f' %np.amax(boron))
        	plt.xlabel('Exposure [EFPD]')
        	plt.ylabel('Boron Concentration [ppm]')
        	pdf.savefig()
        	plt.close

        	plt.rc('text',usetex=True)
        	plt.figure(figsize = (n,n))
        	plt.plot(exp_cor,exp_avg,'r-o')
        	plt.title('Average Burnup over Cycle Length \n Max Value = %f' %np.amax(exp_cor))
        	plt.xlabel('Exposure [EFPD]')
        	plt.ylabel('Core Average Burnup [GWd/MTU]')
        	pdf.savefig()
        	plt.close

        	#set file metadata
        	d = pdf.infodict()
        	d['Title'] = 'SIMULATE Output Summary'
        	d['Author'] = 'Cameron Maras'
        	d['Subject'] = 'Reinforcement Learning in LP Optimization'
        	d['CreationDate'] = datetime.datetime(2020,1,30)














output()
