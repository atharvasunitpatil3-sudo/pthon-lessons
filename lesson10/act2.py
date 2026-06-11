# Check Palindrome
# nitin , racecar , madam , 121 , 1221

word = input("Enter word : ").strip().lower()#test
word_rev = ''
for i in word :
  word_rev = i +word_rev

if word == word_rev:
 print("It is a Palindrome")
else:
 print("It is not a Palindrome..")