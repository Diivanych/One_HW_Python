def step(a, b):
    c = 1
    if b == 0:
        return 1
    else:
        print(f'a = {a}')
        print(f'b = {b}')
        return step((a), (b - c)) * a
print(step(2, 3))
