# initialize x, y, z with input from user
x, y, z = str(input()).split()
z = int(z)
a = 0
b = 0

# process
if x != "!":
	a = z
	b = z
	x, y, z = str(input()).split()
	#x, y, z = str(input()), str(input()), int(input())
	z = int(z)
	while x != '!':
		if z > a:
			a = z
			print(x)
		if z%b == 0:
			print(x)
		x, y, z = str(input()).split()
		#x, y, z = str(input()), str(input()), int(input())
		z = int(z)

## The Final Result of output is bndhbbrhhssl