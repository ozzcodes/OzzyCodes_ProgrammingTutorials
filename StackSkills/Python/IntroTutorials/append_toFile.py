
# append will add data to a file where write to file will overwrite any data to a file
appendMe = 'Some more text here.'

saveFile = open('exampleFile.txt', 'a')
saveFile.write('\n')
saveFile.write(appendMe)
saveFile.close()

