# q1.py

#
# Full Name:Yishao Chen
#  SFU ID #:301652300
# SFU Email:yca541@sfu.ca
#

# ... put your answer to question 1 here ...
name = input("What's your name? ")
quarters = int(input("How many quarters do you have? "))
total_cents = quarters * 25
candies = total_cents // 12
remaining_cents = total_cents % 12
print(f"{name}, you can buy {candies} candies with {remaining_cents} cents left over.")
