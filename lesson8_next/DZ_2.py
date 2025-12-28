"""
Реализовать программу с функционалом калькулятора
для операций над двумя числами. Числа и операция вводятся
пользователем с клавиатуры. Использовать обработку исключений.
"""

try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    sym = str(input("Введите символ операции: "))
    if sym == '+':
        print(num1 + num2)
    elif sym == '-':
        print(num1 - num2)
    elif sym == '*':
        print(num1 * num2)
    elif sym == '/':
        print(num1 / num2)
    elif sym != '+' or sym != '-' or sym != '*' or sym != '/':
        print("Необходимо ввести одну из четырех операций: +, -, *, /")
except ZeroDivisionError:
    print('На ноль то не делим')
except ValueError:
    print("Введите число")