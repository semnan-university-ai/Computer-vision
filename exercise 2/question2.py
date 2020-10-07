
# Amir Shokri [ 9811920009 ] - Farshad Asgharzade [ 9811920004  ] - Alireza Gholamnia [ 9811920011 ]
# Dr.Fadaei
# amirsh.nll@gmail.com - Farshad_asgharzade@hotmail.com - gholamniareza@gmail.com
# python exercise 2 - Question 2


import math

def Degree2Radian(deg):
	return deg * 3.14 / 180

num = input("Enter Number : ")
func = input("cos / sin / tan ? ")

xx = 0
for x in range(0,360):
	if str(x) == num:
		num = int(x)
		xx = 1
		typ = "deg"
		if num < 0 | num > 360:
			print("Invalid Number")
			exit()
		break

if xx == 0:
	typ = "radian"
	num = float(num)
	if num < 0.0:
		print("Invalid Number")
		exit()
	if num > 360.0:
		print("Invalid Number")
		exit()

if func == "cos":
	if typ == 'deg':
		print(math.cos(Degree2Radian(num)))
	else:
		print(math.cos(num))
elif func == "sin":
	if typ == 'deg':
		print(math.sin(Degree2Radian(num)))
	else:
		print(math.sin(num))
elif func == "tan":
	if typ == 'deg':
		print(math.tan(Degree2Radian(num)))
	else:
		print(math.tan(num))
else:
	print("Invalid function")
	exit()