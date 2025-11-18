def greet():
    print('hello, welcome to python')


greet()


def greet0(name):
    print('hello', name)


greet0('kalum')


def add(a, b):
    print(a+b)


add(5, 10)


def add(a, b):
    return a + b


result = add(10, 20)
print(result)


def greet(name="Guest"):
    print("Hello", name)


greet()        # Uses default
greet("Kalum")  # Uses provided value


def student_info(name, age):
    print(name, age)


student_info(age=22, name="Alex")


def total(*numbers):
    print(sum(numbers))


total(1, 2, 3, 4)


def show_details(**info):
    print(info)


show_details(name="Kalum", age=25, country="Sri Lanka")


def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b


def square(x): return x * x


print(square(5))


def find_large(a, b):
    if a > b:
        return a
    else:
        return b


print(find_large(10, 20))
