number = 5
# в двоичной 5 = 101
numbers = []


def look_for_count_number(str):
    start_index = 1

    divide_count = 0

    while start_index <= str.__len__():
        # если есть совпадение
        if str[:start_index] in numbers:
            # if the whole string matches powered number, the minimum number of dividing is 1
            if start_index is str.__len__():
                return 1

            divide_count_of_right_str_part = look_for_count_number(str[start_index:])

            # otherwise check if right part can be divided and assign
            if divide_count_of_right_str_part is not 0:
                if divide_count is 0 or divide_count > divide_count_of_right_str_part + 1:
                    divide_count = divide_count_of_right_str_part + 1

        start_index += 1
    return divide_count


def making_list_of_our_numbers(n):
    i = 0
    binary_number = ""
    while binary_number.__len__() <= 100:
        powered_number = pow(n, i)
        binary_number = bin(powered_number)[2:]
        numbers.append(binary_number)
        i += 1


making_list_of_our_numbers(number)
print(look_for_count_number('110011011'))