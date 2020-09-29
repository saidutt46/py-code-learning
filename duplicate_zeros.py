

def duplicate_zeros(arr):
    possible_zeros = 0
    length_ = len(arr) - 1
    for left in range(length_ + 1):
        if left > length_ - possible_zeros:
            break
        if arr[left] == 0:
            print(left)
            if left == length_ - possible_zeros:
                arr[length_] = 0
                length_ -= 1
                break
            possible_zeros += 1
# Start backwards from the last element which would be part of new list.
    last = length_ - possible_zeros
    print(f'last {last}')

    # Copy zero twice, and non zero once.
    a = range(last, -1, -1)
    print(a)
    for i in range(last, -1, -1):
        print(i)
        if arr[i] == 0:
            print(arr[i], i)
            arr[i + possible_zeros] = 0
            possible_zeros -= 1
            arr[i + possible_zeros] = 0
        else:
            arr[i + possible_zeros] = arr[i]


duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])


# def duplicate_zeros(arr):
#     shadow_arr = []
#     for i in range(len(arr)):
#         if len(shadow_arr) < len(arr):
#             if arr[i] != 0:
#                 shadow_arr.append(arr[i])
#             else:
#                 shadow_arr.extend([0, 0])
#     print(shadow_arr)
#     arr = shadow_arr
#     print(arr)

# ex_input = [1, 0, 2, 3, 0, 4, 5, 0]
# range (i,j)
#
# def duplicate_zeros():
#     arr_length = len(ex_input)
#     dup_array = []
#     for i in range(arr_length):
#         print(i)
#         if len(dup_array) < arr_length:
#             if i <= arr_length:
#                 if ex_input[i] != 0:
#                     dup_array.append(ex_input[i])
#                 else:
#                     dup_array.extend([0, 0])
#             else:
#                 break
#         else:
#             break
#     print(dup_array)

# for i in range(len(arr)):
#     if len(shadow_arr) < len(arr):
#         if arr[i] != 0:
#             shadow_arr.append(arr[i])
#         else:
#             possible_zeros += 1
#             shadow_arr.extend([0, 0])
# print(shadow_arr)
# print(possible_zeros)


# duplicate_zeros()
