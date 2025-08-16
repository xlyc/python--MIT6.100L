## 6.100A PSet 1: Part C
## Name: starrian0
## Time Spent: 01:00:00
## Collaborators: None

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
down_payment = 800000*0.25
amount_saved=initial_deposit
max_amount_saved=initial_deposit*(1+1/12)**36
r=0.00
months=36
steps=0;left=0;right=1

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

while abs(amount_saved-down_payment)>100:
    if max_amount_saved<down_payment:
        r=None
        break
    steps+=1
    r=(left+right)/2
    amount_saved=initial_deposit*(1+r/12)**months
        
    if amount_saved>down_payment+100:
        right=r
    elif amount_saved<down_payment-100:
        left=r

print(f"Best savings rate: {r}")
print(f"Steps in bisection search: {steps}")
