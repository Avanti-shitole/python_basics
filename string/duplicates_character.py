text = input("Enter a string: ")
duplicates = ""

for i in text:
    if text.count(i) > 1 and i not in duplicates:
        duplicates = duplicates + i

print("Duplicate characters:", duplicates)