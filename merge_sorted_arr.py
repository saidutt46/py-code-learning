
def merge(nums1, m, nums2, n):
    nums_copy = nums1 + nums2
    nums_copy.sort()
    if m == 0:
        nums1[:] = []
        nums_copy = nums_copy[1:]
        nusm1 = nums_copy
        print(nums_copy)
    elif m and n > 1:
        nums1[:] = []
        for i in nums_copy[m:]:
            nums1.append(i)


merge([0], 0, [1], 1)
