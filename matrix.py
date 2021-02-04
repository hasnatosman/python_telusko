max = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [7, 8, 9, 10]
]
x = []
for i in range(4):
    x.append([row[i] for row in max])
print(x, end='')
