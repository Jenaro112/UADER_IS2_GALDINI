import os
import sys

lower = 1

if len(sys.argv) > 1:
    upper = int(sys.argv[1])
else:
    upper = 50

os.system("clear")

print("Numeros primos entre %d y %d son: \n" % (lower, upper))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print("%d " % num, end="")

print()
