from algoritms.student import Student


def bubble_sort(my_sorting_list):
    comparisons = 0
    swaps = 0
    for i in range(len(my_sorting_list)):
        for j in range(0, len(my_sorting_list) - i - 1):
            if my_sorting_list[j].rate > my_sorting_list[j + 1].rate:
                comparisons += 1
                my_sorting_list[j], my_sorting_list[j + 1] = my_sorting_list[j + 1], my_sorting_list[j]
                swaps += 1

    print("Comparisons = " + str(comparisons))
    print("Swaps = " + str(swaps))


comparisons = 0


def quicksort(nums, fst, lst, comparisons):
    if lst - fst < 1:
        return

    swaps = 0
    i = fst + 1
    j = lst
    pivot = nums[0].height

    while True:
        while nums[i].height < pivot and i < lst:
            i += 1
            comparisons += 1

        while not nums[j].height < pivot and j > fst:
            j -= 1
            comparisons += 1

        if i >= j:
            break

        nums[i], nums[j] = nums[j], nums[i]
        swaps += 1
    nums[fst], nums[j] = nums[j], nums[fst]
    swaps += 1
    quicksort(nums, fst, j - 1, 0)
    quicksort(nums, j + 1, lst, 0)

    print("Comparisons = " + str(comparisons))
    print("Swaps = " + str(swaps))
