from sys import argv
from os.path import exists

script, from_file, to_file = argv

open(to_file, 'w').write(open(from_file).read())

# indata is just input with .read() at the end
# input = open(from_file)
# indata = input.read()

# line 14 is just output with .write(indata) at the end
# output = open(to_file, 'w')
# output.write(indata)

#combine the two by making both parts into 2 lines, then putting new indata inside output
