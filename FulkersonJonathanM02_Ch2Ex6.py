# Tax and Total Calculator
# By Jonathan Fulkerson
# This program will allow the user to input a base purchase price (or subtotal). The program will
# use the base purchase price to determine the state tax, couty tax, and add them together
# to calculate the total purchase price. Once the prices have been determined it will
# display each price individually to the user.

basePrice = float(input("What was the amount of your purchase?"))
basePrice = round(basePrice, 2)
stateTax = round(basePrice * 0.05, 2)
countyTax = round(basePrice * 0.025, 2)
totalPrice = (basePrice + stateTax + countyTax)

print ("Purchase price = $" + str(basePrice))
print ("State Sales Tax = $" + str(stateTax))
print ("County Sales Tax = $" + str(countyTax))
print ("Total Purchase Price = $" + str(totalPrice))

print ("Written by Jonathan Fulkerson")
