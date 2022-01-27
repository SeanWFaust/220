"""
Sean Faust
Lab1
This is a code to calculate the monthly interest based on user input.
I cannot find the Certificate of Authenticity so in lieu of that, I certify and state that this code is my own
authentic work.
"""
def monthly_interest():
    annual_interest = eval(input("Please enter your annual interest rate: "))
    total_cycle_days = eval(input("Please enter the amount of days in the billing cycle: "))
    previous_balance = eval(input("Please enter the previous balance: "))
    payment = eval(input("Please enter your payment amount: "))
    pay_day = eval(input("Please enter the day you made your payment: "))
    avg_day_bal = ((previous_balance * total_cycle_days) - (payment * (total_cycle_days - pay_day))) / total_cycle_days
    month_interest = (avg_day_bal * (annual_interest / 12)) / 100
    print("Your monthly interest charge is: $", round(month_interest, 2))