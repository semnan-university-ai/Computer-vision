
# Amir Shokri [ 9811920009 ] - Farshad Asgharzade [ 9811920004  ] - Alireza Gholamnia [ 9811920011 ]
# Dr.Fadaei
# amirsh.nll@gmail.com - Farshad_asgharzade@hotmail.com - gholamniareza@gmail.com
# python exercise 2 - Question 1

def fibDirect(n):
	a = 1
	b = 1
	temp = 0

	for x in range(2,n):
		temp = b
		b = a + b
		a = temp

	return b

def fibRecursive(n):
	if n == 1 | n == 2:
		return 1
	elif n < 0:
		return 0
	else:
		fibRecursive(n-1) + fibRecursive(n-2)


# Test Direct fibonacci
print(fibDirect(10))

# Test Recursive fibonacci
print(fibDirect(10))