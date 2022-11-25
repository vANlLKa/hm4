# Написати функцію is_prime, яка приймає 1 аргумент - число від 0 до 1000,
# і повертає True, якщо воно просте, і False - інакше. -> прості числа це числа які
# діляться лише на 1 і на самого себе =)
def is_prime(n:int):
    if n < 1:
        return False
    else:
        for i in range(2,n):
            if n % i == 0 :
                return False
            else:
                return True
number=int(input('введіть число від 0 до 1000 : '))
print(is_prime(number))