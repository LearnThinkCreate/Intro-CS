"""
You have graduated from MIT and now have a great job! You move to the San Francisco Bay Area
 and decide that you want to start saving to buy a house. As housing prices are very high in the Bay Area, 
 you realize you are going to have to save for several years before you can afford to make the down payment 
 on a house. In Part A, we are going to determine how long it will take you to save enough money to make the 
 down payment given the following assumptions:
    1. Call the cost of your dream home ​total_cost​.
    2. Call the portion of the cost needed for a down payment ​portion_down_payment​. For
simplicity, assume that portion_down_payment = 0.25 (25%).
    3. Call the amount that you have saved thus far ​current_savings​. You start with a current
savings of $0.
    4. Assume that you invest your current savings wisely, with an annual return of ​r ​(in other words,
at the end of each month, you receive an additional ​current_savings*r/12​ funds to put into 
your savings – the 12 is because ​r​ is an annual rate). Assume that your investments earn a return of r = 0.04 (4%).
    5. Assume your annual salary is ​annual_salary​.
    6. Assume you are going to dedicate a certain amount of your salary each month to saving for
the down payment. Call that ​portion_saved​. This variable should be in decimal form (i.e. 0.1
for 10%).
    7. At the end of each month, your savings will be increased by the return on your investment,
plus a percentage of your ​monthly salary ​(annual salary / 12).
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


while (portion_down_payment > current_savings):
    current_savings += portion_saved_month
    current_savings *= (1 + .04/12)
    months += 1

print("Number of months: " , months)