# # Задача 2: Найдите сумму цифр трехзначного числа.

# a = input('Введите число (по задаче трехзначное): ')
# sum = 0

# for i in a:
#     sum += int(i)
# print(str(sum) + ' (' + ' + '.join(map(str,a)) + ')')

# # Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# # Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# # а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# s = int(input ('Сколько журавликов сделали ребята всего? '))
# peter = s / 6
# serjey = peter
# kate = (peter + serjey) * 2
# print(f"Петя - {int(peter)}, Катя - {int(kate)}, Сережа - {int(serjey)}")

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

ticketNum = input('Введите номер своего билета: ')
if len(str(ticketNum)) == 6:
    sumA = 0
    sumB = 0
    
    a = ticketNum[:3]
    b = ticketNum[3:]

    for i in a:
        sumA += int(i)
    for i in b:
        sumB += int(i)

    if sumA == sumB:
        print('yes')
    else:
        print('no')
else:
    print('no')