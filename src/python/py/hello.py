sum = 0
for x in range(101):
    sum += x
print(sum)


L = ['Bart', 'Lisa', 'Adam']
for item in L:
	print('hello ' + item + '!')


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(99))