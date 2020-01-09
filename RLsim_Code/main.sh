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

echo "Starting Main job..."

<<<<<<< HEAD
python3 main.py #| tee run.log
=======
python3 main.py | tee run.log
>>>>>>> 648ac38863c9caf1cd70df48210cfdadc9b4cb20

echo "Main Job Finished"
