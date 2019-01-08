food = ['apples', 'oranges', 'pears']

print(food)


def show_choc():
    food = ['snickers', 'kit-kat', 'reece\'s']

    print(food)


show_choc()
print(food)  # this would be overwritten by the outer-scoped food instance initialized globally
