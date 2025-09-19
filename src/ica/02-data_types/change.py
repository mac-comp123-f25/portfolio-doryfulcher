money=732 #Define total money in cents
dollars=money//100
money=money%100
quarters=money//25
money=money%25
dimes=money//10
money=money%10
nickels=money//5
money=money%5
pennies=money
print(dollars)
print(quarters)
print(dimes)
print(nickels)
print(pennies)