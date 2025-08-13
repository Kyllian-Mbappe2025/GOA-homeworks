def Odds(lst):
    save = []
    for i in lst: 
        if i % 2 != 0:
            save.append(i)
    return save

print(Odds([1,5,9,13,18]))