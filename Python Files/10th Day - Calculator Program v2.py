def calculator():
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if a == 0:
            return
        else:
            return a / b

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    isagain, isagain_with_same_result = True, False

    while isagain:
        if isagain_with_same_result:
            number_1 = result
            print(f"{number_1} stands as number1!")
        else:
            number_1 = float(input("What's the first number?\n:"))

        operation_symbol = input("\n".join([x for x in operations]) + "\n:").strip()
        number_2 = float(input("What's the next number?\n:"))
        result = operations[operation_symbol](number_1, number_2)
        print(f"{number_1} {operation_symbol} {number_2} = {result}")
        isagain_with_same_result = input(f"Type 'y' to continue calculating with {result}, "
                                         f"or type 'n' to start a new calculation, "
                                         f"or type 'exit' if you want to exit!\n:").strip().lower()
        if isagain_with_same_result == 'y':
            isagain_with_same_result = True
        elif isagain_with_same_result == 'n':
            isagain_with_same_result = False
        else:
            break

calculator()
print("END")
