# Write a Python program to count the number of lines in a text file. 

def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print("File not found.")
        return 0

filename = "example.txt"  
line_count = count_lines(filename)
print("Number of lines in the file:", line_count)
