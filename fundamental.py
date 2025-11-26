no1 = int(input('enter a number: '))
no2 = int(input('enter 2nd number: '))
sum = no1+no2
print(sum)


age = int(input('enter your age: '))
if age < 13:
    print('child')
elif age < 20:
    print('teenager')
else:
    print('adult')


no = 1
while no <= 10:
    print(no)
    no = no+1


def add(no1, no2, no3):
    sum = no1+no2+no3
    return sum


print(add(90, 50, 30))