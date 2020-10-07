from functions import *

array = [23, 3, 45, 96, 11, 36, 9, 27, 85]
string = 'Semnan University'

# ****************************************
# 1.Find Maximum Number in array

maximum = find_max(array)
print("Question 1: Maximum => {}".format(maximum))
print('****************************************')
# ****************************************
# 2.Order Array
ordered_list = order_array(array.copy())
print("Question 2: Ordered {} => {}".format(array, ordered_list))
print('****************************************')

# ****************************************
# 3.Find Fibonacci 10
print("Question 3: Fibonacci {} => {}".format(10, fibonacci(10)))
print('****************************************')

# ****************************************
# 4.Reverse String, We can use this method too: string[::-1]
print("Question 4: Reversed {} => {}".format(string, reverser(string)))
# print("Question 4 python helper: {}".format(string[::-1]))
print('****************************************')

# ****************************************
# 5.Find GCD n = 654 and m = 744
print("Question 5: GCD n = {} & m = {} => {}".format(654, 744, gcd(654, 744)))
print('****************************************')

# ****************************************
# 6.Find prefect numbers
finds = []
counter = 1
while len(finds) < 4:
    if is_perfect(counter):
        finds.append(counter)
    counter += 1
print("Question 6: 4 Prefect Numbers => {}".format(finds))
print('****************************************')

# ****************************************
# 7.Check 23543 is prime or not
yes = is_prime(23543)
if yes:
    output = 'Yes, 23543 is prime'
else:
    output = 'No, 23543 is not prime'
print("Question 7: Check Prime => {}".format(output))
print('****************************************')

# ****************************************
# 8.Print All prime numbers between 1000 and 2000
lower = 1000
upper = 2000
primes = []
for num in range(lower, upper + 1):
    if is_prime(num):
        primes.append(num)
print("Question 8: Prime numbers between", lower, "and", upper, "are:", primes)
print('****************************************')

# ****************************************
# 9.Print stars
number = 6
print("Question 9: print stars for number {}".format(number))
print_stars(number)
print('****************************************')

# ****************************************
# 10.Replace
replaced = string.replace('e', 'zs')
print("Question 10: Replace e with zs in {} => {}".format(string, replaced))
