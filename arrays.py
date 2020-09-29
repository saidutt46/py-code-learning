my_list = [1, 1, 0, 1, 1, 1, 0,1,1,1,1,1,0]
nancy = []


def max_cons():
    # intitialize count
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
# def max_cons():
#     current_window = 0
#     for i in my_list:
#         if i == 1:
#             print(my_list[i])
#             current_window += current_window
#             print(current_window)
#     windows.append(current_window)
#     windows.sort()
#     print(windows[-1])
#
#
# max_cons()

"""
class Car:
    def __init__(self, name, brand, engine, hp):
        self.name = name
        self.brand = brand
        self.engine = engine
        self.hp = hp

    @property
    def description(self):
        return f'The car is {self.name} coming from {self.brand} with a {self.engine} engine generating {self.hp}'


audi = Car('CLE 300', 'Mercedes Benz', 'I4', 241)
prod_line = [Car] * 10
prod_line[1] = audi
prod_line[0] = Car('BMW 330i', 'BMW', 'I4', 255)
print(prod_line[0].description)
print(prod_line[1].description)
print(prod_line[5])
"""
