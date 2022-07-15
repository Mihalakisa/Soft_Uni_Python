number = input()
prime = 0
non_prime = 0

while number != 'stop':
    if int(number) > 1:
        for i in range(2, int(number)):
            if int(number) % i == 0:
                non_prime += int(number)
        else:
            prime += int(number)
    elif int(number) == 0:
        non_prime += int(number)
    else:
        print("Number is negative.")

    number = input()

print(prime, non_prime)