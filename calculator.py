print("Welcome to the tip calculator!")
print(" ")
total_bill = float(input("What was the total bill? "))

tip_given1 = float(input("How much tip would you like to give? 10%, 12%, 15%? "))
tip_given2 = (tip_given1 / 100 ) * total_bill



people_splitting_the_bill = int(input("How many people are going to split the bill? "))

each_person_should_pay = (total_bill + tip_given2) / people_splitting_the_bill
each_person_should_pay = round(each_person_should_pay, 2)

print(f"Each person should pay ${each_person_should_pay}")


