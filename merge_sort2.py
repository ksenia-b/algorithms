def merge_sort(list1):
    if len(list1) > 1:
        middle_el = len(list1)//2

        left_list = list1[:middle_el]
        right_list = list1[middle_el:]

        merge_sort(left_list)
        merge_sort(right_list)

        print("left_list = ", left_list)
        print("right_list = ", right_list)

        left_index = 0
        right_index = 0
        main_index = 0

        while left_index < len(left_list) and right_index < len(right_list):
            if left_list[left_index] < right_list[right_index]:
                list1[main_index] = left_list[left_index]
                left_index += 1
                main_index += 1
            else:
                list1[main_index] = right_list[right_index]
                right_index += 1
                main_index += 1

        while left_index < len(left_list):
            list1[main_index] = left_list[left_index]
            left_index += 1
            main_index += 1

        while right_index < len(right_list):
            list1[main_index] = right_list[right_index]
            right_index += 1
            main_index += 1

        print("list1 = ", list1)
        # merge_list(left_list, right_list)




if __name__ == '__main__':
    merge_sort([21, 2, 45, 30, 10])
