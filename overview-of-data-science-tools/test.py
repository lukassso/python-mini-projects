# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#    print("{0} is Even".format(num))
# else:
#    print("{0} is Odd".format(num))

print("Before input")
x = int(input("Write some number: "))
print(f"x is: {x}")
print(f"number {x} is" + " not"*(not x % 2 == 0) + " even")