#Chapter 3: The World of Variables and Operators

userAge =  25
print(userAge)
userAge, userName = 36, 'Usama' # Change user Age by Update Variable Value
print(f'userage is {userAge}. User Name is {userName}.')
print("---------------------------------------------")

# first Assignment Sign

x = 5
y = 10
a = x > y
print(a)
y = x

print('x = ', x)
print('y = ', y)
b = y > x 
c = x == y
print(b)
print(c)
print("---------------------------------------------")

#Change Between same variables
d = 10
D = 30
F = d == D
print(F)
print(d)
print(D)
print("---------------------------------------------")

#Basic Operators

q = 5
w = 3

print(q-w) # Subtraction
print(q+w) # Addition
print(q*w) # Multiplication
print(q/w) # Division
print(q//w)# rounds down the answer to the nearest whole Number
print(q%w) # Modulus
print(q**w)# (5 to the power of 3)
print("---------------------------------------------")

#More Assignment Operators

e = 13
print(e)
e += 13
print(e)
e -= 6
print(e)
e *= 2
print(e)
e **= 2
print(e)
e //= 5
print(e)
e /= 5
print(e)
e %= 3
print(e)
e = "This is End of My Chapter 03"
print(e)
print("---------------------------------------------")
