print("Welcome to the tip Calculator")
bill=float(input("What was the total bill? $"))
tip=(float(input("How much tip would you like to give? 10, 12, or 15? "))/100)+1
number_of_persons=int(input("How many people to split the bill? "))
total_for_each=bill*tip/number_of_persons
print(f"Each person should pay: ${round(total_for_each,2)}")