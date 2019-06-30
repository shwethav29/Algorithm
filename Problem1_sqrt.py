def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root

    """
    base =0
    upper = number
    while(upper > base):
        if(upper * upper <= number):
            return upper
        half = upper // 2
        if(half * half == number):
            return half
        elif(half*half <number):
            base = half
            upper -= 1
        else:
            upper = half
    return upper

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (11 == sqrt(143)) else "Fail")