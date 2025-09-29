'''
array = []
num = int(input("Введите кол-во чисел:"))

i = 0

while True:
    n = int(input(f"Введите число:"))
    if n == 0: break
    array.append(n)
    i += 1

total = 0
for nam in range (len(array)):
    total += int(array[nam])
'''


num = input("Введите число:")
res = 0
for i in num:
    res += int(i)
print(res)