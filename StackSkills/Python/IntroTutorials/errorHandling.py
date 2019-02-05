try:
    name = input('What is your name? ')
    print('Running the try...')

    print(str(x))


except TypeError as t:
    print('TypeError triggered')

except NameError as n:
    print('NameError triggered')
    print(str(n))

except Exception as e:
    print(str(e))
    print('General Exception')
