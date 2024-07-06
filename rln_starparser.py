"""

Tools used to parse input STAR files from relion jobs and extract requested data for downstream use.

"""

def parse_star(starfile: str) -> list:
    
    # Open the star file, parse it and return as a list
    
    star = []
    
    with open(starfile, 'r') as file:
        for row in file:
            row = row.strip().split()
            star.append(row)
    
    return star

def metadata_index(starfile: str, metadata_label: str) -> int:
    
    # Find index of metadata label of interest and convert to python numbering
    
    star = parse_star(starfile)
    label = 0
    for row in star:
        if len(row) < 15 and len(row) > 1:
            if row[0] == metadata_label:
                label = int(row[1][1:])
    
    return label-1

def metadata_column(starfile: str, metadata_label: str) -> list:

    # Extract metadata column from specified label into a list

    star = parse_star(starfile)
    label = metadata_index(starfile, metadata_label)
    data = []

    for row in star:
        if len(row) > 10:
            data.append(row[label])

    return data

if __name__ == "__main__":
    pass