import math

# 1. Get the input from the user
# number_to_check = int(input("Enter Your Number: "))

# 2. Define the logic (The "Tool")
def check_if_prime_fast(n):
    if n < 2: 
        return False
    
    limit = int(math.sqrt(n)) + 1
    
    for x in range(2, limit):
        if n % x == 0:
            return False
    return True

# # 3. USE the function (The "Action")
# if check_if_prime_fast(number_to_check):
#     print(f"{number_to_check} is a prime number! ✨")
# else:
#     print(f"{number_to_check} is not prime.")