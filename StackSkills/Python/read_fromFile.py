
# Reads a file that already exists
readMe = open('exampleFile.txt', 'r').read()
print(readMe)


splitMe = readMe.split('\n')
print(splitMe[2])


# easier option for splitting the file, compared to the above
readMe2 = open('exampleFile.txt', 'r').readlines()
print(readMe2)
