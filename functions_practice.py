# A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.
def hello():
  print("Hello, user!")

# A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.
def pack(a,b,c):
  return [a,b,c]

# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". The function should not return anything.
def eat_lunch(my_list):

    j = 0
    for i in my_list:
        if (j == 0):
            print("First I eat", i)
        else:
            print("Next I eat", i)
        j+=1

# Test that your file works by running it in your terminal. Remember, you need to call your functions in order for them to run. Make sure that all three functions run (please print the output of pack()) before submitting the file.
hello()
print(pack("a","b","c"))
eat_lunch(["chicken", "pizza", "burgers", "hotdogs"])
