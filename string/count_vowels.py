text=input("Enter a string: ")
vowels=0
constant=0

for i in text:
 if i in "aeiou":
    vowels= vowels+1
 else:
    constant=constant+1

print("vowels",vowels)
print("constant",constant)
   
