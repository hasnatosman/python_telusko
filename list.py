nums = [1, 44, 6, 66]
print(nums[1])
"""
List is data structure where we can put multiple data types. We can store data, we can pull, push
and also retrieve data.
"""

names = ['John', 'Joe', 'Kate']
values = [9.5, 'Has', 25]

print(names)
print(values)

mil = [names, nums, values]
print(mil)

"""
List is mutable. Mutable means you can change the value of the list.
"""
print('\n')
print('\n')
print('\n')
print('Difference between inset and append')
print('\n')
"""
Insert means you can push data in any index of the list.
Append means you input something at the end of the list.

"""

nums.insert(2, 99)
names.append('Appended')

print(names)
print(nums)

"""
Using pop and remove in list...........................

We can remove any data by calling the value
and remove data by calling the index number.

"""

x = [11, 22, 33, 44, 45]
x.remove(45)
print(x)

y = [32, 54, 65, 76]
y.pop(2)
print(y)

"""
Even if we use only pop method without calling the index number
then it will pop or remove the last value.
"""

z = [2, 4, 6, 8, 9]
z.pop()
print(z)


# we can del any data or value from the list by calling del method.............

del z[2:]
print(z)

# we can add multiple value in list....................

z.extend([4, 5, 77, 80])
print(z)
print(min(z))
print(max(z))
print(sorted(z))