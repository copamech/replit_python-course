print("Loan Calculator")
print("This calculator shows you how much your loan of $1,000 with a 5% APR compounds each year.")
print()

loan = 1000
apr = 0.05

for i in range(10):
  loan += (loan*apr)
  print("Year",i+1,"is",round(loan,2))
