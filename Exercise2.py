num1 = int(input("give me a number: "))
if num1 % 2 == 0 or num1 % 4 != 0:
    print("Even Number")
else:
    print("Odd Number")

num = int(input("Give 1st number:"))
check = int(input("Give 2nd number:"))
if num % check == 0:
    print("{} completely divides {}".format(check, num))
else:
    print("{} doesn't divides {} completely".format(check, num))
