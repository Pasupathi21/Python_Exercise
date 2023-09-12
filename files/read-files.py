

# Read TXT files

with open('../data/new-files.txt', 'r') as file:
    read_file = file.readlines()
    print(read_file)