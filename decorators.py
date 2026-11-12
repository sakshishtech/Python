def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper


@my_decorator
def greet():
    print("Hello!")


greet()

# output

# Before function
# Hello!
# After function

# A decorator is a function that adds extra functionality to another function without changing its original code.
# @my_decorator is shorthand for --> greet = my_decorator(greet)
