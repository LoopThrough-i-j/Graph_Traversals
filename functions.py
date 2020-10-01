def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1)*n

if __name__ == "__main__":

    x = int(input("Num: "))
    fac = factorial(x)
    print(fac)