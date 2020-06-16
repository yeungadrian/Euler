
n = 100

max_count = 1
number = 1

for x in range(1,1000000):
    n = x
    count = 0 
    while n > 1:
        if n % 2 == 0:
            n =  n / 2
        else:
            n = 3 * n + 1
        count = count + 1

    if count > max_count:
        max_count = count
        number = x
    print(f'iteration = {x}')


print(max_count)
print(number)