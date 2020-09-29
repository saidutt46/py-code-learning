ex_array = [22, 456, 567, 9876, 7821, 9082, 222, 9872389, 23213]


def num_even_digits():
    finalresult = []
    result = []
    for i in range(len(ex_array)):
        count = 0
        while ex_array[i] > 0:
            ex_array[i] = ex_array[i] // 10
            count += 1
        result.append(count)
    for i in range(len(result)):
        if result[i] % 2 == 0:
            finalresult.append(result[i])
    print(len(finalresult))
    return len(finalresult)


num_even_digits()
