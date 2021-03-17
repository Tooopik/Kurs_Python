import time


def function_performace(func, arg, arg2, how_many_times=1):
    sum = 0
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg, arg2)
        stop = time.perf_counter()
        sum = sum + (stop - start)
    return sum


def is_element_in(number, gen):
    if number in gen:
        return "Yes"

    else:
        return "No"


setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]

print("SET :", is_element_in(1010, setContainer))
print("SET TIME :", function_performace(
    is_element_in, 1010, setContainer, 500000))

print("LIST :", is_element_in(1010, listContainer))
print("LIST TIME :", function_performace(
    is_element_in, 1010, listContainer, 500000))
