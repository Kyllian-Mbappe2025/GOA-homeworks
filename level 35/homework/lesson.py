# 1)შექმენით სია სადაც შეინახავთ რიცხვებს, შემდგომ დაპირნტეთ ამ სიის სიგრძე გამრავლებული ორზე
numbers = [1,2,3,4,5]
print(len(numbers) * 2)


# 2)შექმენით სახელებით სავსე სია, შემდეგ აქედან ამოაგდეთ ლუწ ინდექსე მდგომი ელემენტები
names = ["saba", "sandro", "nika", "luka", "levani"]
filtered_names = []

for i in range(len(names)):
    if i % 2 == 1:
        filtered_names.append(names[i])
print(filtered_names)



# 3) შექენით  რიცხვებით, სახელებით, ათწილადებით სავსე სია და ამ სიას for loop ით გადაუარეთ და ამავე სიაში მეორეჯერ დაამატეთ ყველა სტრინგ ტიპის ელემენტები
array = ["sandro", 5, 2.6, "saba", "nika", "dog", True]
for i in range(len(array)):
    if type(array[i]) == str(array[i]):
        array.append(i)
print(array)


# 4) შექმენი ორი სია, ერთი სახელებით სავსე მეორე ცარიელი, პირველიდან მეორეშ ჩაამატე ყველა სახელი მაგრამ დიდი ასოებით(დაგჭირდებათ append და upper)
sec_names = ["saba", "lUKa", "sandro", "NIka", "levani"]
second_result = []

for name in sec_names:
    second_result.append(name.upper())
print(second_result)