print ("================|For Loops|================")
print ("\n") # new line
print ("--------------|Example 1|--------------")

for i in range(5):
    print("Hello World!") # add a message here

print("\n") # new line

print ("--------------|Example 2|--------------")

number = 5               # start with 5
for i in range(3):       # do this 3 times
    number = number + 2  # add 2 to the number
print(number)

print("\n") # new line

print ("--------------|Example 3|--------------")

print("You say goodbye")
print("and I say hello")
for i in range(3):      # do this 3 times
    print("Hello")      # this is in the loop
    print("Goodbye")    # this is also in the loop
print("Goodby forever") # this is outside the loop

print("\n") # new line

print ("--------------|Example 4|--------------")

for number in range(5):
    print(number)

print("\n") # new line

print ("--------------|Example 5|--------------")

number = 0                  # start with 0   
for letter in "string":     # for each letter in the word "string"
    number = number + 1     # add 1 to the number
    print(letter, number)   # print the letter and the number

print("\n") # new line