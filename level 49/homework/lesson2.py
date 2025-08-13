def square(sq):
    if (square := sq ** 0.5) * square == sq:
        return square
    else: return sq ** 2
print(square(16))