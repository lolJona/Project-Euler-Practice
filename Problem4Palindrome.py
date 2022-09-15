"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

x = [*range(100, 1000, 1)]
y = [*range(100, 1000, 1)]
z = []
q = []
for i in x:
    for j in y:
        prod = i * j
        z.append(prod)
for l in z:
    if list(reversed(str(l))) == list(str(l)):
        q.append(int(l))
print(max(q))
