

def calculator():
    # I firstly added functions of operations, but I decided to they are unnecessary.
    # def add(a, b):
    #     return a + b
    #
    # def subtract(a, b):
    #     return a - b
    #
    # def multiply(a, b):
    #     return a * b
    #
    # def divide(a, b):
    #     if a == 0:
    #         return
    #     else:
    #         a / b

    isagain = True
    isagain_with_same_result = False
    result = 0
    while isagain:

        if isagain_with_same_result:
            number_1 = float(result)
            print("=" * len(f"The first number is {number_1} as you calculated the previous session."))
            print(f"The first number is {number_1} as you calculated the previous session.")
        else:
            number_1 = float(input("What's the first number?\n:"))

        operation = input("'+'  '-'  '*'  '/'   \nPick an operation\n:").strip()
        number_2 = float(input("What's the next number?\n:"))

        if operation == "+":
            result = number_1 + number_2
            result = round(result)
            result = format(result, '.2f')
            print(str(number_1) + " + " + str(number_2) + " = " + str(result))

        elif operation == "-":
            result = number_1 - number_2
            result = round(result)
            result = format(result, '.2f')
            print(str(number_1) + " - " + str(number_2) + " = " + str(result))

        elif operation == "*":
            result = number_1 * number_2
            result = round(result, 2)
            result = format(result, '.2f')
            print(str(number_1) + " * " + str(number_2) + " = " + str(result))

        elif operation == "/":
            result = number_1 / number_2
            result = round(result, 2)
            result = format(result, '.2f')
            print(str(number_1) + " / " + str(number_2) + " = " + str(result))

        else:
            return

        isagain_with_same_result = input(f"Type 'y' to continue calculating with {result}, "
                                         f"or type 'n' to start a new calculation, "
                                         f"or type 'exit' if you want to exit!\n:").strip().lower()

        if isagain_with_same_result == 'y':
            isagain_with_same_result = True
            continue
        elif isagain_with_same_result == 'n':
            result = 0
            isagain_with_same_result = False
        elif isagain_with_same_result == "exit":
            break



calculator()
print("END")
