"""
Functions do:
    - enable us to reuse code allowing for reduced code repetition
    - offer a way to solve big programs by solving smaller components
"""


def aFunction():
    print('Hello!')


aFunction()


# Function with multiple arguments
def timeString(times, text):
    string = ""

    for x in range(0, times):
        string += text
        return string


myString = timeString(3, 'Hi!')
print(timeString(2, 'Hi!'))
print(myString)
