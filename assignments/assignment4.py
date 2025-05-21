# Hands on Python Data Structure

# Task 1 - Working with Lists

fav_fruits = ["apple", "orange", "kiwi", "blueberry", "mango"]
print(f"Original list: {fav_fruits}")
fav_fruits.append("passionfruit")
print(f"After adding a fruit: {fav_fruits}")
fav_fruits.remove("apple")
print(f"After removing a fruit: {fav_fruits}")
print(f"Reversed list: {fav_fruits[::-1]}")

# Task 2 - Exploring Dictionaries
my_dict = {
    "name": "Erick",
    "age": "22",
    "city": "Ontario"
}

my_dict["favorite color"] = "green"

my_dict["city"] = "Melbourne"

print("Keys:")
for key in my_dict.keys():
    print(key)

print("Values:")
for val in my_dict.values():
    print(val)

# Task 3 - Using Tuples
tup = ("Jurassic Park", "Idol", "A Farewell to Arms")
print(f"Favorite things: {tup}")
#tup[0] = "Not Jurassic Park"
print("Oops! Tuples cannto be changed.")
print(f"Len of tuple: {len(tup)}")
