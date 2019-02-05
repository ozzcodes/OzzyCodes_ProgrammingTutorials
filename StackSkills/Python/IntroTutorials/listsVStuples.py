def example():
    return 15, 19


# Tuple example (immutable)
a, b = example()
print(a)
print(b)

# Python list (mutable)
x = [6, 2, 6, 8, 2, 1, 8, 9]

print(x)
print(x[5])

x.append(12)
print(x)

x.insert(5, 7)
print(x)

# Removes only one value, the first value
x.remove(2)
print(x)

print(x.index(12))
print(x.count(6))

x.sort()
print(x)

y = ['Spot', 'Cam', 'Jam', 'Dan', 'Ozzy']
y.sort()
print(y)

y.reverse()
print(y)
