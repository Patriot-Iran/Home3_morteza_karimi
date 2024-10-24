import math #the math library

def fraction_result(numerator,denominator):
    """
    this function receives two variables it it returns the quotient of the fraction

    numerator = a float
    denominator= a float

    it return the fraction result
    """
    try: #if we dont have logical error
        return numerator/denominator
    except:#if wet have logical error
        return math.inf # it returns the inf when the denominator is zero

    


#it receives numerator
numerator=float (input("Enter the numerator of the fraction:\n"))
#it receives denominator
denominator=float (input("Enter the of denominator the fraction:\n"))

#it prints the returned value from function
print ("the result is :\n",fraction_result(numerator,denominator)) 