print("Welcome to tip calculator")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
total_person = int(input("How many people to split the bill? "))
splited_bill = "{:.2f}".format(((total_bill * (tip_percentage/100)) + total_bill)/total_person)
print(f"Each person should pay: {splited_bill}")