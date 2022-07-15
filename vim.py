def say_goodbye():
    yield "never"
    yield "gonna"
    yield "give"
    yield "you"
    yield "up"


x = say_goodbye()
print(next(x))
