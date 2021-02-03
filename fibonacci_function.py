"""
def func(n):
    a, b = 0, 1
    while a < n:

        print(a, end=' ')
        a, b = b, a + b
    print()


func(100)
"""


def finona(n):
    result = []
    i, j = 0, 1
    while i < n:
        result.append(i)
        i, j = j, i+j
    return result


f = finona(100)
print(f)
