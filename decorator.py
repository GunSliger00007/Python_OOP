def MyDecorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper
@MyDecorator
def grret():
    print("Hello World")
grret()