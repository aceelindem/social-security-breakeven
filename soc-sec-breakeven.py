#!/usr/bin/python3

import sys

def calculate_break_even(monthly_earlier, monthly_later, interest_rate, months_earlier):
    # Convert interest rate to decimal form
    interest_rate_decimal = interest_rate / 100

    # Initialize principal
    principal_earlier = 0
    principal_later= 0
    month = 0

    print(f"\nComparison of collecting ${monthly_earlier:.2f} {months_earlier} months earlier\
 or ${monthly_later:.2f}  with an average interest rate of {interest_rate_decimal*100}%\n\n")
    
    print(f"Year     Earlier Principal      Later Principal")
    while principal_earlier >= principal_later:
        month += 1
        
        # Compute early principal
        principal_earlier += monthly_earlier
        principal_earlier += principal_earlier * (interest_rate_decimal / 12)

        # Compute principal at 70 years old (maximum ss retirement age) 
        if month >= months_earlier:
            principal_later += monthly_later
            principal_later += principal_later * (interest_rate_decimal / 12)
            
        if (month % 12) == 0:
            print(f"{month/12}      ${principal_earlier:.2f}              ${principal_later:.2f}")

    return month

def main(args):
# Get inputs from the user
    monthly_earlier = float(input(
        "Enter the earlier monthly social security amount [Press Enter for default: $3828]: ")or "3828")
    monthly_later = float(input(
        "Enter the monthly later social security amount [Press Enter for default: $4850]): ") or "4850")
    interest_rate = float(input(
        "Enter the annual interest rate (in percent) [Press Enter for default: 0.0]: ") or "0.0")
    months_earlier = int(input(
        "Enter the number of months earlier [Press Enter for default: 40]: ") or "40")

    # Calculate and print the result
    result = calculate_break_even(monthly_earlier, monthly_later, interest_rate, months_earlier)
    print(f"The break-even point is: {result:.2f} months or {result/12:2f} years")

if __name__ == "__main__":
    main(sys.argv[0])
    
