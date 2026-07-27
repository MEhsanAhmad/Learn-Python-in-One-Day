# # Run this to create the file in your "Practise files" folder
# with open("myfile.txt", "w") as f:
#     f.write("This is the first line.\n")
#     f.write("This is the second line.\n")

# print("File created successfully!")


# with open("myfile.txt", "r") as f:
#     firstline = f.readline()
#     secondline = f.readline()
#     print(firstline, end="") # 'end=""' prevents the extra blank line
#     print(secondline, end="")
# f.close() #needed; it happens automatically here!

userWrite = input("Enter what you want to right: ")

def write ():
    with open("myfile.doc", "w") as f:
        f.write("\n"+ userWrite + "\n")
    return True

write()