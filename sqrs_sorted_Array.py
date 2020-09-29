ex_array = [-4, -1, 0, 3, 10]


def sqrtsorted_arr():
    unsorted_result = []
    for i in ex_array:
        unsorted_result.append(i**2)
    unsorted_result.sort()
    print(unsorted_result)


sqrtsorted_arr()