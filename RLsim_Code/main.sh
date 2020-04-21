#!  /bin/sh
#
#PBS -N simulate
#PBS -e error.dat
#PBS -o info.dat
#PBS -p gradq
#PBS -l nodes=1:ppn=1
cd $SLURM_SUBMIT_DIR
echo $SLURM_SUBMIT_DIR
#  Make sure we're in right directory
date

echo "Starting Main job..."

python3 main.py #| tee run.log

echo "Main Job Finished"
