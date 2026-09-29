 # Write a program to calculate how many total digits are in a number entered by the user?
 
num = int(input("Enter a number: "))
temp = num
digits = 0

while temp > 0:

    digits += 1
    temp = temp // 10
    
print(digits)
    