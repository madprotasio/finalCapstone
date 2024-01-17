import math 

# User is prompt to input their loan option
print("Investment - to calculate the amount of interest you'll earn on you investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")

# User input will automatically be converted to lower case
user_input = input("Please enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if user_input == 'investment':
    # Set up for investment option
    # I am establishing all the varables needed for the calculations
    pay = float(input("Please enter the amount you wish to deposit: "))
    int_rate = float(input("Please enter the interest rate: ")) / 100
    years = int(input("Please enter the amount of years you plan on investing: "))

    # The option for simple or compound interest, user must choose which one to take
    # User input will automatically be converted to lower case
    user_choice = input("Do you want a 'simple' or 'compound' interest? ").lower()

    # If user chooses simple, calculates the amount accordingly
    if user_choice == 'simple' :
        total_simp = pay *(1 + int_rate * years)
        print("The total you need to repay is: ", total_simp)

    # Else calculates compound accordingly
    elif user_choice == 'compound':
        total_comp = pay * math.pow(1 + int_rate, years)
        print("The total you need to repay is: ", total_comp)

    # Display appropriate ERROR message when input is not recognised
    else:
        print("Invalid choice. Please enter 'simple' or 'compound'.")

elif user_input == 'bond':
    # Set up for bond option
    # Established the variables needed for calculation
    pay_house = float(input("Please enter the present value of the house: "))
    Int_Rate = float(input("Please enter the interest rate: ")) / 100
    months = int(input("Please enter the amount of months you plan to take to repay the bond: "))

    # Calculates the total amount to repay accordingly
    total_bond = (Int_Rate * pay_house ) / (1 - (1 + Int_Rate) ** (-months))
    print("The total amount you need to repay is: ", total_bond)

else:
    # If input not recognised, display ERROR message 
    print("Invalid choice. Please enter 'investment' or 'bond'.")