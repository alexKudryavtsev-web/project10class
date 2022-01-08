# Реализуем алфавит, у нас будет латиница
alphabet = ""

with open("alphabet.txt", "r", encoding='UTF8') as f:
    alphabet = f.read()

# Функции, работающие с числами


def encr_number(num, e, n):
    return int(pow(num, e, n))


def decr_number(num, d, n):
    return int(pow(num, d, n))

# Функции, расширяющие функции сверху


def encr_text(text, e, n):
    result = []
    for symbol in text:
        result.append(encr_number(alphabet.index(symbol), e, n))
    return result


def decr_text(int_list, d, n):
    result = ""
    for num in int_list:
        result += alphabet[decr_number(num, d, n)]
    return result
