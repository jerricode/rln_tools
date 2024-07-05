"""

Tools used to parse input STAR files from relion jobs for downstream use.

"""

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

if __name__ == "__main__":
    pass