age = 18
if age >= 18:
    print("you are adult")

age = 15
if age >= 18:
    print("you are adult")
else:
    print("you are not adult")

marks = 75
if marks >= 75:
    print("A+ grade")
elif marks >= 60:
    print("A grade")
elif marks >= 50:
    print("B grade")
else:
    print("C grade")

fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)
# 1 2 3 4

for i in range(1, 6):
    print(i)
# 2 3 4 5

count = 1
while count <= 5:
    print(count)
    count += 1

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(6):
    if i == 3:
        continue
    print(i)

for i in range(1, 6):
    if i % 2 == 0:
        print(i, 'is even')
    else:
        print(i, 'is odd')
