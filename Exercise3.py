a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#  prints out all the elements of the list that are less than 5.

for i in a:
    if i < 5:
        print(i)

# make a new list that has all the elements less than 5 from this list in it and print out this new list
new_list = []
for i in a:
    if i < 5:
        new_list.append(i)
print(new_list)

# Ask the user for a number and return a list that contains only elements from the original list a that are smaller
# than that number given by the user.

custom_list = []
user_input = int(input("Enter Number: "))
for i in a:
    if i < user_input:
        custom_list.append(i)
print(custom_list)

# Advance
print([e for e in a if e < 5])