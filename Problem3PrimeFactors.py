"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

primelist = []
for nums in range(1,13195):
    if 13195 % nums == 0:
        primelist.append(nums)
print(primelist)
for prime in primelist:
    if prime % 3 == 0:
        primelist.remove(prime)
print(primelist)
for prime in primelist:
    if prime > 5 and prime % 5 == 0:
        primelist.remove(prime)
print(primelist)
for prime in primelist:
    if prime > 7 and prime % 7 == 0:
        primelist.remove(prime)
print(primelist)
for prime in primelist:
    if prime > 13 and prime % 13 == 0:
        primelist.remove(prime)
print(primelist)
for prime in primelist:
    if prime > 29 and prime % 29 == 0:
        primelist.remove(prime)
print(primelist)
for prime in primelist:
    if prime > 2638 and prime % 2639 == 0:
        primelist.remove(prime)
print(primelist)

# Needs to be optimized!
