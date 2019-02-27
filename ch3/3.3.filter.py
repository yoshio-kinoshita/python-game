# filter(要素を選ぶ関数、　配列)

print(list(filter(lambda a: a % 2 == 0, [0, 1, 2, 3, 4, 5])))

print(list(filter(lambda a: a % 2 == 1, [0, 1, 2, 3, 4, 5])))
print(list(filter(lambda a: a % 3 == 0 and a != 0, [0, 1, 2, 3, 4, 5])))
