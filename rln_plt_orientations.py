from numpy import pi as pi
from matplotlib import pyplot as plt
from sys import argv

def parse_star(starfile) -> list:
    # Open the star file, parse it and return as a list
    
    output = []
    
    with open(starfile, 'r') as star:
        for row in star:
            row = row.strip().split()
            output.append(row)
    
    return output

def metadata_index(starfile: list, metadata_label: str) -> int:
    
    # Find index of metadata label of interest and convert to python numbering
    
    label = 0
    
    for line in starfile:
        if len(line) < 15 and len(line) > 1:
            if line[0] == metadata_label:
                label = int(line[1][1:])
    
    return label-1

def radians(degree: float) -> float:
    return degree * (pi / 180)

def bin(angles: tuple, bins: dict) -> tuple:
    rot = angles[0]
    tilt = angles[1]
    rot_bins = []
    tilt_bins = []

    for key in bins.keys():
        rot_bins.append(key[0])
        tilt_bins.append(key[1])

    rot_bin = float()
    tilt_bin = float()
    
    for angle in rot_bins:
        if rot >= angle:
            rot_bin = angle
    
    for angle in tilt_bins:
        if tilt >= angle:
            tilt_bin = angle
    
    return rot_bin, tilt_bin

def main():
    # Try to parse star file and figure out metadata indices to extract data from
    
    try:
        star = parse_star(argv[1])
    except:
        print("Please specify an input STAR file after the program name")
        exit()
    
    rot = metadata_index(star, '_rlnAngleRot')
    tilt = metadata_index(star, '_rlnAngleTilt')

    # Extract angles of interest (rotation, tilt) and output as a tuple

    angles = []

    for row in star:
        if len(row) > 10:
            angles.append((float(row[rot]), (float(row[tilt])-90)))

    # Convert angles to radians

    converted = []

    for rot, tilt in angles:
        converted.append((radians(rot), radians(tilt)))

    # Setup data structure to bin the converted coordinates into
    # TODO: make bin size dynamic based on orientational sampling of the data
    # TODO: This doesn't seem very efficient and takes a while to run... but it works

    bin_size = 64
    bin_range = range((-1 * bin_size//2), (bin_size//2))
    bins = dict()

    for x in bin_range:
        for y in bin_range:
            bins[(x*(2*pi / bin_size), y*(pi / bin_size))] = 0
    
    for angle in converted:
        bins[bin(angle, bins)] += 1

    # Plot the viewing distribution

    x, y = zip(*bins)
    colors = bins.values()
    plt.scatter(x, y, s=40, c=colors, marker="H", cmap='rainbow')

    plt.xticks([-1*(pi), -1*((3*pi)/4), -1*((2*pi)/4), -1*((1*pi)/4), 0, 1*((1*pi)/4), (2*pi)/4, (3*pi)/4, (4*pi)/4], \
        ['-π', '-3π/4', '-π/2', '-π/4', '0', 'π/4', 'π/2', '3π/4', 'π'])
    plt.yticks([-1*((2*pi)/4), -1*((1*pi)/4), 0, 1*((1*pi)/4), (2*pi)/4], \
        ['-π/2', '-π/4', '0', 'π/4', 'π/2'])

    plt.xlabel("Azimuth")
    plt.ylabel("Elevation")
    plt.tight_layout()
    plt.show()

main()