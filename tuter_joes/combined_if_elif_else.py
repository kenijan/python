

# Combined example of if, elif, and else

# Fine calculation based on the number of days

days = int(input("Enter the number of days: "))

# If the days are 0 or less, no fine
if days <= 0:
    print("Good! No Fine")

# If days are between 1 and 5, fine is 0.5 per day
elif days <= 5:
    fine = days * 0.5
    print(f"Fine Amount: {fine}")

# If days are between 6 and 10, fine is 1 per day
elif days <= 10:
    fine = days * 1
    print(f"Fine Amount: {fine}")

# If days are more than 10 but less than or equal to 30, fine is 5 per day
elif days > 10 and days <= 30:
    fine = days * 5
    print(f"Fine Amount: {fine}")

# If days are greater than 30, membership is canceled
else:
    print("Membership Cancelled")
'''

Explanation:
    Input: You enter the number of days using input().
    Conditions:
        If the number of days is 0 or less, there is no fine.
        If the days are between 1 and 5, a fine of 0.5 per day is applied.
        If the days are between 6 and 10, a fine of 1 per day is applied.
        If the days are between 11 and 30, a fine of 5 per day is applied.
        If the days are more than 30, the membership is canceled.

'''