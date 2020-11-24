from functools import reduce

items = list(range(100, 1001))
multip_all = reduce(lambda x, y: x * y, items)

print(multip_all)