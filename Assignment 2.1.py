# Interacting with the user 
Greeting = input("What is your name: ")
print ("Welcome to my Loan Qualifier Program", Greeting )

#alerting user that the program is not designed to accept commas
Message = "Please enter integer values without a comma" 
print (Message)

# Requesting for basic information to assess user's eligibility for loan
house_price = int(input("What is the price of you dream house? "))

#alerting user to input gross income
Text = "Please input salary before tax"
print (Text)

salary = int(input("What is your salary? "))
credit_score = int(input("What is your credit score? "))
employee_tenure = int(input("How many years have you been at your job? "))

# Asking program to bring output based on user's information input
if salary >= (house_price) * 0.2:
    if credit_score >= 650:
        if employee_tenure >=3:
            print("You might qualify for a loan")
            print ('Please hold...')
            import time 
            time.sleep (5)
            print ("CONGRATULATIONS!!! Your loan request is approved")
            print( Greeting, "please contact 555-555-5555 for information about how the loan would be disbursed to your account.")        
        else: 
            print ("You need to have been employed for at least 3 years to qualify for this loan.")
    else:
        print ("You need to improve your credit score")
        print("A minimum of 650 is required")

else:
    print(Greeting, "a higher salary is needed to qualify for this loan.")


print("Thank you for using my Loan Qualifier Program!") 