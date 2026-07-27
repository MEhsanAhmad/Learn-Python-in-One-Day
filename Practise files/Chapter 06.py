#Chapter 6: Making Choices and Decisions

# Not equals: 5 != 2
# Greater than: 5>2
# Smaller than: 2<5
# Equal than  : 2==2
# Greater than or equals to: 5>=2 5>=5
# Smaller than or equals to: 2 <= 5 2 <= 2

userEnter = int(input("Enter you any number: "))
if userEnter > 2 : print("Hello World")
elif userEnter < 2 : print("How Are You")
else : print("Ok Good By.")

#inline if

myInt = int(input("Enter you any number: "))
num1 = 12 if myInt==10 else 13
print(num1)
print("---------------------------------------------")


myPets = input("Enter your any Pet name: ")
pets = ['cats', 'dogs', 'rabbits', 'hamsters']
for myPets in pets:
    print(myPets)

#get index number

myPets = input("Enter your any Pet name: ")
pets = ['cats', 'dogs', 'rabbits', 'hamsters']
for index, myPets in enumerate(pets):
    print(index, myPets)


message = "Hello World"
for i in message:
    print(i)

for i in range(4,): print(i)

#while Loop

counter = -5

while counter < 0:
    print("counter = ", counter) 
    counter = counter + 1

#Break

j = 0
for i in range(150000):
    j = j + 1
    print("i =", i, "j =", j)
    if j == 11:
        break

#Continue

j = 0

for i in range(5):
    j = j + 1
    
    print(f"i = {i}, j = {j}")
    if j == 1:
        continue  # This jumps back to the start of the loop
    print("I will be skipped over if j = 6")
        
# Try, except

try: 
    userInput = int(input("Enter Any Number: "))
    answer = userInput/2
    
    print(int(answer))
except:
    print("Error")


try:
    # 1. Get Input
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    # 2. Perform Calculation
    result = num1 / num2

except ValueError:
    print("Error: Please enter whole numbers only.")

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

else:
    # This ONLY runs if the 'try' block had NO errors
    print(f"The calculation was successful! Answer: {result}")
    try:
        with open("missing.txt", "r") as myFile:
            print(myFile.read())
    except FileNotFoundError:
        print("Note: The math worked, but 'missing.txt' does not exist.")

finally:
    # This runs NO MATTER WHAT (error or no error)
    print("Program execution finished.")

print("---------------------------------------------")
