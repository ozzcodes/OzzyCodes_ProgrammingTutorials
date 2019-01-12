
from sklearn import datasets

iris = datasets.load_iris()
digits = datasets.load_digits()

print(digits.data)

# to obtain the truth for the digit dataset
print('\n\nDigit dataset ground truth:')
print(digits.target)

# Shaping the data arrays
print('\n\nShaping the data arrays:')
print(digits.images[0])
