#!  /bin/sh
#
#PBS -N simulate
#PBS -e error.dat
#PBS -o info.dat
#PBS -q shortq
#PBS -l nodes=1:ppn=1
cd $SLURM_SUBMIT_DIR
echo $SLURM_SUBMIT_DIR
#  Make sure we're in right directory
date

echo "starting job..."

simulate3 /home/cgmaras/Python/RLsim_Code/SimRuns/new_core10/new_core10.inp   
echo Job Finished