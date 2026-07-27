#Exercise 1: The Personalized Receipt

productName = input("Enter your product Name :")
productPrice = input("Enter Your product price :")

mylist = dict()

mylist[productName] = productPrice

print(mylist)
print(f"You purchased 3 units of {productName} for a total of ${productPrice}.")


