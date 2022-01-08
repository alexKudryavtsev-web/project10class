# В этом файле есть все функции по генерации ключей
import math
import random

# Проверка простоты числа


def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

# НОД:


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Случайно выбираем два простых числа


def random_prime(low=10, high=20):
    list_num = []
    i = 2
    while len(list_num) <= high:
        if is_prime(i):
            list_num.append(i)
        i += 1
    list_num = list_num[low:]
    p = random.choice(list_num)
    list_num.remove(p)
    q = random.choice(list_num)
    return p, q

# Генерируем ключи


def key():
    p, q = random_prime()
    n = p*q
    f = (p-1)*(q-1)
    e_list = []
    d_list = []

    for i in range(2, f):
        if is_prime(i) and gcd(n, i) == 1:
            e_list.append(i)

    for i in range(2, f):
        if gcd(n, i) == 1:
            d_list.append(i)

    return [random.choice(e_list), n], [random.choice(d_list), n]


