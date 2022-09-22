import itertools                          #Iterable tools module allows for easy permutations
numlist = str(1234567890)                 
numlist1 = str(123)                       #Just to test with a smaller list
k = itertools.permutations(numlist)       #Permutates the "list" which is actually a string
k = list(k)
k = ["".join(perm) for perm in k]
j = sorted(k)                             #Line 5 converts the perms to a list form, 6 adds them to the list, 7 sorts
print(j[999999])
