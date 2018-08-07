"""# Exercise: Is In
# Write a Python function, is_in(c_har, a_str), that takes in two arguments a
c_haracter and String and returns the is_in(c_har, a_str) which retuns a boolean value.

# This function takes in two arguments c_haracter and String and returns
one boolean value."""

def is_in(c_har, a_str):
    '''
    c_har: a single c_haracter
    a_str: an alphabetized string
    returns: True if c_har is in a_str; False otherwise
    '''
    a_num = None
    c_har = c_har.lower()
    c_str = a_str.lower()
    b_str = ''.join(sorted(c_str))
    if len(b_str) == 0:
        return "String length cannot be 0."
    elif len(b_str) == 1:
        if c_har in b_str:
            return True
        return False
    else:
        a_num = int(len(b_str)/2)
        if c_har == b_str[a_num]:
            return True
        else:
            if c_har < b_str[a_num]:
                return is_in(c_har, b_str[:a_num])
            return is_in(c_har, b_str[a_num:])
def main():
    """function main """
    data = input()
    data = data.split()
    print(is_in((data[0][0]), data[1]))

if __name__ == "__main__":
    main()
