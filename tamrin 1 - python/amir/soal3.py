

# Amir Shokri
# 9811920009
# Dr.Fadaei
# amirsh.nll@gmail.com
# python exercise - 3

a = 1
b = 1
temp = 0
counter = 1

while counter < 9:
	temp = a + b
	a = b
	b = temp
	counter+=1


print(b)