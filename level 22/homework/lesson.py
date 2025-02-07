a = int(input("შეიყვანეთ a: "))
b = int(input("შეიყვანეთ b: "))

if a > b:
    for num in range(b + 1, a):
        print(num)
else:
    print("არასწორი შეყვანა! a უნდა იყოს მეტი ვიდრე b.")