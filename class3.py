class Dog:
    trick = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.trick.append(trick)


name1 = Dog('Hasico')
name2 = Dog('Max')

print(name1.name)
print(name2.name)

name1.add_trick('Roll over')
name2.add_trick('Find wanted')

print(name1.trick)
#print(name2.trick)