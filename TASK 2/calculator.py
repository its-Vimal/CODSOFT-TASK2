num1=float(input("Enter 1st No. = "))
num2=float(input("Enter 2nd No. = "))
print("For ADDITION enter -----------> A\n"
"For SUBCTRACTION enter -------> S\n"
"For MULTIPLICATION enter------> M\n"
"For DIVISION enter -----------> D\n"
"For All operations enter -----> X\n")
operator=input("Choose & Enter the Operator = ")
if operator=='A':
    print("ADDITION of inputted no.'s are : ",num1+num2)
elif operator=='S':
    print("SUBCTRACTION of inputted no.'s are : ",num1-num2)
elif operator=='M':
    print("MULTIPLICATION of inputted no.'s are : ",num1*num2)
elif operator=='D':
    print("DIVISION of inputted no.'s are : ",num1/num2)
elif operator=='X':
    print("ADDITION of inputted no.'s are : ",num1+num2)
    print("SUBCTRACTION of inputted no.'s are : ",num1-num2)
    print("MULTIPLICATION of inputted no.'s are : ",num1*num2)
    print("DIVISION of inputted no.'s are : ",num1/num2)
else:
    print("ERROR:You entered the wrong operator.")
