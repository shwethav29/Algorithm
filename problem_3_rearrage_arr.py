import math
def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sort_array_desc(input_list,0,len(input_list))

    number1 = 0
    number2 = 0
    for i , ele in enumerate(input_list):
        if(i & 1):
            number2 = ele + number2*10
        else:
            number1 = ele + number1*10
    return number1,number2


def sort_array_desc(input_list,start_index,end_index):
    if((end_index-start_index) <= 1):
        return
    mid = start_index + ((end_index-start_index) // 2)
    sort_array_desc(input_list,start_index,mid)
    sort_array_desc(input_list,mid,end_index)
    merge(input_list,start_index,mid,mid,end_index)

def merge(input_list,left_start,left_end,right_start,right_end):
    left = left_start
    right = right_start
    output_arr = []
    while(left<left_end and right<right_end):
        if(input_list[left]<input_list[right]):
            output_arr.append(input_list[right])
            right +=1
        else:
            output_arr.append(input_list[left])
            left +=1
    while(left<left_end):
        output_arr.append(input_list[left])
        left += 1
    while(right < right_end):
        output_arr.append((input_list[right]))
        right += 1
    for i, ele in enumerate(output_arr):
        input_list[left_start+i] = ele


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function( [[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[],[0,0]])
test_function([[2],[2,0]])
test_function([[1,2],[2,1]])
test_function([[1,3,2],[31,2]])
