
# 1 Поработайте с переменными, создайте несколько, выведите на экран. Запросите у
# пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.

a = 4
b = 3
print(a, b)

strings = input("Please enter words: ")
integers = int(input("Please enter numbers: "))
print(strings)
print(integers)

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.

time_in_sec = int(input("Please enter the time in sec: "))
hours = time_in_sec // 3600
seconds = time_in_sec % 3600
minutes = seconds//60
seconds = seconds % 60
print("%d:%d:%d" % (hours, minutes, seconds))

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
# ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input("Please enter number: ")
nn = n + n
nnn = nn + n
n = int(n)
nn = int(nn)
nnn = int(nnn)
sum = n + nn +nnn
print("%d + %d + %d = %d" % (n, nn, nnn, sum))

# 4 . Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Please enter number: "))
if number > 0:
    i = 0
    total = 0
    maximum = None
    while i < number:
       y = number - i
       total = total + y
       # print(y)
       if maximum is None or maximum < y:
           maximum = y
       i = i+1

    print(maximum, total)
else:
    print("Please enter number more than 0")

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
# финансовым результатом работает фирма. Например, прибыль — выручка больше издержек,
# или убыток — издержки больше выручки. Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение
# прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль
# фирмы в расчёте на одного сотрудника.


proceeds = int(input("Please enter company proceeds: "))
costs = int(input("Please enter company costs: "))
if proceeds > costs:
    print("Компания прибыльна")
    profit = proceeds-costs
    profitability = profit / proceeds
    quantity_employees = int(input("Quantity employees: "))
    profit_per_employee = profit / quantity_employees
    print(profitability)
    print(profit_per_employee)
else:
    print("Компания убыточна")
'''
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a
километров. Каждый день спортсмен увеличивал результат на 10% относительно
предыдущего. Требуется определить номер дня, на который результат спортсмена составит не
менее b километров. Программа должна принимать значения параметров a и b и выводить
одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на шестой день спортсмен достиг результата — не менее 3 км.
'''
a = int(input("Please enter number for a: "))
b = int(input("Please enter number for b: "))
if a <= b:
    count = 1
    print(count, "-й день:", a)
    while a <= b:
        a = a + (a * 0.1)
        count = count +1
        print(count, "-й день:", "{:.2f}".format(a))
    print("Ответ на ", count, "-й день спортсмен достиг результата - не менее ", b, "км")
else:
    print("Please enter 'a' less than 'b'")
