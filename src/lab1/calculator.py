a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
sign = input("Введите один из знаков +-*/: ")


def calc(num1, operator, num2):
    try:
        if operator == "+":
            return f"{num1} + {num2} = {num1 + num2}"
        if operator == "-":
            return f"{num1} - {num2} = {num1 - num2}"
        if operator == "*":
            return f"{num1} * {num2} = {num1 * num2}"
        if operator == "/":
            return f"{num1} / {num2} = {num1 / num2}"
        raise ValueError("Введены некорректные данные.")
    except ZeroDivisionError:
        return "На ноль делить нельзя."


print(calc(a, sign, b))