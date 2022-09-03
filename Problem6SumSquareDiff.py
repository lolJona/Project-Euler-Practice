h = 0
for i in range(1, 101):
    h += i**2
k = 0
for j in range(1, 101):
    k += j
print(k)
l = k**2
m = l - h
print(m)
