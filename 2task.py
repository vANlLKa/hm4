# Написати функцію аритметичного, що приймає 3 аргументи: перші 2 - числа,
# третій - операція, яка повинна бути проведена над ними.
# Якщо третій аргумент +, скласти їх; якщо -, то відняти; * - помножити; /
# - Розділити (перше на друге). В інших випадках повернути рядок
# "Невідома операція".
def функція(a,b,c,sum=0):
    if c == '+':
        sum = a + b
    elif c == '-':
        sum = a - b
    elif c == '*':
        sum = a * b
    elif c == "/":
        try:
            sum= a / b
        except ZeroDivisionError as err:
            print(err)
    else :
        print('я не знаю такої дії =(')
    return sum
first = int(input("введіть число: "))
second = int(input("введіть друге число: "))
third = input("ведіть дію: ")
print(функція(first, second, third))