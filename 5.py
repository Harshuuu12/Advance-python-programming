# Write a Python program to read a file line by line and store it into a lis

def read_lines_to_list(filename):
    lines = []
    f = open(filename, 'r') 
    for line in file:
        lines.append(line.strip())
        return lines

filename = 'sample.txt'  

lines_list = read_lines_to_list(filename)

for line in lines_list:
    print(line)
