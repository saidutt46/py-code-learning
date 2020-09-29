def max_water(height):
    min_, max_ = 0, len(height) - 1
    areas = 0
    while min_ != max_:
        if height[min_] < height[max_]:
            areas = max((max_ - min_) * height[min_], areas)
            min_ += 1
        else:
            areas = max((max_ - min_) * height[max_], areas)
            max_ -= 1
    print(areas)
    return areas

    # BRUTE FORCE
    # water_area = []
    # for up_index, up_val in enumerate(height):
    #     for low_index, low_val in enumerate(height):
    #         if up_index != low_index:
    #             if up_val < low_val:
    #                 width = up_val
    #                 if up_index < low_index:
    #                     calc_diff = up_index - low_index
    #                     water_area.append(width * abs(calc_diff))
    #                 else:
    #                     calc_diff = low_index - up_index
    #                     water_area.append(width * abs(calc_diff))
    #             if up_val == low_val:
    #                 if up_index < low_index:
    #                     calc_diff = up_index - low_index
    #                     water_area.append(low_val * abs(calc_diff))
    #                 else:
    #                     calc_diff = low_index - up_index
    #                     water_area.append(low_val * abs(calc_diff))
    #             if up_val > low_val:
    #                 width = low_val
    #                 if up_index < low_index:
    #                     calc_diff = up_index - low_index
    #                     water_area.append(width * abs(calc_diff))
    #                 else:
    #                     calc_diff = low_index - up_index
    #                     water_area.append(width * abs(calc_diff))
    # sorted_list = sorted(water_area)
    # return sorted_list[-1]


max_water([1,8,6,2,5,4,8,3,7])