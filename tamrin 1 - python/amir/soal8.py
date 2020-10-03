

# Amir Shokri
# 9811920009
# Dr.Fadaei
# amirsh.nll@gmail.com
# python exercise - 8

counter = 0

for x in range(999, 2001):
	counter = 0
	for y in range(2,round(x / 2) + 1):
		if x % y == 0:
			counter+=1

	if counter==0:
		print(x, end=" ")