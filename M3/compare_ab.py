"""comparision of two variables"""
def compare_ref(parameter):
#Definding the function for the type
    return type(parameter)
# VARA = int(input ("Enter the first variable value"))
# VARB = int(input("Enter the second variable value"))

VARA = "hello"
VARB = 12

STRING_TYPE = "string"
if compare_ref(VARA) == compare_ref(STRING_TYPE)  or compare_ref(VARB) == compare_ref(STRING_TYPE):
    print("String Involved")
elif VARA > VARB:
    print("Bigger")
elif VARA == VARB:
    print("Equal")
else:
    print("Smaller")
