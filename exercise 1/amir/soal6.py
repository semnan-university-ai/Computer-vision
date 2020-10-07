

# Amir Shokri
# 9811920009
# Dr.Fadaei
# amirsh.nll@gmail.com
# python exercise - 6

n = 2
i = 1
fullNum = 0;
sumNum = 0

while fullNum<4:
	sumNum = 0
	i = 1

	while i < n:
		if n % i == 0:
			sumNum+=i
		i+=1

	if n == sumNum:
		print(n, end=" ")
		fullNum+=1

	n+=1