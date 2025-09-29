'''
message = "Hello"
for c in message:
    print(c)
else:
    print(f"Последний символ: {c}. Цикл завершен");
print("Работа программы завершена")
'''

'''
i = 1
j = 1
while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1
'''

'''
while True:
    num1 = int(input("Введите первое число:"))
    num2 = int(input("Введите второе число"))
    print("Сумма чисел:", num1 + num2)
    str = input ("Чтобы завершить нажмите Y")
    if (str =="Y" or str =="y"): break
'''

'''
def main():
    hai()
    davai()

def hai():
    print("Hello")

def davai():
    print("Good Bye")

main()
'''

'''
def print_person(name = "Tom", age = 18):
    print(f"Name: {name}  Age: {age}")



print_person()
print_person("Bob")
print_person("Sam", 37)

'''

def print_person(*, name, age, company):
    print(f"Name: {name} Age: {age}  Company: {company}")

print_person(age = 22, company ="Google")