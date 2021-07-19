def my_range(start, stop=None, step=1):
    if not stop:
        stop = start
        start = 0
    i = start
    while True:
        yield i
        i += step
        if i >= stop:
            break


for i in range(4):
    print(i)