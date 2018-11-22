def calendar(list):
    left_elem = 0
    right_elem = 1
    lenght_of_my_list = len(list)

    elem = 0
    while elem < lenght_of_my_list:
        next_elem = elem + 1
        while next_elem < lenght_of_my_list:
            if list[elem][right_elem] > list[next_elem][right_elem]:
                list.pop(next_elem)
                lenght_of_my_list -= 1
            else:
                if list[elem][right_elem] < list[next_elem][left_elem]:
                    next_elem += 1
                    continue
                else:
                    merged_element = (list[elem][left_elem], list[next_elem][right_elem])
                    list[elem] = merged_element
                    list.pop(next_elem)
                    lenght_of_my_list -= 1
        elem += 1
    return list


my_tuple = [(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)]
print(calendar(my_tuple))