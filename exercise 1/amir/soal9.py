

# Amir Shokri
# 9811920009
# Dr.Fadaei
# amirsh.nll@gmail.com
# python exercise - 9

n = 7

starChar = n+1
lineChar = 1

for x in range(0,n):

	if(starChar==1):
		break

	for z in range(1,lineChar):
		print("_", end="")
	
	for y in range(1,starChar):
		print("*", end="")

	print("")

	starChar-=1
	lineChar+=1