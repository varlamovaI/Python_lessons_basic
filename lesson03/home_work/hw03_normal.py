# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
"""
def fibonacci(n,m):
    import math
    while n <= m :
        a = int((((1 + math.sqrt(5))/2)**n-((1 - math.sqrt(5))/2)**n)/
                (math.sqrt(5)))
        print (a)
        n += 1

x = fibonacci(4,18)
print ("="*50)
"""


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


num = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]

def srt(list):
    print (num)
    lst = []
    while len(num) > 0 :
        x = num[0]
        for i in num :
            if i <= x :
                x = i
            num.remove(x)
            lst.append(x)
        print (lst)

srt(num)


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
