"""

Tools used to parse input STAR files from relion jobs and extract requested data for downstream use.

"""

def parse_star(starfile) -> list:
    
    # Open the star file, parse it and return as a list
    
    output = []
    
    with open(starfile, 'r') as star:
        for row in star:
            row = row.strip().split()
            output.append(row)
    
    return output

def metadata_index(star: list, metadata_label: str) -> int:
    
    # Find index of metadata label of interest and convert to python numbering
    
    label = 0
    
    for row in star:
        if len(row) < 15 and len(row) > 1:
            if row[0] == metadata_label:
                label = int(row[1][1:])
    
    return label-1

def metadata_column(star: list, metadata_label: str) -> list:

    label = metadata_index(star, metadata_label)
    output = []

    for row in star:
        if len(row) > 10:
            output.append(row[label])

    return output

if __name__ == "__main__":
    pass