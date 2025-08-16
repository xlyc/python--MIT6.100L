## 6.100A PSet 1: Part B
## Name: starrain0
## Time Spent: 00:08:00
## Collaborators: none

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
months = 0
amount_saved = 0

down_payment = 0.25 * cost_of_dream_home
monthly_salary = yearly_salary / 12

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while amount_saved < down_payment:
    amount_saved += (monthly_salary * portion_saved + amount_saved * (0.05/12))
    if (months!=0 and months %6 == 0):
        monthly_salary *= (1 + semi_annual_raise)
    months += 1
print(f"Number of months : {months}")
