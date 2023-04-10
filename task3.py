# Задание 3. Сформировать из введенного числа
# обратное по порядку входящих в него
# цифр и вывести на экран. Например, если введено число 3486,
# то надо вывести число 6843.


number = int(input('Введите число: '))
number2 = 0

for i in enumerate(str(number)):
    digit = number % 10
    number = number // 10
    number2 = number2 * 10
    number2 = number2 + digit

print(f"Заданное число в противоположном порядке: {number2}")