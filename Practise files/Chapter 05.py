#Chapter 5: Making Your Program Interactive

#input

userName = input("Enter your name: ")
userCity = input("Enter Your City: ")

print(f"My name is {userName}. My city Name is {userCity}.")

print("---------------------------------------------")

#print()
#first Way:

print("Hello World, I am ", userName,"Live in ", userCity, ".")

#2nd Way
print("Hello World, my name is %s and i am Live in %s." %(userName, userCity))

#3rd WAy

print("Hello World, my name is {} and i am Live in {}." .format(userName, userCity))

#4th Way

print("Hello World, I am " + userName +" Live in " + userCity + ".")

#5th Way 

print(f"My name is {userName}. My city Name is {userCity}.")

print("---------------------------------------------")
#triple Quotes 

print(f'''Hello World!,
      My name is {userName}.
      My city Name is {userCity}.
      {userName} is like to learn programming.''')
print("---------------------------------------------")


#Escape Characters

print("Hello \n World") #\n  New Line
print("Hello \t World") #\t  Tab
print("\\") # \ Allow to function like n t , ' "" in string
print(r"Hello\tWorld") # r stop \ to function in string

print("---------------------------------------------")
