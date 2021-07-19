#Created for one argument
def my_map(func, args):
    for value in args:
        yield func(value)

print(list(my_map(lambda x: x + 2, [1,2,4,5,7,8])))

#Created for many args
def my_map_1(func, *values):
    i = 0
    while True:
        try:
            yield func(*[value[i] for value in values])
        except IndexError:
            break
        i += 1


def my_map_2(func, *args):
    count_args = len(args)
    if len(args) == 1:
        min_len = 1
    else:
        min_len = len(args[count_args - 1])
        while count_args >= 0:
            if min_len > len(args[count_args - 2]):
                min_len = len(args[count_args - 2])
            count_args -= 1
    j = 0
    while min_len > 0:
        new_list = []
        i = 0
        while i < len(args):
            new_list.append(args[i][j])
            i += 1
        yield func(*new_list)
        min_len -= 1
        j += 1

list1 = [1,2,3]
list2 = [4,5]

def add_(x, y):
    return x + y
print(list(my_map_2(add_, list1, list2)))