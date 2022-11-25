# Напишіть функції sum_range(start, end), яка сумує всі цілі числа від
# значення start до end включно. Якщо користувач задасть перше число більше ніж друге
# просто поміняйте їх місцями
start = int(input('введіть перше число: '))
end = int(input('введіть друге число:'))
sum = 0
if start > end :
    for i in range(end-1,start+1):
        sum += i
else:
    for i in range(start-1, end+1):
        sum += i
print('сума чисел в першого до другого :',sum)