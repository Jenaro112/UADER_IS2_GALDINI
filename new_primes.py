import os

lower = 1
upper = 50

os.system("clear")

print("Numeros primeos entre %d y %d son: \n" % (upper, lower))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print("%d " % num, end="")

print()
