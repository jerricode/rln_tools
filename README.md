# rln_plt_orientations.py #

Project started 07/01/2024

Uses python 3.12 venv

## Objective

Create a python program that plots particle orientations described in a relion STAR file as a 2D plot in the style of cryosparc viewing direction distribution plot.

## Program outline draft (WIP)

**Learning goals**
* Try to use as few external packages as possible, i.e. make my own star file handler function

### Basic functionality outline:

1) Parse relion STAR file, extract relevant coordinates, convert if needed (unclear yet)
2) Determine appropriate bin size based on orientational sampling, quantify number of particles in each bin
3) Plot each bin based on the two coordinates with color of the point indicating the number of particles in that bin, i.e. a heatmap

### Additional functionality 

1) Deal with datasets refined with symmetry
2) Plot by class if done on a 3D class file?
3) ...