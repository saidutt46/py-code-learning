
def two_sum(nums, target):
    h_map = {}
    for index, num in enumerate(nums):
        answer = target - num
        if answer in h_map:
            print([h_map[answer], index])
            return [h_map[answer], index]
        else:
            h_map[num] = index


two_sum([3, 2, 4, 9, 12, 78, 79, 67, 34, 90, 45, 65, 12], 46)
