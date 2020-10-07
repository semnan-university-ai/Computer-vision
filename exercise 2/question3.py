
# Amir Shokri [ 9811920009 ] - Farshad Asgharzade [ 9811920004  ] - Alireza Gholamnia [ 9811920011 ]
# Dr.Fadaei
# amirsh.nll@gmail.com - Farshad_asgharzade@hotmail.com - gholamniareza@gmail.com
# python exercise 2 - Question 3

def isPrime(n):
	for x in range(2,round(n/2)+2):
		if(x % n == 0):
			return 0
	return 1


counter = 1
i = 2
out = 0

while counter < 1000:
	i += 1
	if isPrime(i) == 1:
		counter = counter + 1
		out += i

print(out)