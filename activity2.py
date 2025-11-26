# ---b---
marks1 = []

for i in range(10):
    mark = float(input(f'enter mark of student {i+1}: '))
    marks1.append(mark)

maximum = max(marks1)
minimum = min(marks1)
average = sum(marks1)/len(marks1)

print('maximum mark: ', maximum)
print('minimum mark: ', minimum)
print('average: ', average)

# ---c---


def get_grade(mark):
    if mark > 75:
        return 'A'
    elif 65 <= mark <= 75:
        return 'B'
    elif 55 <= mark <= 64:
        return 'C'
    elif 45 <= mark <= 54:
        return 'S'
    else:
        return 'F'


marks2 = []

for i in range(5):
    mark = float(input(f'enter mark {i+1}: '))
    marks2.append(mark)

print('\n grade for the fice marks:')
for i, mark in enumerate(marks2, start=1):
    print(f'mark {i}: {mark} -> grade: {get_grade(mark)}')
