#Exercise 2: The Data Typer

import ast
userData = input("Enter your Data in one line: ")
try:
    userData = ast.literal_eval(userData)
except (ValueError, SyntaxError):
    userData = userData

print(type(userData))