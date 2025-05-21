# Exploring String Methods

# Task 1 - String slicing and Indexing
my_string = "Python is amazing!"
first = my_string[:6]
last = my_string[10:-1]
reverse = my_string[::-1]

print(f"First word: {first}")
print(f"Amazing part: {last}")
print(f"Reversed string: {reverse}")

# Task 2 - String Methods
new_string = " hello, python world! "
print(new_string := new_string.strip())
print(new_string := new_string.capitalize())
print(new_string := new_string.replace("world", "universe"))
print(new_string := new_string.upper())

# Task 3 - Check for palindromes
word = input("Enter a word: ")
if word == word[::-1]:
    print(f"Yes, '{word}' is a palindrome!")
else:
    print(f"No, '{word}' is not a palindrome!")
