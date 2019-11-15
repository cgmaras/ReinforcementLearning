import random
from random import choice
# --------------- Primary Input File for RL/SIMULATE Code ---------------------------------
#
#
#
## core layout
FuelMap = [8,8,7,7,6,5,4,2,0]
RefMap = [1,1,2,1,2,2,2,3,3]
BaffleMap = [0,0,0,1,1,2,3,4,6]


class Input:

    def __init__(self):
        self.base = '/home/cgmaras/Python/RLsim_Code/Base_Files/base.inp'       # Base Input File Directory
        self.lib = '/home/cgmaras/Python/RLsim_Code/Base_Files/cms.pwr-all.lib' # Fuel Repository directory
        self.res = '/home/cgmaras/Python/Base_Files/cycle1.res'                 # Initial Restart file
        self.Runs = 2                                                           # Number of SIMULATE Runs
        self.FA = 157                                                           # Core Configuration (Number of Fuel Assemblies)
        self.out = '/home/cgmaras/Python/RLsim_Code/Outputs'                    # Output File Directory


## core layout
FuelMap = [8,8,7,7,6,5,4,2,0]
RefMap = [1,1,2,1,2,2,2,3,3]
BaffleMap = [0,0,0,1,1,2,3,4,6]


#class Fuel:
#  def __init__(self, Type=None, Enrichment=None, BU=None, BP=None, Volume=None):
#    self.Type = Type                                                            # Fuel Type from Project
#    self.Enrichment = Enrichment                                                # Enrichment of FA in U235 w/o
#    self.BU = BU                                                                # Burnup
#    self.BP = BP                                                                # Number of Burnable Poison Rods
#    self.Volum = Volume                                                         # Number of FA in inventory
#    self.Flag = "2"                                                             # flag for inputgen

#Fuel_2 = Fuel(2,2.0,0,0,50)
#Fuel_3 = Fuel(3,2.5,0,0,50)
#Fuel_4 = Fuel(4,2.5,0,16,50)
#Fuel_5 = Fuel(5,3.2,0,0,50)
#Fuel_6 = Fuel(6,3.2,0,16,50)
#print(Fuel_5.Type)


Fuel_2 = {}
Fuel_3 = {}
Fuel_4 = {}
Fuel_5 = {}
Fuel_6 = {}
Fuel = {}
Fuel_2 = {'Flag': 2, 'Type': 2, 'BU': 0, 'Enrichment': 2.0, 'BP': 16, 'INV': 50}
Fuel_3 = {'Flag': 2, 'Type': 3, 'BU': 0, 'Enrichment': 2.5, 'BP': 16, 'INV': 50}
Fuel_4 = {'Flag': 2, 'Type': 4, 'BU': 0, 'Enrichment': 2.5, 'BP': 16, 'INV': 50}
Fuel_5 = {'Flag': 2, 'Type': 5, 'BU': 0, 'Enrichment': 3.2, 'BP': 16, 'INV': 50}
Fuel_6 = {'Flag': 2, 'Type': 6, 'BU': 0, 'Enrichment': 3.2, 'BP': 16, 'INV': 50}
Fuel = {'2':Fuel_2, '3':Fuel_3, '4':Fuel_4, '5':Fuel_5, '6':Fuel_6}
Types = [2,3,4,5,6]

#print(Fuel['2']['Enrichment'])

print(choice(Types))



