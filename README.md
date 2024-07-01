# rln_plt_orientations.py #

Project started 07/01/2024

## Objective

Create a python program that plots particle orientations described in a relion STAR file as a 2D plot in the style of cryosparc viewing direction distribution plot.

## Program outline draft (WIP)

### Basic functionality outline:

1) Parse relion STAR file, extract relevant coordinates, convert if needed (unclear yet)
2) Determine appropriate bin size based on orientational sampling, quantify number of particles in each bin
3) Plot each bin based on the two coordinates with color of the point indicating the number of particles in that bin, i.e. a heatmap

### Additional functionality 

1) Deal with datasets refined with symmetry
2) ???