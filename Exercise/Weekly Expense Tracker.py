# #Weekly Expense Tracker

# total = 0  # Changed from 'today' to 'total' to match the loop

# for day in range(1, 8):
#     expense = float(input(f"Day {day} - Enter your expense: $"))
#     total += expense # This now works because 'total' exists

# average = total / 7

# # Using 'total' and 'average' correctly here
# print(f"\nYour total weekly expense is: ${total:.2f}")
# print(f"Your average daily expense is: ${average:.2f}")

#Bank credit and debit
# total = 0

# for day in range(1, 8):
#     credit = float(input(f"How much you credit add in Day {day} your account: $"))
#     total += credit
#     debit = float(input(f"How much you use in Day {day} your account: $"))
#     total -= debit

# print(f"How much you have in your account: ${credit:.2f}")
# print(f"How much you used to your account: ${credit:.2f}")
# print(f"How much you have remaining in your account: ${total:.2f}")

total_balance = 0
all_credits = 0
all_debits = 0

for day in range(1, 8):
    print(f"--- Day {day} ---")
    credit = float(input("Amount to add (Credit): $"))
    debit = float(input("Amount spent (Debit): $"))
    
    # Update our 3 "buckets"
    all_credits += credit
    all_debits += debit
    total_balance += (credit - debit)

print("-" * 20)
print(f"Total amount added: ${all_credits:.2f}")
print(f"Total amount spent: ${all_debits:.2f}")
print(f"Remaining balance:  ${total_balance:.2f}")