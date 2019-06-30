def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    smaller =0
    large = len(input_list)-1
    equal = 0
    while(equal <= large):
        if(input_list[equal] < 1):
            swap(input_list,smaller,equal)
            smaller +=1
            equal+=1
        elif(input_list[equal]==1):
            equal+=1
        else:
            swap(input_list,equal,large)
            large -=1
        #print(input_list)
        #print("s {} e {} l {}".format(smaller,equal,large))

    return input_list

def swap(input_list,left_index,right_index):
    temp = input_list[left_index]
    input_list[left_index]=input_list[right_index]
    input_list[right_index] = temp

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])