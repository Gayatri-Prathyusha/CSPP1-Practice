"""#Exercise : Function and Objects Exercise-3
#Implement a function that converts the given
testList = [1, -4, 8, -9] into [1, 16, 64, 81]"""

def square(a_num):
    """squaring function"""
    return a_num**2
def apply_to_each(l_list, f_un):
    """the function to print the list"""
    for i, _ in enumerate(l_list):
        l_list[i] = f_un(l_list[i],)
    return l_list
def main():
    """function main"""
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, square))

if __name__ == "__main__":
    main()
