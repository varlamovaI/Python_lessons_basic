# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
"""
def my_round(num, ndig):
    num = num*(10**ndig)+0.41
    num = num//1
    return num/(10**ndig)

print(my_round(2.1234567, 5))
print(my_round(2.123456789874, 3))
print(my_round(2.1234567, 2))

"""


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    t1 = ticket_number[:3]
    t2 = ticket_number[3:]

    sum1 = 0
    sum2 = 0
    for i in t1:
        sum1 = sum1 + int(i)
    for i in t2:
        sum2 = sum2 + int(i)
    if sum1 == sum2: print ('lucky')
    else: print ('unlucky')

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
