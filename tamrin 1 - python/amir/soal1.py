

# Amir Shokri
# 9811920009
# Dr.Fadaei
# amirsh.nll@gmail.com
# python exercise - 1

n = [ 23, 3, 45, 96, 11, 7, 36, 9, 27, 85 ]

minNum = n[0]
maxNum = n[0]

for x in n:
	if x > maxNum:
		maxNum = x
	if x < minNum:
		minNum = x

print("minimum number : ", minNum)

print("maximum number : ", maxNum)
		