def calculate(lhs, rhs, operation):
    if operation == "add":
        return lhs + rhs

    elif operation == "sub":
        return lhs - rhs

    elif operation == "mult":
        return lhs * rhs

    elif operation == "div":
        return lhs / rhs

#------------------------------------------------------------

print("Hello World")

#------------------------------------------------------------

lhs_num = input("Введите первое число: ")

rhs_num = input("Введите второе число: ")

operation = input("Введите операцию (add/sub/mult/div): ")

lhs_num = int(lhs_num)

rhs_num = int(rhs_num)

print(calculate(lhs_num, rhs_num, operation))

#------------------------------------------------------------

evens = [num for num in range(11) if num % 2 is 0]

print(evens)
