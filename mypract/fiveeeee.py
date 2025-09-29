array = []
n = int(input('Введите количество чисел списка:'))

for e in range(n):
    num = int(input(f"Введи {e + 1}-e число: "))
    array.append(num)
print(f"Ваш Массив: {array}")


total_sum = sum(array)
print(f"Сумма элементов массива: {total_sum}")


average = total_sum / len(array)
print(f"Среднее арифметическое: {average}")


max_number = max(array)
min_number = min(array)
print(f"Максимальное число массива: {max_number}")
print(f"Минимальное число массива: {min_number}")


negative_count = 0
for number in array:
    if number < 0:
        negative_count += 1
print(f"Количество отрицательных чисел в списке: {negative_count}")

positive_count = 0
for number in array:
    if number > 0:
        positive_count += 1
print(f"Количество положительных чисев в списке: {positive_count}")


