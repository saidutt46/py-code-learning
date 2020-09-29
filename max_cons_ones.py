my_list = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0]
nancy = []


def max_cons():
    # initialize count
    count = 0

    # initialize max
    result = 0
    n = len(my_list)

    for i in range(0, n):

        # Reset count when 0 is found
        if my_list[i] == 0:
            count = 0

        # If 1 is found, increment count
        # and update result if count
        # becomes more.
        else:

            # increase count
            count += 1
            result = max(result, count)
            print(result)

    print(result)
    return result


max_cons()
