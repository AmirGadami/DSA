def bubble_sort(my_list):
    """
    Bubble Sort: Repeatedly swaps adjacent elements if they are in the wrong order.
    Time Complexity: O(n^2)
    """
    for i in range(len(my_list)-1, 0, -1):  # Shrinks the unsorted portion
        for j in range(i):  # Iterate from 0 to i-1
            if my_list[j] > my_list[j+1]:  # Swap if out of order
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list


def selection_sort(my_list):
    """
    Selection Sort: Finds the minimum element and places it at the beginning.
    Time Complexity: O(n^2)
    """
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j

        if min_index != i:
            # Swap current element with the found minimum
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list


def insertion_sort(my_list):
    """
    Insertion Sort: Builds the sorted list one item at a time.
    Time Complexity: O(n^2), but faster on nearly sorted data.
    """
    for i in range(1, len(my_list)):
        j = i - 1
        temp = my_list[i]

        # Shift elements to the right to make room for insertion
        while j >= 0 and temp < my_list[j]:
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = temp  # Insert in correct position
    return my_list


def merge(list1, list2):
    """
    Merges two sorted lists into one sorted list.
    Time Complexity: O(n + m)
    """
    combined = []
    i = 0
    j = 0

    # Compare elements from both lists
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    # Add remaining elements from list1
    while i < len(list1):
        combined.append(list1[i])
        i += 1

    # Add remaining elements from list2
    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined


def merge_sort(my_list):
    """
    Merge Sort: Divides the list into halves, sorts each, and merges.
    Time Complexity: O(n log n)
    """
    if len(my_list) == 1:
        return my_list

    mid_index = len(my_list) // 2
    left = merge_sort(my_list[:mid_index])   # Recursively sort left half
    right = merge_sort(my_list[mid_index:])  # Recursively sort right half

    return merge(left, right)  # Merge sorted halves


def swap(my_list, index1, index2):
    """
    Swaps two elements in a list.
    """
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_index, end_index):
    """
    Places the pivot element in its correct position in the array.
    All smaller elements are moved before it, and larger ones after.
    Returns the final position of the pivot.
    """
    swap_index = pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    
    # Finally place pivot in its correct position
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(my_list, left, right):
    """
    Recursively sorts the list using the Quick Sort algorithm.
    """
    if left < right:
        pivot_index = pivot(my_list, left, right)  # Partition around pivot
        quick_sort_helper(my_list, left, pivot_index - 1)   # Left subarray
        quick_sort_helper(my_list, pivot_index + 1, right)  # Right subarray
    return my_list


def quick_sort(my_list):
    """
    Quick Sort: Uses divide-and-conquer to sort the list in-place.
    Time Complexity: Average O(n log n), Worst O(n^2)
    """
    quick_sort_helper(my_list, 0, len(my_list) - 1)