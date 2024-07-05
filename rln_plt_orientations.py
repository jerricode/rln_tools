"""

Plot refined particle image orientations from a relion refinement job output STAR file as a heatmap.

"""

import numpy as np
from matplotlib import pyplot as plt
from sys import argv
import rln_starparser

def radians(degree: float) -> float:
    return degree * (np.pi / 180)

def plot(angles: list) -> plt:
    # Plot the data as a hexbin heatmap
    # TODO: make bin size dynamic based on orientational sampling of the data

    x, y = zip(*angles)
    gridsize = 64

    plt.hexbin(x, y, gridsize=gridsize, cmap='jet', mincnt=1)
    plt.xlim(-1*np.pi, np.pi)
    plt.ylim(-1*(np.pi/2), np.pi/2)

    plt.xticks([-1*(np.pi), -1*((3*np.pi)/4), -1*((2*np.pi)/4), -1*((1*np.pi)/4), 0, 1*((1*np.pi)/4), (2*np.pi)/4, (3*np.pi)/4, (4*np.pi)/4], \
        ['-π', '-3π/4', '-π/2', '-π/4', '0', 'π/4', 'π/2', '3π/4', 'π'])
    plt.yticks([-1*((2*np.pi)/4), -1*((1*np.pi)/4), 0, 1*((1*np.pi)/4), (2*np.pi)/4], \
        ['-π/2', '-π/4', '0', 'π/4', 'π/2'])

    plt.colorbar(label='# of particles')
    plt.xlabel('Azimuth')
    plt.ylabel('Elevation')
    plt.tight_layout()
    plt.savefig('orientations.svg', format='svg', metadata={'Description' : f'Generated from {argv[1]}'})
    plt.show()

def plot_orientations():
    # Try to parse star file and figure out metadata indices to extract data from
    try:
        star = rln_starparser.parse_star(argv[1])
    except:
        print("Please specify an input STAR file after the program name")
        exit()
    
    # Get the metadata indices of interest for plotting
    rot = rln_starparser.metadata_index(star, '_rlnAngleRot')
    tilt = rln_starparser.metadata_index(star, '_rlnAngleTilt')

    # Extract angles of interest (rotation, tilt), convert to radians, output as a tuple
    angles_radians = []
    for row in star:
        if len(row) > 10: # Skip the header portion of the file
            angles_radians.append((radians(float(row[rot])), (radians(float(row[tilt])-90))))
    
    # Plot the converted angles as a hexbin heatmap
    plot(angles_radians)

if __name__ == "__main__":
    plot_orientations()