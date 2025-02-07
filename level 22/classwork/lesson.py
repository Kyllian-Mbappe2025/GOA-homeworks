score = int(input("Enter your exam score: "))  # მომხმარებლისგან ქულის მიღება

if score == 10 or score == 9:
    print("A")
elif score == 8 or score == 7:
    print("B")
elif score == 6 or score == 5:
    print("C")
else:
    print("You did not pass")  # თუ 5-ზე ნაკლებია

