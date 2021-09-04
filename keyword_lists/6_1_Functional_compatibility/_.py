list = []

with open("_.txt") as f:
    for i in f:
        list.append(i.rstrip('\n'))

# print(list)