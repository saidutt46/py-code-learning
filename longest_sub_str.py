def longest_sub_str(s):
    dct = {}
    max_so_far = curr_max = start = 0
    for index, i in enumerate(s):
        if i in dct and dct[i] >= start:
            max_so_far = max(max_so_far, curr_max)
            curr_max = index - dct[i]
            start = dct[i] + 1
        else:
            curr_max += 1
        dct[i] = index
    return max(max_so_far, curr_max)


# def longest_sub_str(s):
#     h = {}
#     counter = 0
#     for index in range(len(s)):
#         counter += 1
#         if index == len(s) - 1:
#             print(counter)
#             return
#         else:
#             if s[index] in h:
#                 if index < len(s):
#                     print(s[index + 1:len(s)])
#                     longest_sub_str(s[index + 1: len(s)])
#             else:
#                 h[s[index]] = index
#                 print(h)


# longest_sub_str('pwwkew')
longest_sub_str('abcabcbb')
