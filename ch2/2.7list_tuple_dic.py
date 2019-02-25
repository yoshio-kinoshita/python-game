# タプル
subject = (78, 95, 68, 62)
# subject[0] = 82
total = subject[0] + subject[1] + subject[2] + subject[3]
average = total / 4
print(average)

# リスト
subject = [78, 95, 68, 62]
subject[0] = 82
total = subject[0] + subject[1] + subject[2] + subject[3]
average = total / 4
print(average)

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
scores = [98, 68, 72, 59, 89, 48, 39, 85]
animals = ["horse", "rabbit", "lion", "elephant", "mouse"]

print(scores[1])
scores[1] = 77
print(scores)

weekdays.append("Saturday")
print(weekdays)

animals.insert(3, "Rhino")
print(animals)

del animals[2]
print(animals)

score = {
    "math": 78,
    "english": 95,
    "chemistry": 68,
    "science": 62
}

print(score)
print(score["english"])

score["math"] = 82
print(score)
