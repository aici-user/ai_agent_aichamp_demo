number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    is_prime = True
    if number < 2:
        is_prime = False
    else:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

    if is_prime:
        print(f"{number} is odd and prime.")
    else:
        print(f"{number} is odd but not prime.")