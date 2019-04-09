prices = {"Plavix": 6.50, "Aspirin": 1.33}


def plavix_cost():
    p_cost = prices["Plavix"] * 365

    return p_cost


def aspirin_cost():
    a_cost = prices["Aspirin"] * 365

    return a_cost


print("Plavix", "=", plavix_cost().__round__())
print("Aspirin", "=", aspirin_cost().__round__())
