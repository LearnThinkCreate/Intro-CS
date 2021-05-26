"""
Copy solution to Part A and modify to include the folowing
1. Have the user input a semi-annual salary raise ​semi_annual_raise​ (as a decimal percentage) 
2. After the 6t​h​ month, increase your salary by that percentage. Do the same after the 12t​h
month, the 18​th​ month, and so on.

Write a program to calculate how many months it will take you save up enough money for a down payment.
 Like before, assume that your investments earn a return of ​r​ = 0.04 (or 4%) and the required down payment 
 percentage is 0.25 (or 25%). Have the user enter the following variables:
1. The starting annual salary (annual_salary)
2. The percentage of salary to be saved (portion_saved)
3. The cost of your dream home (total_cost)
4. The semi­annual salary raise (semi_annual_raise)
"""

# Intializing the variables
        ## Creating the input variables that the user can enter 
annual_salary = float(input("Enter your annual salary "))
portion_saved = float(input("Enter the percent of your salary to save, as a deceimal "))
total_cost = float(input("Enter the cost of your dream home: "))
        ## Creating the calculation variables
portion_down_payment = total_cost *0.25
current_savings = 0
portion_saved_month = (annual_salary * portion_saved)/12
months = 0

## Loop runs until the current savings exceed the necessary amount for a down payment
while (portion_down_payment > current_savings):
    current_savings += portion_saved_month
        ## Multiplying the current savings to factor in 4% a year in appreciation 
    current_savings *= (1 + .1/12)
    months += 1
        ## Assignng the semiannual raise of 3%
    if months%6 == 0:
        annual_salary *= 1.03
        portion_saved_month = (annual_salary * portion_saved)/12

print("Number of months: " , months)
print(annual_salary)
print(portion_saved_month)