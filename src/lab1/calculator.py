
def calc(num1, operator, num2):
    num1 = float(num1)
    num2 = float(num2)
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
if __name__ == '__main__':
    while True:
        a = input('Введите первое число: ')
        sign = input("Введите оператор: ")
        b = input("Введите второе число: ")
        print(calc(a,sign,b))
