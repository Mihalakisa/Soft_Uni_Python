def uppercase(function):
    def wrapper():
        result = function()
        uppercase_result = result.upper()
        return uppercase_result

    return wrapper


@uppercase  # <-- Decorator
def say_hi():
    return 'hello there'


@uppercase  # <-- Decorator
def say_buy():
    return 'Buy this'


def say_hello():
    return "I say hello"


decorate = uppercase(say_hello)
print(decorate())

print(say_hi())
print(say_buy())
