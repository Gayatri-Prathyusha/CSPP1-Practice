"""#Exercise : how many
# write a procedure, called how_many, which returns the sum of the number of
values associated with a dictionary."""

def how_many(a_dict):
    '''
    a_dict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    c_num = 0
    for word in a_dict.keys():
        for _ in a_dict[word]:
            c_num = c_num+1
    return c_num
def main():
    """function main"""
    n_num = input()
    a_dict = {}
    for _ in range(int(n_num)):
        s_tr = input()
        l_ist = s_tr.split()
        if l_ist[0][0] not in a_dict:
            a_dict[l_ist[0][0]] = [l_ist[1]]
        else:
            a_dict[l_ist[0][0]].append(l_ist[1])
    print(how_many(a_dict))


if __name__ == "__main__":
    main()
    