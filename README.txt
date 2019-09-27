
InputGen.inp reads the base.inp file and creates a local directory called Queue which it fills with input files 



-- Sim Folder - to be put in RDFMG folder for running simulate
	- simulate.sh is the shell command for submitting simulate
	- Any new input files generated locally are copied over to rdfmg Queue folder



Plot.py and Output_Search.py files are used to read output files locally that are copied over from rdfmg Sim Folder structure 
	- create local directory called Outputs and copy in .out files from simulate runs
 
