#ფუნქცია შეიძლება დააბრუნოს შედეგი ან უბრალოდ გააკეთოს რაღაც მოქმედება, მაგალითად, მონაცემების გამოკითხვა ან ჩამოყალიბება.
#ფუნქცია არის კოდის ნაწილი, რომელიც ასრულებს გარკვეულ დავალებას და შეიძლება შეიცავდეს ერთ ან მეტ არგუმენტს.

def add_numbers(x, b):
    # ორ არგუმენტს ვამატებთ ერთმანეთს
    return x + b
result = add_numbers(10, 6)
print(result)  #16

def Hello(name):
    # გადაცემული სახელის დაბეჭდვა
    print(f"Hello, {name}!")

Hello("შენივე სახელი")  # მაგ: Hello, Son ki gun!
def Multiply_Number(x, b):
    # ორ არგუმენტს ვამრავლებთ
    return x * b  

result = Multiply_Number(4, 5)
print(result)  # 20

def arithmetic_operations(x, y, z, w):
    # ყველა ოპერაციის შესრულება
    addition = x + y + z + w
    subtraction = x - y - z - w
    multiplication = x * y * z * w

    # დაყოფის ოპერაცია, სადაც თავიდან აცილებთ ხარვეზებს
    if y != 0 and z != 0 and w != 0:
        division = x / y / z / w
    else:
        division = "Cannot divide by zero"

    return addition, subtraction, multiplication, division

add, sub, mul, div = arithmetic_operations(10, 5, 2, 1)
print(f"Addition: {add}, Subtraction: {sub}, Multiplication: {mul}, Division: {div}")    
  
