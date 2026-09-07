text=input("enter a string: ")
reverse=""

for i in text:
  reverse= i + reverse
  

if text==reverse:
  print("palindrome sting")
else:
  print("Not palindrome string")
