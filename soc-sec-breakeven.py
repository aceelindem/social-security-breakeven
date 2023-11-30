#!/usr/bin/python3

import sys

def calculate_break_even(monthly_before_70, monthly_70, interest_rate, months_before_70):
    # Convert interest rate to decimal form
    interest_rate_decimal = interest_rate / 100

    # Initialize principal
    principal_before_70 = 0
    principal_70 = 0
    month = 0

    print(f"Year      Before 70 Principle    At 70 Principal")
    while principal_before_70 >= principal_70:
        month += 1
        
        # Compute before_70 principle
        principal_before_70 += monthly_before_70
        principal_before_70 += principal_before_70 * (interest_rate_decimal / 12)

        # Compute principle at 70 years old (maximum ss retirement age) 
        if month >= months_before_70:
            principal_70 += monthly_70
            principal_70 += principal_70 * (interest_rate_decimal / 12)
            
        if (month % 12) == 0:
            print(f"{month/12}      ${principal_before_70:.2f}              ${principal_70:.2f}")

    return month

def main(args):
# Get inputs from the user
    monthly_before_70 = float(input("Enter the monthly social security amount before 70: "))
    monthly_70 = float(input("Enter the monthly social security amount at 70 [Press Enter for default: $4850]): ") or "4850")
    interest_rate = float(input("Enter the annual interest rate (in percent): "))
    months_before_70 = int(input("Enter the number of months before 70: "))

    # Calculate and print the result
    result = calculate_break_even(monthly_before_70, monthly_70, interest_rate, months_before_70)
    print(f"The break-even point is: {result:.2f} months or {result/12:2f} years")

if __name__ == "__main__":
    main(sys.argv[0])
    
