

# Amir Shokri
# 9811920009
# Dr.Fadaei
# amirsh.nll@gmail.com
# python exercise - 10


Str1 = "Semnan Univercity"
output = ""
i = 0

for x in Str1:
	if x == 'e':
		output = output + 'zs'
	else:
		output = output +  x
	i+=1
	
for x in output:
	print(x, end = '')