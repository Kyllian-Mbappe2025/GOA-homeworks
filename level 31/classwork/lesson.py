def four_numbers_sum(a, b, c, d):
    sum_result = a + b + c + d
    return sum_result
print(four_numbers_sum(14, 8, 15, 11))

def func1(word, times):
    return word * times
print(func1("Hala Madrid", 3))

def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '':
        return num1 - num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "ნულზე გაყოფა არ შეიძლება"
    else:
        return "არასწორი ოპერატორი"
print(calculator(10, 5, '+'))  # 15
print(calculator(10, 5, '-'))  # 5
print(calculator(10, 5, '*'))  # 50
print(calculator(10, 5, '/'))  # 2.0
print(calculator(10, 0, '/'))  # "ნულზე გაყოფა არ შეიძლება"
print(calculator(10, 5, '^'))  # "არასწორი ოპერატორი"

def func2(price, fasdakleba, money):
    final_price = price - fasdakleba
    if money >= final_price:
        return "გეყოფა ფული"
    else:
        return "არ გეყოფა ფული"
print(func2(100, 20, 90))   # "გეყოფა ფული"
print(func2(150, 50, 70))   # "არ გეყოფა ფული"
