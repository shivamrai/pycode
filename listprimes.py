def find_primes(listall):
    # def is_prime():
    list1 = []
    for x in listall:
        if is_prime(x):
            list1.append(x)
        else:
            continue
    print("The prime numbers are: ", list1)


def is_prime(n):
    c = False
    if n == 2:
        c = True
    elif n == 1:
        c = False
    else:
        for m in range(2, n):
            if n % m == 0:
                c = False
                break
            else:
                c = True
    return c


if __name__ == "__main__":
    # division primes in list
    number = input("Enter a number: ")

    list = []
    while int(number) != -1:
        if int(number) < 0:
            print("Invalid Input")
            number = input("Enter another number: ")
        else:
            list.append(int(number))
            number = input("Enter next number: ")

    print("You entered these numbers: ", list)
    find_primes(list)
