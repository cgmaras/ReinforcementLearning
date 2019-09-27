#!  /bin/sh
#
#PBS -N simulate
#PBS -e error.dat
#PBS -o info.dat
#PBS -q shortq
#PBS -l nodes=1:ppn=1

#  Make sure we're in right directory
cd /home/cgmaras/Python
date
rm project.out

echo "starting job..."

ls

FILES=/home/cgmaras/Python/Queue/*
for f in $FILES
do

    fname="${f##*/}"
    name=${fname%.*} 
    echo $name
    mkdir -p /home/cgmaras/Python/Runs/$name
    cd /home/cgmaras/Python/Runs/$name
    cp /home/cgmaras/Python/Base_Files/s3_init.inp /home/cgmaras/Python/Runs/$name
    cp /home/cgmaras/Python/Base_Files/cycle1.res /home/cgmaras/Python/Runs/$name
    cp /home/cgmaras/Python/Base_Files/cms.pwr-all.lib /home/cgmaras/Python/Runs/$name
    cp /home/cgmaras/Python/Runs/$name/$name.out /home/cgmaras/Python/Outputs
    rm /home/cgmaras/Python/Runs/$name/$name.out
    simulate3 $f
  
done

