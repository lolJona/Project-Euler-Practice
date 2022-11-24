primesum = 0

def is_prime(number):
    if number > 1:
        for num in range(2, int(number**0.5) + 1):
            if number % num == 0:
                return False
        return True
    return False

for num in range(1, 2000000):
    if is_prime(num):
        primesum = primesum + num
print(primesum)
