def find_max(array):
    max = 0
    if array:
        max = array[0]
        for number in array:
            if number > max:
                max = number

    return max


def find_min(array):
    min = 0
    if array:
        min = array[0]
        for number in array:
            if number < min:
                min = number

    return min


def order_array(not_ordered):
    ordered_list = []
    while not_ordered:
        min = find_min(not_ordered)
        ordered_list.append(min)
        not_ordered.remove(min)

    return ordered_list


def fibonacci(n):
    if n <= 1:
        out = 0
    elif n == 2:
        out = 1
    else:
        out = fibonacci(n - 1) + fibonacci(n - 2)

    return out


def reverser(string):
    string = list(string)
    revers = ''
    while string:
        revers += string.pop()

    return revers


def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
    return True


def print_stars(n):
    n = n + 1
    step = n
    for i in range(1, step):
        stars = ''
        for j in range(step, 1, -1):
            if j <= n:
                symbol = '*'
            else:
                symbol = '_'
            stars += symbol
        print(stars)
        n -= 1


def is_perfect(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n


def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)
