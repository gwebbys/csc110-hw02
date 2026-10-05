#Grace Webb

# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    """Get two number inputs from the user, and then return them back to the function, where it will end""" 
    # the return shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    x = int(input("give me x: "))    #this asks the user to give an integer
    y = int(input("give me y: "))
    return x,y

# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
    """Calculate (a*b)/(a+b) and return"""
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    numerator = (a*b)
    print("mult result:", numerator)    #this calculates the (a*b) or numerator of our operation
    
    denominator = (a+b)
    print("add result:", denominator)
    
    return numerator / denominator
    

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
    """This adds a * and = border, and then prints out the inputed numbers and the result from task 2"""
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    print("*" * 16)
    print("RESULTS:")
    print("first number:", a)
    print("second number:", b)
    print("multadd result:", ab_multadd)   
    print("=" *16)

def main ():
    """This calls task 1, task 2, and task 3"""
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y

    x, y = read_two_ints()

    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd

    xy_multadd = compute_multadd(x,y)   #this applies the numbers we got in the first task to become a and b in our operation
   

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;

    print_fancy(x, y, xy_multadd)  #this performs the function in task 3


    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
