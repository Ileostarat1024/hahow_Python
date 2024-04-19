import time

def count_time(func):
    def inner():
        start = time.time()
        print('running',func.__name__)
        func()
        end = time.time()
        print('elapsed',end - start, 'seconds')
    return inner


def say_hi():
    print('hi')

def say_yes():
    print('yes')

say_hi = count_time(say_hi)
say_yes = count_time(say_yes)
say_hi()
say_yes()

