import random
c = 0
i = input('min number:')
x = input('max number:')
i = int(i)
x = int(x)
n = random.randint(i, x)
while True:
	c += 1
	num = input('please key a number:')
	num = int(num)
	if num == n:
		print('congrats!')
		break
	elif num < n:
		print('up')
	elif num > n:
		print('down')
print('its the', c, 'time')