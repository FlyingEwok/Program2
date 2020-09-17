'''You will design a program to exchange the values of two numbers without using a temporary variable. You will ask a user to input two numbers and print the numbers in the reverse order. (Hint, you may have only two variables)''' 

num1 = int(input("Enter a number: " ))
num2 = int(input("Enter a number: " ))

#Print variable values out before exchange
print("Before Exchange: num1 = ", num1, " num2 = ", num2) 

#Swap num1 & num2

#Swap numbers by getting sum of the 2 numbers and swapping by using subtraction from the sum
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

#Print variable values out after exchange
print("After Exchange: num1 = ", num1, " num2 = ", num2)

#hello