Ps5_games = [1,2,3,4,5,6,7,8,9,10]
Ps5_games [4] = "GTA VI"
Ps5_games [5] = "FC26"
Ps5_games [6] = "W2k25"
Ps5_games [7] = "NBA2k26"
Ps5_games [8] = "CAll OF DUTY BLACK OPS 6"
Ps5_games [9] = "SPIDER-MAN 2"
print(Ps5_games [5:10])

# Python-ში slicing (ნაწილობრივი ამოჭრა) ძალიან სასარგებლო მეთოდია,
# რომელიც გამოიყენება სიების (lists),
# სტრიქონების (strings) და სხვა მიმდევრობითი მონაცემთა სტრუქტურების
# (tuples, ranges) ნაწილობრივ ამოსაჭრელად. ქვემოთ მოცემულია კოდი კომენტარებით,
# რომელიც განმარტავს slicing-ის გამოყენებას:

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reversed_list = []  # ცარიელი სია, სადაც შევინახავთ შებრუნებულ მონაცემებს
for i in range(len(my_list) - 1, -1, -1):  # ვიწყებთ ბოლო ინდექსიდან (9) და მივდივართ 0-მდე
        reversed_list.append(my_list[i])  # ვამატებთ ელემენტებს შებრუნებული მიმდევრობით
print(reversed_list)  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

Football = [1,2,3,4,5,6,7,8,9,10]
Football [0] = "Camavinga"
Football [1] = "Vinicius"
Football [2] = "Mbappe"
Football [3] = "Bellingham"
Football [4] = "Tchouameni"
Football [5] = "Valverde"
Football [6] = "Guller"
Football [7] = "Rodrygo"
Football [8] = "Modirc"
Football [9] = "Carvajal"
print(Football)

# list–შეიძლება შეიცავდეს სხვადასხვა ტიპის მონაცემებს:(int, float, string, list, tuple და სხვ.).
# string –შეიცავდეს მხოლოს სიმბოლოებს,და მისი შიგთავსის შეცვლა შეუძლებელია.