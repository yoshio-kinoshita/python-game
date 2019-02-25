a = 3

if a:
    print("true")
else:
    print("false")

print(a)

print(bool(0.0))
print(bool(3.14))
print(bool({}))
print(bool({1, 2, 3}))
print(bool({"hello"}))
print(bool(""))

x = 10 if a > 0 else 20
print(x)

counter = 0

while counter < 3 :
    print(counter)
    counter += 1

total = 0
index = 0
subject = (78, 95, 68, 62)

while index < len(subject):
    total += subject[index]
    index += 1

average = total / len(subject)
print(average)

total = 0
for score in subject:
    total += score
average = total / len(subject)
print(average)

for letter in "hi!":
    print(letter)

is_even = lambda x: x % 2 == 0
print(is_even(2))
print(is_even(3))
lambda name: print("Hi!" + name)
