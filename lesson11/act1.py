# Sum of n natural numbers 
upper_limit = int(input("Enter upto which number you want sum : "))
start = 1
sum_numbers = 0

while start <= upper_limit :
    sum_numbers += start
    start +=1

print(f"The sum of natural numbers starting from 1 upto {upper_limit} is :{sum_numbers}")