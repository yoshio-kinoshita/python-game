# map(処理を行う関数、 list or tuple)

def make_double(x):
    return x * 2

print(list(map(make_double, [1, 2, 3])))

print(list(map(lambda x: x * 2, [1,2,3])))
