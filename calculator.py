print("                              calculator")
addition = "+"
subtraction = "-"
multipliction = "*"
division = "/"
num_1 = float(input(""))
num_2 = float(input(""))
operator = input("kindly enter operator")
#c = "num_1"  + "num2"
if operator == addition:
    c = num_1+num_2
    print(c)

elif  operator == subtraction:
    c = num_1 - num_2
    print("c = num_1 - num_2")
elif operator == multipliction:
    c = num_1 * num_2
    print("num_1 * num_2")
elif operator == division:
    c = num_1 / num_2
    print("num_1 / num 2")
else:
     print("invalid_number")

    



