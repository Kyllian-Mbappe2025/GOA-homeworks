def operation(int1,int2,operator):
    if operator == "+":
        return int1 + int2
    elif operator == "-":
        return int1 - int2
    elif operator == "/":
        return int1 / int2
    else: int1 * int2

print(operation(2,2,"+"))