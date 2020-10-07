
# Amir Shokri [ 9811920009 ] - Farshad Asgharzade [ 9811920004  ] - Alireza Gholamnia [ 9811920011 ]
# Dr.Fadaei
# amirsh.nll@gmail.com - Farshad_asgharzade@hotmail.com - gholamniareza@gmail.com
# python exercise 2 - Question 5

def fibRecursive(n):
	if n == 1 | n == 2:
		return 1
	elif n < 0:
		return 0
	else:
		fibRecursive(n-1)

from datetime import datetime

start = datetime.now()
fibRecursive(800)
print("RunTime : ", datetime.now()-start)