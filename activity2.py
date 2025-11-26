marks = []

for i in range(10):
    mark = float(input(f'enter mark of student {i+1}: '))
    marks.append(mark)

maximum = max(marks)
minimum = min(marks)
average = sum(marks)/len(marks)

print('maximum mark: ', maximum)
print('minimum mark: ', minimum)
print('average: ', average)
