def prime_checker(number):
    IsPrime = False
    for i in range(2, number):
        if number % i == 0:
            IsPrime = False
            break
        else:
            IsPrime = True

    if IsPrime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Enter a number to be checked if it's Prime or not! : "))
prime_checker(number=n)