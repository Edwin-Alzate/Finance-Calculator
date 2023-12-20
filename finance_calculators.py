import math
''' This program allows the user to access two financial calculators, an investment calculator and a home loan repayment calculator.

1. Display to the user the options for the calculators he can access.
2. Request input from the user selecting one of the options.
3. Accept the input strings as capitalised, uppercase or lowercase.
4. If an invalid option is entered go back to last step.
5. If Investment is selected ask the user for the amount being deposited, interest rate, years planing on investing and what type of interest they want.
6. If an invalid option is entered go back to last step.
7. Calculate the result for the investment and display it to the user.
8. If Bond is selected ask the user for the present value of the house, interest rate and numbers of month they plan to repay the bond.
9. Calculate the result for the repayments and display it to the user. 
10. If end is selected finalise the calculator '''

print("\n\t\tWelcome to the Finance Calculator.")                        # Adding new line \n and tabs \t to the tittle
print("-" * 75)                                                          # Decoration for the tittle
print("\nInvestment - Calculate the amount of interest you'll earn on your investment.")    # Displaying the menu to the user
print("Bond       - Calculate the amount you'll have to pay on a home loan.")
print("End        - Close the calculator.")

# Creating the variable calculator as True to enter a loop
calculator = True                                                          

# Creat the loop for the calculator to run as many times as the user wants
while calculator == True:                                                  

    # Store the input in the variable named selection and convert it to lowercase to be case insensitive for the comparison
    selection = input("\nEnther either 'investment' or 'bond' to proceed to the calculator, or 'end' to finalise: ").lower()  

    # Start the conditional statement to check if the selected option was 'investment'
    if selection == "investment":                     
        
        investment = True
        while investment:
            try:
                # Display instructions to the user
                print("\nTo calculate the investment enter the following values in numbers.")           

                # Asking for the information needed from the user to do the calculation
                amount = float(input("\nEnter the amount you are planning to invest: "))       

                interest_rate = float(input("Enter the interest rate that you will receive: "))

                years = float(input("Enter the time of your investment in years. "))

                # Dividing interest rate to make it a float number smaller than 1 for the calculation 
                interest_rate = interest_rate / 100                                                            

                # Declaring the varibale that will act as condition for the investment calculator
                investment_calc = True

            except ValueError:
                print("\nINVALID DATA!! PLEASE ENTER NUMBERS ONLY.")

            else:                                      
                # Creating a loop to make sure the user input correctly 1 of the 2 options
                while investment_calc == True:        
                    
                    # Requesting type of interest and converting it to lowercase to be case insensitive for the comparison
                    type_interest = input("Please enter if the interest is 'simple' or 'compound'. ").lower()

                    # Checking if the user selected option 'simple'
                    if type_interest == "simple":                                      
                        
                        # Calculating investment with simple interest
                        investment = amount * (1 + interest_rate * years)              

                        # Display the result of investment rounded to 2 decimals
                        print(f"\nThe amount of money you will receive at the end of your investment is: {round(investment,2)}")    

                        # Making the condition False to finish the loop and go back to main menu
                        investment_calc = False
                        investment = False                                        

                    # Check if the user selected option 'compound'
                    elif type_interest == "compound":                                  
                        
                        # Calculating investment with compound interest
                        investment = amount * math.pow((1 + interest_rate), years)     

                        # Display the result of investment rounded to 2 decimals
                        print(f"\nThe amount of money you will receive at the end of your investment is: {round(investment,2)}")    

                        # Making the condition False to finish the loop
                        investment_calc = False                                        
                        investment = False
                    else:
                        # If the user does not input a correct option makes the variable True to start the loop again
                        print("\nInvalid option, try again.")
                        investment_calc = True                                              

    # Check if the selected option was 'bond'
    elif selection == "bond": 

        bond = True

        while bond:                                                 

            try:
                # Display instructions to the user
                print("\nTo calculate the bond repayments enter the following values in numbers.")     

                # Asking for the information needed from the user to do the calculation
                house_price = float(input("\nEnter the current value of the property: "))       

                interest_rate = float(input("Enter the interest rate that you will pay on the loan: "))

                months = int(input("Enter the time in months that you will take to repay the bond: "))
            
            except ValueError:
                print("\nINVALID DATA!! PLEASE ENTER NUMBERS ONLY.")

            else:
                # Dividing interest rate by 100 to make it a float number smaller than 1 for the calculation
                interest_rate = interest_rate / 100

                # Dividing interest rate by 12 to know monthly interest
                interest_rate = interest_rate / 12                                 

                # Calculating monthly repayments for the bond
                bond = ((interest_rate * house_price) / (1 - (1 + interest_rate) ** (-months)))      

                # Display the monthly repayments rounded to 2 decimals
                print(f"\nThe amount of money you will have to pay monthly is {round(bond,2)}")
                print(f"For a total of {round(bond*months,2)} in 120 months.")

                bond = False    
    
    # Check if the selected option was 'end'
    elif selection == "end":                                               

        # Display closing message
        print("\nClosing the calculator...\nGood bye!!")

        # Setting the variable to false to break out of the while loop and finalise the calculator
        calculator = False                                                 
    
    else:
        # If the previous conditions are not met make the variable calculator True to start the loop again
        print("\nInvalid option, try again.")
        calculator = True                                                  
