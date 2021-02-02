"""
Here, I will show the even and odd numbers in different ways.
I will use for loop and take input from users.
"""
for x in range(0, 10):
    if x % 2 == 0:
        print(x, ' is a even number.')
    else:
        print(x, 'is odd number.')
        
x = int(input('Enter a number: '))
if x % 2 == 0:
    print('It is even.')
else:
    print('It is odd.')
    


