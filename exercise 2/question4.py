
# Amir Shokri [ 9811920009 ] - Farshad Asgharzade [ 9811920004  ] - Alireza Gholamnia [ 9811920011 ]
# Dr.Fadaei
# amirsh.nll@gmail.com - Farshad_asgharzade@hotmail.com - gholamniareza@gmail.com
# python exercise 2 - Question 4

inputString = open("input.txt", "r")
inputString = inputString.read()
inputStringSplit = inputString.split(" ")

WordCount = []
for w in inputStringSplit:
    WordCount.append(inputStringSplit.count(w))

dic = list(zip(inputStringSplit, WordCount))
dic=dict.fromkeys(dic)

print(dic)