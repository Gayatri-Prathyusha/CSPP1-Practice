"""#Exercise : Biggest Exercise
#Write a procedure, called biggest, which returns the key
corresponding to the entry with the largest number of values
associated with it. If there is more than one such entry, return
any one of the matching keys."""
def biggest(a_dict):
    '''
    a_dict: A dictionary, where all the values are lists.
    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    return max(a_dict)
def main():
    """function main"""
    n_str = input()
    a_dict = {}
    for _ in range(int(n_str)):
        s_tr = input()
        l_ist = s_tr.split()
        if l_ist[0][0] not in a_dict:
            a_dict[l_ist[0][0]] = [l_ist[1]]
        else:
            a_dict[l_ist[0][0]].append(l_ist[1])
    print(biggest(a_dict))

if __name__ == "__main__":
    main()
   