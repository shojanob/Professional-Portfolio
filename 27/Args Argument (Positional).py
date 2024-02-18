def add(*args):
    print(args[0])

    sum = 0
    for n in args:
        sum += n
    return sum

print(add(5,3,2,1))