#Far from elegant, or efficient, but it eventually gets the job done 🤷‍♂️

import statistics
plist = []
for a in range(1, 1000):
    for b in range(1, 1000):
        for c in range(1, 1000):
            if (a**2 + b**2 == c**2) and (a + b + c <= 1000):
                p = str(a + b + c)
                plist.append(int(p))
print(statistics.mode(plist))
