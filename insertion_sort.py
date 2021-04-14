def insertion_sort(arr):
    for index in range(1, len(arr)):
        current_el = arr[index]
        left_el_index = index - 1

        while left_el_index >= 0 and arr[left_el_index] > current_el:
            arr[left_el_index + 1] = arr[left_el_index]
            left_el_index = left_el_index - 1

        arr[left_el_index + 1] = current_el


insertion_sort([6, 2, 30, 21])