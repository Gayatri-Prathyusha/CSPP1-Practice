"""#Exercise : Function and Objects Exercise-2
#Implement a function that converts the given testList = [1, -4, 8, -9] into
[2, -3, 9, -8]"""


def inc(a):
    return a+1

def apply_to_each(l_list, f_un):
    """the function to print the list"""
    for i, _ in enumerate(l_list):
        l_list[i] = f_un(l_list[i],)
    return l_list

def main():
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, inc))

if __name__ == "__main__":
    main()
