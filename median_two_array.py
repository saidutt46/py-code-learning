def find_median(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    nums1_copy = nums1[:m]
    nums1[:] = []
    p1 = 0
    p2 = 0

    while p1 < m and p2 < n:
        if nums1_copy[p1] < nums2[p2]:
            nums1.append(nums1_copy[p1])
            p1 += 1
        else:
            nums1.append(nums2[p2])
            p2 += 1

    if p1 < m:
        nums1[p1 + p2:] = nums1_copy[p1:]
    if p2 < n:
        nums1[p1 + p2:] = nums2[p2:]

    if len(nums1) % 2 == 0:
        print('even executing')
        g = nums1[int(len(nums1) / 2)] + nums1[int(len(nums1) / 2) - 1]
        return g / 2
    else:
        print('executing')
        return nums1[int(len(nums1) / 2)]


print(find_median([1, 2], [3, 4]))
