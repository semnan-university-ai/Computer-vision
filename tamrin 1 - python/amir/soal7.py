

# Amir Shokri
# 9811920009
# Dr.Fadaei
# amirsh.nll@gmail.com
# python exercise - 7

n = 23543
counter = 0

for x in range(2,round(n / 2) + 1):
	if n % x == 0:
		counter+=1

if counter==0:
	print('yes')
else:
	print('no')