#We decided to keep everything within the function so no data needed to be called
#in from outside the function, and it allowed us to minimize repeated code.
def within_budget():

    name = None
#We applied a loop, so if no data is inputed (false) than the code will not continue until data is provided (true)
    while not name:
#The variable name is provided with meaning.
        name = input("Please enter your name: ")

#below are the variables for Salary, and the bills we have selected to conduct the budget analysis. 
    salary = int(input("Enter your monthly salary to the nearest dollar: "))
#Initially we had the grocery variable multiplied by 3 to reflect three trips a month since that was the average according to statistics
#but we decided on just keeping it on a total for the entire month.
    grocery_bill = int(input("How much do you spend a month on food to the nearest dollar?: $"))
    home_expense = int(input("How much is your mortgage or rent to the nearest dollar? $"))
    car_payment = int(input("What is your monthly car payment?"))

#Here is where we created an array to hold the totals of all of the bills.
    expenses = [grocery_bill, home_expense, car_payment]
#Below is where we added a constant which is 0, this is where the total expenses is initialized from.
    monthly_total = 0
#here is where it loops through the expenses we created.
    for expense in expenses:
#with the loop, it grabs in the monthly_total which is initialized at 0(constant)
#and adds the total of expenses to it.
        monthly_total += expense
#Below is where the total of all expenses and salary are compared and provides the user with the results based off
#what constraints are met. 
    print(f"Your total monthly expenses are ${monthly_total} ")

    if monthly_total > salary:

            print (f"{name},you're living above your means")

    elif monthly_total < salary:
            print (f"Good job {name} , you're within your budget!")
        
    else:

            print (f"{name}, please check the data provided.")
#this is the final piece that activates the function.
within_budget()
