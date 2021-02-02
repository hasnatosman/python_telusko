even_lst = []


def func(n):
    x, y = 0, 1
    while x < n:
        print(x, end=' ')
        x, y = y, x + y
        if x % 2 == 0:
            even_lst.append(x)


print('Fibonacci series: ')
func(100)
print()
print('Even numbers in fibonacci series:  ', even_lst)
