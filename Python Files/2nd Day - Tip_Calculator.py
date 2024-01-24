print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_perct = float(input("What percentage you would like to give? 10, 12, 15, or how much you want? %"))
people_count = int(input("How many people to split the bill? "))

result_per_person = round( ( bill*(100+tip_perct)/100 ) / people_count , 2) 

print(f"Each person should pay ${result_per_person}.")
