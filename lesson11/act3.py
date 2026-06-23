# Armstrong Number
num = input("Enter the number to check :")
sum = 0
power = len(num_str)
num = int(num_str)
temp = num
#153
while temp > 0:
    digit = temp % 10 #3
    sum = sum + digit**power
    temp = temp//10

print("Sum : ",sum)

if(sum == num):
    print("This is Armstrong number")
else:
    print("Not an Armstrong number")