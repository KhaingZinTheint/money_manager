def expense():
    total = 0
    exp = 0
    others_exp = 0
    while True:
        salary = float(input("Your total salary: "))
        food = float(input("Your total food expenses: "))
        bills = float(input("Your total bill expenses: "))
        shopping = float(input("Your total shopping expenses: "))
        edu = float(input("Your total education expenses: "))
        donation = float(input("Your total donation expenses: "))
        saving = float(input("Your total saving : "))
        others = input("Do you have any other expenses?yes/no: ")
        if others[0] == "n":
           total = salary - (food+bills+shopping+edu+donation+saving)
           exp = food+bills+shopping+edu+donation+saving
           break
        elif others[0] == "y":
           others_exp = float(input("Your other expenses: "))
           total = salary - (food+bills+shopping+edu+donation+saving+others_exp)
           exp = food+bills+shopping+edu+donation+saving+others_exp
           break
        else:
           print("Please only put yes/no only.")
           
    print("\nExpense Summary:")
    print("Salary: \t\t", salary)
    print("Food Expenses: \t\t", food)
    print("Bills Expenses: \t", bills)
    print("Shopping Expenses: \t", shopping)
    print("Education Expenses: \t", edu)
    print("Donation Expenses: \t", donation)
    print("Saving: \t\t", saving) 
    if others_exp > 0:
        print("Other Expenses: \t", others_exp)
   
    
    print(".....................................")          
    print(f"Your total  expense is {exp}")
    print(f"Your avaliable balance is {total}")


def main():
    print("Welcome from our money manager!")
    print("Are you ready to check your monthly expense!")
    print("...................................................")
    expense()
    
main()
