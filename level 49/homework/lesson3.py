def odd_even(num_list):
    res = []
    for x in num_list:
        if x % 2 != 0 and num_list.index(x) % 2 == 0:
            res.append(x)
    return res
print(odd_even([1,2,3,4,5,6,7,8]))