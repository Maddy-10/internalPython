vowels = "aeiouAEIOU"
count = 0
str = input("Enter a string: ")
for char in str:
    if char in vowels:
        count += 1
print("Number of vowels in the string:", count)


# Output:
# Enter a string: Hello World
# Number of vowels in the string: 3