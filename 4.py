# Write a Python program to read last n lines of a file.

def read_n_lines(fo,n):
    f = open("1.py",'r')
    lines = f.readlines()
    for line in lines[:n]:
        print(line.strip())

filename = 'sample.txt'   
n = 5  

read_n_lines(filename,n)

