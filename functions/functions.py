def function_name(parameters):
    print(parameters + 2)


function_name(5)


def default_example(num1=7, num2=8):
    print(num1 * num2)


default_example()
default_example(2)  # 16
default_example(2, 6)  # 12
default_example(num2=3)


def default_example_2(num1=7, num2=8):
    return num1 * num2


print(default_example_2() + 44)  # 100


# Exercise
def hello_world_printer():
    print("hello world")


hello_world_printer()


def name_printer(name):
    print(name)


name = input("type your name")
name_printer(name)
