def sort_list(list):
    n = len(list)
    i = 0

    while i < n :
        j = 0
        while j < (n - i - 1) :
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
            j += 1
        i += 1
    return list


unsorted_list = [ 3, 5, 1, 6, 2, 7, 4]
sorted_list = sort_list(unsorted_list)
print(sorted_list)

list1 = [4,5,6,2,49]
sorted_list = sort_list(list1)
print(sorted_list)


