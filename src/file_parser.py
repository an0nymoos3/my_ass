"""
    This file parses the text content of the .ass file.
    It then returns the instructions with all the extra
    symbols and blank lines stripped.
"""

def parse_file(ass_file) -> []:
    lines = []
    with open(ass_file) as f:
        for line in f.readlines():
            line = line.strip()
            
            # Split each instruction
            line = line.split(",")

            if len(line) == 1:
                if line[0] != '':
                    lines.append(line)

            if len(line) > 1:
                lines.append(line)


    # Remove all spaces
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j] = lines[i][j].strip()    

    return lines