def primeNumber(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
    
number = int(input())
if primeNumber(number):
    print("Es primo")
else:
    print("No es primo")