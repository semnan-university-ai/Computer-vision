

# Amir Shokri
# 9811920009
# Dr.Fadaei
# amirsh.nll@gmail.com
# python exercise - 5

n = 654
m = 744

if n > m:
	maxNum = n
else:
	maxNum = m

counter = 1
BMM = 0

while counter <= maxNum:
	if n % counter == 0:
		if m % counter == 0:
			BMM = counter
	counter+=1

print(BMM)