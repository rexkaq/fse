import sys
a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
if a > 1000:
    print("Неверное число")
    sys.exit()
elif a < 0:
    print("Неверное число")
    sys.exit()
if b > 1000:
        print("Неверное число")
        sys.exit()
elif b < 0:
        print("Неверное число")
        sys.exit()
if a >b:
    print("Первое число больше второго")
elif a == b:
    print("Числа равны")
else:
    print("Второе число больше первого")
