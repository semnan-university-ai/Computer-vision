

# Amir Shokri
# 9811920009
# Dr.Fadaei
# amirsh.nll@gmail.com
# python exercise - 2

n = [ 23, 3, 45, 96, 11, 7, 36, 9, 27, 85 ]


arrLen = 10
for i in range(arrLen-1): 
	for j in range(0, arrLen-i-1):
		if n[j] > n[j+1]: 
			n[j], n[j+1] = n[j+1], n[j] 

print(n)