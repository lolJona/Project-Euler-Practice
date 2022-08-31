"""
I'm sure I can do this with a while loop, 
along with adding something along the lines of fiblist[-1] and fiblist[-2]
and evaluating and appending if the resultant value evaluates to < 4000000
but I can't figure out how to implement it.  Thoughts?

This gives the correct answer but is far from elegant or efficiently written.
"""

fibsum = 0
fiblist = [1, 2]
num1 = 1
num2 = 2
val1 = num1 + num2
fiblist.append(val1)
print(val1)
num1 = val1
print(num1)
val2 = num1 + num2
fiblist.append(val2)
num2 = val2
val1 = num1 + num2
fiblist.append(val1)
num1 = val1
val2 = num1 + num2
fiblist.append(val2)
num2 = val2
val1 = num1 + num2
fiblist.append(val1)
num1 = val1
val2 = num1 + num2
fiblist.append(val2)
num2 = val2
val1 = num1 + num2
fiblist.append(val1)
num1 = val1
val2 = num1 + num2
fiblist.append(val2)
num2 = val2
val1 = num1 + num2
fiblist.append(val1)
num1 = val1
val2 = num1 + num2
fiblist.append(val2)
num2 = val2
val1 = num1 + num2
fiblist.append(val1)
num1 = val1
val2 = num1 + num2
fiblist.append(val2)
num2 = val2
val1 = num1 + num2
fiblist.append(val1)
num1 = val1
val2 = num1 + num2
fiblist.append(val2)
num2 = val2
val1 = num1 + num2
fiblist.append(val1)
num1 = val1
val2 = num1 + num2
fiblist.append(val2)
num2 = val2
val1 = num1 + num2
fiblist.append(val1)
num1 = val1
val2 = num1 + num2
fiblist.append(val2)
num2 = val2
val1 = num1 + num2
fiblist.append(val1)
num1 = val1
val2 = num1 + num2
fiblist.append(val2)
num2 = val2
val1 = num1 + num2
fiblist.append(val1)
num1 = val1
val2 = num1 + num2
fiblist.append(val2)
num2 = val2
val1 = num1 + num2
fiblist.append(val1)
num1 = val1
val2 = num1 + num2
fiblist.append(val2)
num2 = val2
val1 = num1 + num2
fiblist.append(val1)
num1 = val1
val2 = num1 + num2
fiblist.append(val2)
num2 = val2
val1 = num1 + num2
fiblist.append(val1)
num1 = val1
val2 = num1 + num2
fiblist.append(val2)
num2 = val2
val1 = num1 + num2
fiblist.append(val1)
num1 = val1
val2 = num1 + num2
fiblist.append(val2)
num2 = val2
print(fiblist)
for fib in fiblist:
    if fib % 2 == 0:
        fibsum += fib
print(fibsum)
