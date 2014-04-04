#calculates the cost of a meal taking tax and tips into account
cost=input('enter cost of the meal ' )

tax=0.0675*cost
print tax, 'rands was added for tax' 
tip=0.1*cost
print tip,'rands extra for the tip'
totalcost=cost+tip
print totalcost, 'is the total amount to be paid'