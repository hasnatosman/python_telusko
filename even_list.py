"""
will generate a new list that will collect odd number list from given list.

"""
lst = [2, 4, 3, 5, 6, 43, 65, 87, 99, 88]
new_lst = []
for i in lst:
    if i % 2 == 0:
        new_lst.append(i)

print(new_lst)