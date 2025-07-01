def swap(num1, num2):                  #This if the funtion to perform swap the numbers
    num3 = num1                        #Here we are assissing the num1 value to num3 variable
    num1 = num2                        #Here we are assissing the num2 value to num1 variable
    num2 = num3                        #Here we are assissing the num3 value to num2 variable
    return num1, num2                  #Here we are sending the final swapping value

num1 = int(input("Enter your First number:"))    #Here taking the first input value from the user
num2 = int(input("Enter your second number:"))   #Here taking the second input value from the user
print("Before swapping first number and second number value is:",(num1, num2))    #Here prints the values before swapping
print("After swapping first number and second number value is:", swap(num1,num2)) #Here prints the values after swapping