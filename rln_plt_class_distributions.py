"""

Plot the particle distribution between classes as a function of refinement iteration for a series of star files.
--> This may benefit from an iteration class? Because we will be looking at multiple iterations worth of data? Not sure yet

"""

import rln_starparser
from matplotlib import pyplot as plt
import numpy as np
from sys import argv

def iteration(star: list) -> int:
    # Return the iteration number for the starfile
    pass

def bin(class_numbers) -> dict:
    
    # Return the total number of particles per class as a dict
    
    particle_numbers = dict()
    for i in range(1, (int(max(class_numbers))+1), 1):
        particle_numbers[f'class {i}'] = 0
    
    for particle in class_numbers:
        particle_numbers[f'class {particle}'] += 1

    return particle_numbers

def plot():
    # Plot the data as a line graph over time for each class
    pass

def rln_plt_class_distributions():
    try:
        star = rln_starparser.parse_star(argv[1])
    except:
        print("Please specify an input STAR file after the program name")
        exit()

    class_numbers = rln_starparser.metadata_column(star, '_rlnClassNumber')

    data = bin(class_numbers)

    print(data)

if __name__ == "__main__":
    rln_plt_class_distributions()
    