#Reflector = ["1,9","2,9","3,8","3,9","4,8","5,7","5,8","6,6","6,7","7,5","7,6","8,3","8,4","8,5","9,1","9,2","9,3"]
#Baffle = ["4,9","5,9","6,9","7,9","8,9","9,9","9,4","9,5","9,6","9,7","9,8","8,6","8,7","8,8","7,7","7,8","6,8"]
#LP = [{'1,1': {'Flag': 2, 'Fuel Type': 4, 'BU': 0, 'Enrichment': 2.5, 'BP': 16}, '1,2': {'Flag': 2, 'Fuel Type': 4, 'BU': 0, 'Enrichment': 2.5, 'BP': 16}, '1,3': {'Flag': 2, 'Fuel Type': 6, 'BU': 0, 'Enrichment': 3.2, 'BP': 16}, '1,4': {'Flag': 2, 'Fuel Type': 3, 'BU': 0, 'Enrichment': 2.5, 'BP': 0}, '1,5': {'Flag': 2, 'Fuel Type': 5, 'BU': 0, 'Enrichment': 3.2, 'BP': 0}, '1,6': {'Flag': 2, 'Fuel Type': 6, 'BU': 0, 'Enrichment': 3.2, 'BP': 16}, '1,7': {'Flag': 2, 'Fuel Type': 6, 'BU': 0, 'Enrichment': 3.2, 'BP': 16}, '1,8': {'Flag': 2, 'Fuel Type': 3, 'BU': 0, 'Enrichment': 2.5, 'BP': 0}, '1,9': {'Flag': 1, 'Fuel Type': 1, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '2,1': {'Flag': 2, 'Fuel Type': 5, 'BU': 0, 'Enrichment': 3.2, 'BP': 0}, '2,2': {'Flag': 2, 'Fuel Type': 6, 'BU': 0, 'Enrichment': 3.2, 'BP': 16}, '2,3': {'Flag': 2, 'Fuel Type': 6, 'BU': 0, 'Enrichment': 3.2, 'BP': 16}, '2,4': {'Flag': 2, 'Fuel Type': 6, 'BU': 0, 'Enrichment': 3.2, 'BP': 16}, '2,5': {'Flag': 2, 'Fuel Type': 2, 'BU': 0, 'Enrichment': 2.0, 'BP': 0}, '2,6': {'Flag': 2, 'Fuel Type': 2, 'BU': 0, 'Enrichment': 2.0, 'BP': 0}, '2,7': {'Flag': 2, 'Fuel Type': 2, 'BU': 0, 'Enrichment': 2.0, 'BP': 0}, '2,8': {'Flag': 2, 'Fuel Type': 5, 'BU': 0, 'Enrichment': 3.2, 'BP': 0}, '2,9': {'Flag': 1, 'Fuel Type': 1, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '3,1': {'Flag': 2, 'Fuel Type': 2, 'BU': 0, 'Enrichment': 2.0, 'BP': 0}, '3,2': {'Flag': 2, 'Fuel Type': 6, 'BU': 0, 'Enrichment': 3.2, 'BP': 16}, '3,3': {'Flag': 2, 'Fuel Type': 4, 'BU': 0, 'Enrichment': 2.5, 'BP': 16}, '3,4': {'Flag': 2, 'Fuel Type': 5, 'BU': 0, 'Enrichment': 3.2, 'BP': 0}, '3,5': {'Flag': 2, 'Fuel Type': 3, 'BU': 0, 'Enrichment': 2.5, 'BP': 0}, '3,6': {'Flag': 2, 'Fuel Type': 2, 'BU': 0, 'Enrichment': 2.0, 'BP': 0}, '3,7': {'Flag': 2, 'Fuel Type': 6, 'BU': 0, 'Enrichment': 3.2, 'BP': 16}, '3,8': {'Flag': 1, 'Fuel Type': 1, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '3,9': {'Flag': 1, 'Fuel Type': 1, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '4,1': {'Flag': 2, 'Fuel Type': 4, 'BU': 0, 'Enrichment': 2.5, 'BP': 16}, '4,2': {'Flag': 2, 'Fuel Type': 6, 'BU': 0, 'Enrichment': 3.2, 'BP': 16}, '4,3': {'Flag': 2, 'Fuel Type': 6, 'BU': 0, 'Enrichment': 3.2, 'BP': 16}, '4,4': {'Flag': 2, 'Fuel Type': 2, 'BU': 0, 'Enrichment': 2.0, 'BP': 0}, '4,5': {'Flag': 2, 'Fuel Type': 6, 'BU': 0, 'Enrichment': 3.2, 'BP': 16}, '4,6': {'Flag': 2, 'Fuel Type': 4, 'BU': 0, 'Enrichment': 2.5, 'BP': 16}, '4,7': {'Flag': 2, 'Fuel Type': 4, 'BU': 0, 'Enrichment': 2.5, 'BP': 16}, '4,8': {'Flag': 1, 'Fuel Type': 1, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '4,9': {'Flag': 0, 'Fuel Type': 0, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '5,1': {'Flag': 2, 'Fuel Type': 2, 'BU': 0, 'Enrichment': 2.0, 'BP': 0}, '5,2': {'Flag': 2, 'Fuel Type': 3, 'BU': 0, 'Enrichment': 2.5, 'BP': 0}, '5,3': {'Flag': 2, 'Fuel Type': 5, 'BU': 0, 'Enrichment': 3.2, 'BP': 0}, '5,4': {'Flag': 2, 'Fuel Type': 5, 'BU': 0, 'Enrichment': 3.2, 'BP': 0}, '5,5': {'Flag': 2, 'Fuel Type': 3, 'BU': 0, 'Enrichment': 2.5, 'BP': 0}, '5,6': {'Flag': 2, 'Fuel Type': 3, 'BU': 0, 'Enrichment': 2.5, 'BP': 0}, '5,7': {'Flag': 1, 'Fuel Type': 1, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '5,8': {'Flag': 1, 'Fuel Type': 1, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '5,9': {'Flag': 0, 'Fuel Type': 0, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '6,1': {'Flag': 2, 'Fuel Type': 5, 'BU': 0, 'Enrichment': 3.2, 'BP': 0}, '6,2': {'Flag': 2, 'Fuel Type': 5, 'BU': 0, 'Enrichment': 3.2, 'BP': 0}, '6,3': {'Flag': 2, 'Fuel Type': 3, 'BU': 0, 'Enrichment': 2.5, 'BP': 0}, '6,4': {'Flag': 2, 'Fuel Type': 5, 'BU': 0, 'Enrichment': 3.2, 'BP': 0}, '6,5': {'Flag': 2, 'Fuel Type': 6, 'BU': 0, 'Enrichment': 3.2, 'BP': 16}, '6,6': {'Flag': 1, 'Fuel Type': 1, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '6,7': {'Flag': 1, 'Fuel Type': 1, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '6,8': {'Flag': 0, 'Fuel Type': 0, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '6,9': {'Flag': 0, 'Fuel Type': 0, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '7,1': {'Flag': 2, 'Fuel Type': 4, 'BU': 0, 'Enrichment': 2.5, 'BP': 16}, '7,2': {'Flag': 2, 'Fuel Type': 3, 'BU': 0, 'Enrichment': 2.5, 'BP': 0}, '7,3': {'Flag': 2, 'Fuel Type': 5, 'BU': 0, 'Enrichment': 3.2, 'BP': 0}, '7,4': {'Flag': 2, 'Fuel Type': 6, 'BU': 0, 'Enrichment': 3.2, 'BP': 16}, '7,5': {'Flag': 1, 'Fuel Type': 1, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '7,6': {'Flag': 1, 'Fuel Type': 1, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '7,7': {'Flag': 0, 'Fuel Type': 0, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '7,8': {'Flag': 0, 'Fuel Type': 0, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '7,9': {'Flag': 0, 'Fuel Type': 0, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '8,1': {'Flag': 2, 'Fuel Type': 4, 'BU': 0, 'Enrichment': 2.5, 'BP': 16}, '8,2': {'Flag': 2, 'Fuel Type': 2, 'BU': 0, 'Enrichment': 2.0, 'BP': 0}, '8,3': {'Flag': 1, 'Fuel Type': 1, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '8,4': {'Flag': 1, 'Fuel Type': 1, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '8,5': {'Flag': 1, 'Fuel Type': 1, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '8,6': {'Flag': 0, 'Fuel Type': 0, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '8,7': {'Flag': 0, 'Fuel Type': 0, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '8,8': {'Flag': 0, 'Fuel Type': 0, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '8,9': {'Flag': 0, 'Fuel Type': 0, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '9,1': {'Flag': 1, 'Fuel Type': 1, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '9,2': {'Flag': 1, 'Fuel Type': 1, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '9,3': {'Flag': 1, 'Fuel Type': 1, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '9,4': {'Flag': 0, 'Fuel Type': 0, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '9,5': {'Flag': 0, 'Fuel Type': 0, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '9,6': {'Flag': 0, 'Fuel Type': 0, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '9,7': {'Flag': 0, 'Fuel Type': 0, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '9,8': {'Flag': 0, 'Fuel Type': 0, 'BU': 0, 'Enrichment': 0, 'BP': 0}, '9,9': {'Flag': 0, 'Fuel Type': 0, 'BU': 0, 'Enrichment': 0, 'BP': 0}}]
