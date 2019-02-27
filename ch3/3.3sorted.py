# sorted ソートします。

a = [7, 4, 3, 1, 5]
print(sorted(a))
print(a)

print(sorted(a, reverse=True))

s = ["banana", "apple", "peach"]
print(sorted(s))
print(sorted(s, reverse=True))

# 内包表記
# [式 for 要素名 in リスト]

print([x * 2 for x in [1, 2, 3,4]])
print([x**2 for x in range(5)])