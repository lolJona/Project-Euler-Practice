"""

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

"""

x = [*range(1, 1000000, 1)]
q = []
for l in x:
    if (list(reversed(str(l))) == list(str(l))) and (list(reversed(str(bin(l)[2:]))) == list(str(bin(l)[2:]))):
        q.append(int(l))
print(sum(q))
