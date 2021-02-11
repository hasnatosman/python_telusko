class Dog:
    kind = 'Shefard'

    def __init__(self, name):
        self.x = name


n = Dog(' German')
print(n.kind, n.x)