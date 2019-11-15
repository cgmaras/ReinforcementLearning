

-- user_input.py is where input from the user guides the code 

-- main.sh is the slurm job script for the main.py file

-- main.py is the main python file controlling the other files 
	-- InputGen.inp reads the user input and creates a local directory called Queue which it fills with input files 
	-- simulate.py is the python file for setting up simulate structure and making job scripts 

	-- Output_Search.py file is used to read output files locally that are copied over from rdfmg Sim Folder structure 
	
 
