import random
import math

# Функция, определяющая простату числа
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    elif n < 2:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Функция, определяющая взаимную простоту
def is_coprime_numbers(a, b):
    while b != 0:
        a, b = b, a % b
    return a == 1

# Генератор простого числа
def generate_prime():
    n = int(random.random()*10000)
    while not is_prime(n):
        n += 1
    return n

# Класс, реализующий публичный ключ
class PublicKey:
    def __init__(self, e, n):
        self.e = e
        self.n = n

    def encrypt(self, num):
        return pow(num, self.e, self.n) # Используем возведение в степень с по модулю

# Класс, реализующий закрытый ключ
class PrivateKey:
    def __init__(self, d, n):
        self.d = d
        self.n = n

    def decrypt(self, num):
        return pow(num, self.d, self.n)

# Генератор ключей:
def createKeys():
    p = generate_prime()
    q = generate_prime()

    n = p * q
    f = (p-1)*(q-1)

    e = None
    for i in range(1, f):
        if is_prime(i) and is_coprime_numbers(i, f):
            e = i
            break
    d = None
    for i in range(1, n):
        if (i * e) % f == 1:
            d = i
    return PublicKey(e, n), PrivateKey(d, n)

def convert_to_str(list):
    res = ""
    for i in list:
        res += chr(i)
    return res

# Интерфейс программы:
if __name__ == "__main__":
    public, private = createKeys()

    int_array = [ord(s) for s in input("Input message: ")]

    print("Public keys: {" + str(public.e) + "," + str(public.n) + "}")
    print("Public keys: {" + str(private.d) + "," + str(private.n) + "}")

    en_int_array = [public.encrypt(i) for i in int_array]
    print("Encrypted:", en_int_array)
    dec_int_array = [private.decrypt(i) for i in en_int_array]
    print("Checked:", convert_to_str(dec_int_array))
    input()
