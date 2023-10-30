# Write a Python program to copy the contents of a file to another file

def copy_file(source_filename, destination_filename):
    try:
        with open(source_filename, 'r') as source_file:
            contents = source_file.read()

        with open(destination_filename, 'w') as destination_file:
            destination_file.write(contents)
        
        print("File successfully copied.")
    except FileNotFoundError:
        print("File not found.")

source_filename = "source.txt"   
destination_filename = "destination.txt"  

copy_file(source_filename, destination_filename)
