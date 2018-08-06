"""Exercise: fourth power
Write a Python function, fourth_power, that takes in one number and 
returns that value raised to the fourth power.
You should use the square procedure that you defined in an earlier 
exercise exercise (you don't need to redefine square in this box;
This function takes in one number and returns one number."""

def square(x_val):
    """
    x_val: int or float.
    """
    # Your code here
    return x_val**2
def fourth_power(x_val):
    """
    x_val: int or float.
    """
    # Your code here
    return square(square(x_val))
def main():
    """actual code"""
    data_in = input()
    data_in = float(data_in)
    temp = str(data_in).split('.')
    if(temp[1] == '0'):
        print(fourth_power(int(float(str(data_in)))))
    else:
        print(fourth_power(data_in))

if __name__ == "__main__":
    main()
