from usingFunctions.aClass import Linux

if __name__ == '__main__':
    old = Linux()
    new = Linux()
    old.addData(1.0)
    new.addData(1.2)

print('Old:', old.data)
print('New:', new.data)

