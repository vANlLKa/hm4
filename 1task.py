# Напишіть функції sum_range(start, end), яка сумує всі цілі числа від
# значення start до end включно. Якщо користувач задасть перше число більше ніж друге
# просто поміняйте їх місцями

def sum_range(start,end,sum=0):
    if start > end:
        for ch in range(end-1, start+1):
            sum += ch
    else:
        for i in range(start-1,end+1):
            sum += i
    return sum
start = int(input("введіть перше число: "))
end = int(input("введіть друге число: "))
print(sum_range(start,end))