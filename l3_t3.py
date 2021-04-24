def my_func(*args):
    v = list(args)
    v.sort()
    return sum(v[-1:])


print(my_func(1, 2, 6))
