# Binary search algorithm

# This code searches test_list for the number 6
test_list = [1, 3, 5, 6, 8, 13, 17, 26, 27, 28, 31, 37, 45]

def binary_search(sorted_list, target, steps):
    middle = int( len(sorted_list) / 2 ) # look in the middle of the array
    this_number = sorted_list[middle]
    steps += 1

    if this_number == target:
        print(f"You have found the target!: {target} \n It took {steps} steps.")
        return
    elif this_number > target:
        # Must be smaller
        binary_search(sorted_list[0 : middle], target, steps)
    else:
        # Must be larger
        binary_search(sorted_list[middle : len(sorted_list)], target, steps)

binary_search(test_list, 6, 0)