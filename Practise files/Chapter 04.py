#Chapter 4: Data Types in Python

# %s = String
# %d = integers
# %f = floats

brand = "Apple"
exchangeRate = 1.23523524591

#if i used % so i change f to s but not in format.
message = "The price of this %s laptop is %-5d USD and the exchange rate is %s USD to 1 EUR." %(brand, 1299, exchangeRate)
print(message)

message1= "this is my %s and i get form %s in the %d rupees." %("Book", "Books Store", 500)
print(message1)
print("---------------------------------------------")

#Formatting Strings using the format() method

message = "The price of this {} laptop is {} USD and the exchange rate is {} USD to 1 EUR." .format(brand, 1299, exchangeRate)
print(message)
message = "The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:.2f} USD to 1 EUR." .format(brand, 1299, exchangeRate)
print(message)

message1 = "{0} is easier than {1}".format("Python","Java")
message2 = "{1} is easier than {0}".format("Python", "Java")
message3 = "{:10.2f} and {:d}".format(1.234234234, 12)
message4 = "{}".format(1.234234234)
print(message1)
print(message2)
print(message3)
print(message4)
print("---------------------------------------------")

#Type Casting In Python
#int()
#float()
#str()

Number2 = 502.115896
str1    = "StringName"
print(Number2)
Number1 = int(Number2)
print(Number1)
print(type(Number1))
Number3 = float(Number2)
print(Number2)
print(type(Number2))
Number4 = str(Number3)
print(Number4)
print(type(Number4))

print("---------------------------------------------")

#List

userAge3 = [21, "Ehsan", 23, 24, 25]
userAge = [21, 22, 23, 24, 25]

print(userAge3[0])
print(userAge3[1])
print(userAge3[4])
# Reverse
print(userAge3[-3])
print(userAge3[-5])

userAge2 = userAge[2:5]
print(userAge2)
print(userAge)
userAge4 = userAge[0:5:3]
print(userAge4)

userAge4 = userAge[0:5:2]
print(userAge4)
userAge4 = userAge[0:5:4]
print(userAge4)

numberList = [1, 2, 3, 4, 125, 6, 7, 8, 9, 10] # if step is 2 mean (0+2, 2+2, 4+2 index)
print(numberList[:9])
print(numberList[3:])

numberList1 = numberList[0:11:3]
print(numberList1)

numberList2 = numberList[::3]
print(numberList2)
print("---------------------------------------------")

#List Modify by append

numberList.append(12) # add in list
print(numberList)
del numberList[1] #by index delete used del
print(numberList)

#Tuple 
monthsOfYear = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
print(monthsOfYear)

print(monthsOfYear[2])
# monthsOfYear[0] = "Jan" Tuple is not modify OK
print("---------------------------------------------")

#Dictionary

userNameAndAge = {"Ehsan": 22, "Usama": 21, "Zeeshan":45, "Arslan":26}
print(userNameAndAge)
print(userNameAndAge["Ehsan"])
userNameAge = dict(Ehsan = 21, Aktar = 23, Naeem = 29) #other way to write Dictionary
print(userNameAge["Naeem"])

userNameAge["Usama"] = 29
print(userNameAge)

del userNameAge["Usama"]
print(userNameAge)


countryNameList = {"Chaina" : 154, 91 : "Japan", 96 : "indea", 90 : "Turkey", 128 : "Iran"}
print(countryNameList)

print(countryNameList["Chaina"])
print(countryNameList[91])
print("---------------------------------------------")
