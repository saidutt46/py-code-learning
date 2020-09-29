def longest_prefix(container):
    x = min(container, key=len)
    op_string = ''
    smallest_index = container.index(x)
    for high, val in enumerate(container):
        if high != smallest_index:
            if val[0] != x[0]:
                return ''
            else:
                print('calculating')
                for low, lil_val in enumerate(container):
                    print(low)


longest_prefix(["abower","flow","flight"])