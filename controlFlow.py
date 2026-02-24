num = 3
denom = 0
if denom != 0 and num / denom > 10:
    print("Here")
else:
    print("there")

#Why is this true? The first part of condition is true then the whole condition must be true.
#So the next part will be skipped.

status = int(input("Enter your status"))
msg = "No error"

#switch style in Python
match status:
    case 400:
        msg = "Bad request"
    case 420 | 430:
        msg = "Not bad"
    case _:#default
        msg = "Not sure yet"

#try/except block
try:
    number = int(input("Enter a number:"))
    result = 10 / number
    print(f"Result is {result}")
except ZeroDivisionError:
    print("You can not divide by zero.")
except ValueError:
    print("Please enter a valid integer.")
else:
    print("Good")#If no erorrs occurred in the block
finally:
    print("We can clean up resources here.")#No matter what happens, "finally" block will be run.

#We called errors expect syntax erorr as exception.
#assert: to say something is true
n = int(input("Enter a positive value: "))
assert n > 0
#If you enter a non-positive value, the program throws an AssertionError exception.

#while-else
count = 0
while count < 5:
    print(count, "is less than five")
    count += 1
else:
    print(count,"is not less than five")

#for statement
friends = ['Anthony', 'Michael', 'Tom']
for friend in friends:
    friend = 'forever'#This does not impact the original list.
print(friends)

#range
for i in range(10):
    print(i)
    i = 5
#The output will be 0 1 2 ... because i will be overwritten with the next index in range

#enumerate() function: assign numbers to iteration items
cars = ['kias', 'audi', 'bmw']
for i, car in enumerate(cars, start = 1):
    print(f"iteration {i}: {car}")