def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    start = 0
    end = len(input_list)-1
    min_index = find_minimum(input_list)
    if(number < input_list[end]):
        return binary_search(input_list,number,min_index,end)
    else:
        return binary_search(input_list,number,0,min_index)
    return -1

def  binary_search(input_list,target,start_index,end_index):
    if(start_index>=end_index):
        return -1
    mid = start_index + (end_index-start_index)//2
    if(target == input_list[mid]):
        return mid
    if(target>input_list[mid]):
        start_index = mid+1
    if(target < input_list[mid]):
        end_index = mid
    return binary_search(input_list,target,start_index,end_index)

def find_minimum(input_list):
    begin = 0
    end = len(input_list)-1
    while(begin<end ):
        if(input_list[begin] < input_list[end]):
            return begin
        mid = begin + ((end -begin) // 2)
        print(" low {} mid {} high {}".format(begin,mid,end))
        if(input_list[begin]<input_list[mid]):
            begin = mid
        elif(input_list[end]>input_list[mid]):
            end = mid
        else:
            return end
    return end

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 9, 10, 11, 12], 10])
