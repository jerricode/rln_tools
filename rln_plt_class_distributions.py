"""

Plot the particle distribution between classes as a function of refinement iteration for a series of star files.--> This may benefit from an iteration class? Because we will be looking at multiple iterations worth of data? Not sure yet

"""

import rln_starparser
import matplotlib.pyplot as plt
import numpy as np
import glob

def get_iteration(starfile: str) -> int:
    filename = starfile.split("/")[-1]
    iteration = filename.split("_")[1][2:]
    return iteration

def num_classes(starfile: str) -> int:
    return len(np.unique(rln_starparser.metadata_column(starfile, '_rlnClassNumber')))

def bin_particle_classes(starfile: str) -> dict:
    
    # Return the total number of particles per class as a dict

    particle_classes = rln_starparser.metadata_column(starfile, '_rlnClassNumber')
    particle_numbers = dict()
    
    for i in range(1, (int(max(particle_classes))+1)):
        particle_numbers[f'Class {i}'] = 0
    
    for particle in particle_classes:
        particle_numbers[f'Class {particle}'] += 1

    return particle_numbers

def plot(dataset: dict):

    # Plot number of particles in each class by iteration

    iterations = [iteration.split(" ")[1] for iteration in dataset]
    classes = [key for key in dataset['Iteration 1'].keys()]

    for classno in classes:
        numbers = [dataset[iteration][classno] for iteration in dataset]
        plt.plot(iterations, numbers, label=classno, linewidth=3.0)

    # Formatting

    plt.title('Particle class distribution over time')
    plt.xlabel('Iteration')
    plt.ylabel('# of particles')
    plt.legend()
    plt.tight_layout()
    plt.savefig('particle_class_distribution.svg', format='svg')

    plt.show()

def main():
    
    # Get list of STAR files for processing

    starfiles = sorted(glob.glob('/home/jerrico/python/rln_tools/exdata/class_dist/*_data.star'))
    if len(starfiles) == 0:
        raise("No STAR files found for processing")
    
    # Iterate through the files and write the binned particle numbers to a dict

    data = dict()

    for starfile in starfiles:
        
        iteration = f'Iteration {int(get_iteration(starfile))}'
        numbers = bin_particle_classes(starfile)
        data[iteration] = numbers
    
    # Plot the data

    plot(data)
        

if __name__ == "__main__":
    main()
    