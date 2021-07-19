#example 1
def zip_generator_1(*args):
    count_args = len(args)

    min_len = len(args[count_args - 1])

    while count_args >= 0:
        if min_len > len(args[count_args - 2]):
            min_len = len(args[count_args - 2])
        count_args -= 1


    i = min_len - 1
    while i >= 0:
        yield [arg[i] for arg in args]
        i -= 1
#example 2
def zip_generator_2(*args):
    min_len = len(args[0])
    for iterable in args:
        if len(iterable) < min_len:
            min_len = len(iterable)
    # or min_len = min([len(arg) for arg in args])
    for i in range(min_len):
        result = []
        for arg in args:
            result.append(arg[i])
        x = tuple(result)
        yield x
list1 = [1,2,3,4]
list2 = [4,7,6,7,8,]
list3 = [1,2,4]


for couple in zip_generator_2(list1, list2, list3):
    print(couple)