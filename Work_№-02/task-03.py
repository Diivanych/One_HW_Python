'''
def math(op, x, y):
    print(op(x, y))


calc1 = lambda a, b: a * b

math(lambda a, b: a * b, 10, 40)
'''
# -------------------------------------------------
'''
data = [1, 2, 3, 5, 8, 15, 23, 38]
out = []
for i in data:
    if i % 2 == 0:
        out.append((i, i ** 2))
print(*out)
'''
# -------------------------------------------------
'''
def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]

res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res) # [2, 8, 38]
res = list(select(lambda x: (x, x ** 2), res))
print(res)
'''
# -------------------------------------------------
'''
list_1 = [x for x in range (1,20)]
print(list_1)
list_1 = list(map(lambda x: x * 10, list_1 ))
print(list_1)
'''
# -------------------------------------------------
data = '15 156 96 5 3 8 52 5'
print(data)

# data = data.split()
# print(data) # ['1', '2', '3', '5', '8', '15', '23', '38']

data = list(map(int,data.split()))
print(data)