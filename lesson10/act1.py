 # Sum of N natural numbers

limit = int(input("Enter limit : "))
total = 0

for i in range(1, limit+1):
    total += i
print(f"The total up to limit is : {total}")


