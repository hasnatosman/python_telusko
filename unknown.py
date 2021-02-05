fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits)
print('Number of fruits ', len(fruits))
print('Pear is in ', fruits.index('pear'), 'nd position.')
print('Number of apple in the list ', fruits.count('apple'))
fruits.remove('banana')

print(fruits)
fruits.reverse()
print(fruits)