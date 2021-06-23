
import statistics

# Input from user:
name = input('What is your name?: ')
print('Hello', name)


# Statistics module in use for list of numbers
exList = [5, 3, 2, 9, 9, 7, 4, 3, 1, 8, 9]

x = statistics.mean(exList)
print(x)

x = statistics.median(exList)
print(x)

x = statistics.mode(exList)
print(x)

x = statistics.stdev(exList)
print(x)

x = statistics.variance(exList)
print(x)
