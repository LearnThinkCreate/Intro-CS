"""
In Part B, you had a chance to explore how both the percentage of your salary that you save each month and your annual raise affect how long it takes you to save for a down payment. 
This is nice, but suppose you want to set a particular goal, e.g. to be able to afford the down payment in three years. 
How much should you save each month to achieve this? In this problem, you are going to write a program to answer that question. To simplify things, assume:
3
1. Your semi­annual raise is .07 (7%)
2. Your investments have an annual return of 0.04 (4%)
3. The down payment is 0.25 (25%) of the cost of the house
4. The cost of the house that you are saving for is $1M.

You are now going to try to find the best rate of savings to achieve a down payment on a $1M house in 36 months.
Since hitting this exactly is a challenge, we simply want your savings to be within $100 of the required down payment.
In​ ps1c.py​, write a program to calculate the best savings rate, as a function of your starting salary. 
You should use ​bisection search​ to help you do this efficiently. You should keep track of the number of steps it takes your bisections search to finish. 
You should be able to reuse some of the code you wrote for part B in this problem.
Because we are searching for a value that is in principle a float, we are going to limit ourselves to two decimals of accuracy (i.e., we may want to save at 7.04% ­­ or 0.0704 in decimal 
– but we are not going to worry about the difference between 7.041% and 7.039%). This means we can search for an integer​ between 0 and 10000 (using integer division),
 and then convert it to a decimal percentage (using float division) to use when we are calculating the ​current_savings​ after 36 months. By using this range, there are only a 
 finite number of numbers that we are searching over, as opposed to the infinite number of decimals between 0 and 1. This range will help prevent infinite loops. 
 The reason we use 0 to 10000 is to account for two additional decimal places in the range 0% to 100%. Your code should print out a decimal (e.g. 0.0704 for 7.04%).
"""
"""
I modified the script so that it shows what savings rate and return I would need to have over the next 9 years to be a millionaire
Variables to Change include Annual salary increase
Rate of investment returns 
Starting Salary
"""

# Intializing the variables
    ## Fixed Variables
#total_cost = 1000000
tolerance = 100 # Margin of error
    ## Input Variables
annual_salary = float(input("Enter your current annual salary: "))
down_payment = int(input("Enter your desired savings: "))
time = int(input("How many months in the future? "))
salary_raise = float(input("Enter your average annual raise (in decimal form): "))
r = float(input("Enter your Annual Rate of Return on Investments: "))

    ## Calculation Variables 
current_savings = 5000
steps = 0
     ## Guessing Variables
high = 1
low = 0
savings_rate  = 0

    ## Step 1: Testing the Condition
while abs(down_payment - current_savings) >= tolerance:
        ## Intializing current_savings to be 0 and portion saved to calculation new var
    current_savings = 5000
        ## Have to initialize the input salary for every loop
    input_salary = annual_salary
    monthly_savings = (input_salary * savings_rate)/12

    for months in range(time):
            ## Assignng the semiannual raise of 7%
        if months % 12 == 0 and months > 0:
            input_salary *= (1 + salary_raise)
            ## Finding the new monthly savings if there's a raise
            monthly_savings = (input_salary * savings_rate)/12
        ## Adding the monthly savings to the current savings
        current_savings += monthly_savings
        ## Multipling by the 
        current_savings *= (1 + r/12)
        ## Assigning Portion saved with Bisection
    if down_payment > current_savings:
        low = savings_rate
    else:
        high = savings_rate
    savings_rate = (high + low)/2
    ## The total amount of guesses
    steps += 1
    if steps > 13:
        break

if abs(down_payment - current_savings) >= tolerance:
    print("It is not possible to pay the down payment in three years")
else:
   print("How much you need to save: " , savings_rate)
   print("Steps in Bisection search: " , steps)        
   print("Salary " , time/12, " years in the future: " ,input_salary)


