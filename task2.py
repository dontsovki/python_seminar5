# Подсчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры
# (4, 6 и 0) и 2 нечетные (3 и 5).

def func(num):
    even = 0
    odd = 0

    if not num:
        return even, odd
    if num % 10 % 2 == 1:
        odd += 1
    else:
        even += 1
    return func(num // 10, even, odd)


n = int(input())
func(n)