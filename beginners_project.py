# # ----- STUDENT GRADING SYSTEM -----

# def average(scores):
#     return sum(scores)/len(scores)

# def grade_system(avg):
#     if avg >= 70:
#         return "A"
#     elif avg >= 60:
#         return "B"
#     elif avg >= 50:
#         return "C"
#     elif avg >= 40:
#         return "D"
#     else:
#         return "F"
    
# def highest_score(scores):
#     return max(scores)

# def lowest_score(scores):
#     return min(scores)

# def status(avg):
#     if avg >= 50:
#         return "PASS"
#     else:
#         return "FAIL"
    
# def total_score(scores):
#     return sum(scores)

# while True:
#     scores = []
#     subjects = ["Mathematics","English", "Biology", "Chemistry", "Physics"]

#     student = input("Enter your name: ")

#     for subject in subjects:
#         score = int(input(f"{subject} : "))
#         scores.append(score)

#     avg = average(scores)
#     grade = grade_system(avg)
#     high = highest_score(scores)
#     low = lowest_score(scores)
#     stats = status(avg)
#     total = total_score(scores)

#     print(f"Student Name: {student}")
#     print(f"Average = {avg:.2f}")
#     print(f"Highest score = {high}")
#     print(f"Lowest score = {low}")
#     print(f"Grade = {grade}")
#     print(f"Status = {stats}")
#     print(f"Total Score = {total}")

#     break

# ---- NUMBER GUESSING GAME ------

# secret_number = 10
# user_guess = None
# guess_count = 0
# out_of_guesses = False
# guess_limit = 3

# while user_guess != secret_number and not(out_of_guesses):
#     if guess_count < guess_limit:
#         user_guess = int(input("Enter a guess number: "))
#         guess_count += 1
#     else:
#         out_of_guesses = True

# if out_of_guesses:
#     print("You are out of guesses. SO SORRY, YOU LOSE!")
# else:
#     print("YOU WIN!")

# -----  ATM SIMULATOR ----

# balance = 100000

# def check_balance():
#     print(f"Your Balance = {balance}")

# def deposit():
#     global balance
#     amount = int(input("Enter the amount to be deposited: "))
#     if amount <= 0:
#         print("Invalid amount")
#     else:
#         balance += amount
#         print(f"{amount} deposited successfully!")

# def withdraw():
#     global balance
#     amount = int(input("Enter an amount to withdraw: "))

#     if amount > balance:
#         print("Insufcient funds")
#     elif amount <= 0:
#         print("Invalid amount")
#     else:
#         balance -= amount
#         print(f"{amount} withdawn successfully!")

# while True:
#     print("---- ATM SIMULATION -----")
#     print("1. Check Balance ")
#     print("2. Deposit ")
#     print("3. Withdraw ")
#     print("4. Exit ")

#     choice = int(input("Pick an option: "))

#     if choice == 1:
#         check_balance()
#     elif choice == 2:
#         deposit()
#     elif choice == 3:
#         withdraw()
#     elif choice == 4:
#         print("Thanks for stopping by. GoodBye!!!")
#         break
#     else:
#         print("Invalid Option")
#         break

# ---- TO DO LIST APP ------

# tasks =[]

# def add_task():
#     task = input("Enter a task to add: ")
#     tasks.append(task)
#     print(f"{task} added successfully!")

# def view_task():
#     if len(tasks) == 0:
#         print("No task added yet!")
#     else:
#         for task in tasks:
#             print("-", task)

# def remove_task():
#     task = input("Enter task to delete: ")
#     if task not in tasks:
#         print(f"{task} not found in list")
#     else:
#         tasks.remove(task)
#         print(f"{task} deleted successfully!")

# while True:
#     print(" \n TO-DO-LIST APP")
#     print("1. Add task ")
#     print("2. Remove task ")
#     print("3. View task ")
#     print("4. Exit ")

#     choice = int(input("Pick an option: "))

#     if choice == 1:
#         add_task()
#     elif choice == 2:
#         remove_task()
#     elif choice == 3:
#         view_task()
#     elif  choice == 4:
#         print("Done for the day. GooBye!!!")
#         break
#     else:
#         print("Invalid option")

# ------ COURSE REGISTRATION SYSTEM -------

# register_course =  []
# drop_course = []

# def registered_course():
#     course = input("Enter the course to be registered: ")
#     if course in register_course:
#         print(f"{course} registered already!")
#     else:
#         register_course.append(course)
#         print(f"{course} registered successfully!")

# def dropped_course():
#     course = input("Enter the course to drop: ")
#     if course in register_course:
#         register_course.remove(course)
#         # drop_course.append(course)
#         print(f"{course} deselected successfully!")
#     else:
#         print(f"{course} not among regsitered courses")

# def view_registered_courses():
#     if len(register_course) == 0:
#         print("No course registered yet!")
#     else:
#         for course in register_course:
#             print("-", course)

# while True:
#     print("\n STUDENT COURSE REGISTRATION")
#     print("1. Register Courses: ")
#     print("2. Drop Courses: ")
#     print("2. View Courses: ")
#     print("4. Exit")

#     choice = int(input("Pick an option: "))

#     if choice == 1:
#         registered_course()
#     elif choice == 2:
#         dropped_course()
#     elif choice == 3:
#         view_registered_courses()
#     elif choice == 4:
#         print("Congratulations on successfully registering your courses. GoodBye!!!")
#         break
#     else:("Invalid option")

# ----- CONTACT BOOK -----

# contacts = {}

# def add_contacts():
#     name = input("Enter a name: ")
#     phone = input("Enter a phone number: ")
#     contacts[name] = phone
#     print(f"{name} added successfully!")

# def search_contacts():
#     name = input("Search for a name: ")
#     if name in contacts:
#         print(f"{name} : {contacts[name]}")
#     else:
#         print(f"{name} not in contact list yet")

# def delete_contacts():
#     name = input("Enter a name to delete: ")
#     if name in contacts:
#         del contacts[name]
#         print(f"{name} deleted successfully!")
#     else:
#         print(f"{name} not found in contact list")

# def view_contacts():
#     if len(contacts) == 0:
#         print("No contacts stored yet!")
#     else:
#         for name, phone in contacts.items():
#             print(f"{name} : {phone}")  

# while True:
#     print("\n CONTACT BOOKS")
#     print("1. Add Contacts. ")
#     print("2. Search Contacts. ")
#     print("3. Delete Contacts. ")
#     print("4. View Contacts. ")
#     print("5. Exit")

#     choice = int(input("Pick an option: "))

#     if choice ==  1:
#         add_contacts()
#     elif choice == 2:
#         search_contacts()
#     elif choice == 3:
#         delete_contacts()
#     elif choice == 4:
#         view_contacts()
#     elif choice == 5:
#         print("GoodBye!!!")
#         break
#     else:
#         print("Invalid Option")

# ----- INVENTORY MANAGEMENT SYSTEM -----

# shop_inventory = {}

# def add_products():
#     product = input("Product name: ")
#     quantity = int(input("Quantity: "))
#     shop_inventory[product] = quantity
#     print(f"{product} added to inventory successfully!")

# def update_quantity():
#     product = input("Product Name: ")
#     quantity = int(input("New Quantity: "))
#     if product in shop_inventory:
#         shop_inventory[product] = quantity
#         print(f"{product} quantity updated succesfully!")
#     else:
#         print(f"{product} not present in inventory")

# def remove_products():
#     product = input("Product Name: ")
#     # quantity = int(input("Quantity: "))
#     if product in shop_inventory:
#         del shop_inventory[product]
#         print(f"{product} removed from inventory successfully!")
#     else:
#         print(f"{product} not found in inventory")

# def view_inventory():
#     if len(shop_inventory) == 0:
#         print("No inventory added yet!")
#     else:
#         for product, quantity in shop_inventory.items():
#             print(f"- {product} = {quantity}")

# while True:
#     print("\n INVENTORY MANAGEMENT SYSTEM")
#     print("1. Add Products. ")
#     print("2. Update Products. ")
#     print("3. Remove Products. ")
#     print("4. View Inventory. ")
#     print("5. Exit. ")
    
#     choice = int(input("Pick an option: "))

#     if choice == 1:
#         add_products()
#     elif choice == 2:
#         update_quantity()
#     elif choice == 3:
#         remove_products()
#     elif choice == 4:
#         view_inventory()
#     elif choice == 5:
#         print("Thnaks for checkinf in today. GoodBye!!!")
#         break
#     else:
#         print("Enter a valid option")

# ---- QUIZ APPLICATION -------

# quiz = {
#     "What is the capital of Nigeria?": "Abuja",
#     "Which planet is known as the Red Planet?": "Mars",
#     "How many continents are there on Earth?": "7",
#     "What is 2 + 2?": "4",
#     "Who wrote Python programming language?": "Guido van Rossum",
#     "What is the largest ocean on Earth?": "Pacific",
#     "What is the boiling point of water in Celsius?": "100",
#     "Which animal is known as the King of the Jungle?": "Lion",
#     "What is the currency of the United States?": "Dollar",
#     "How many days are there in a leap year?": "366"
# }

# def run_quiz(quiz):
#     score = 0

#     for question, answer in quiz.items():
#         print(f"{question}: ")
#         user_answer = input("Answer: ")

#         if user_answer.strip().lower() == answer.lower():
#             score += 1
#     return score

# def show_result(score, total):
#     print("\n RESULT CHECKER")
#     print(f"Score = {score}/{total}")

#     if score >= 8:
#         print("Remark: Excellent")
#     elif score >= 5:
#         print("Remark: Good")
#     else:
#         print("Remark: Fail")
    
# score = run_quiz(quiz)
# show_result(score, len(quiz))

# --------- MINI BANKING SYSTEM --------

# accounts = {}
# next_account_number = 1001

# def create_account():
#     global next_account_number

#     account_number = str(next_account_number)
#     account_name = input("Enter Name: ")
#     account_pin = input("Create a 4-digit PIN: ")
#     initial_deposit = int(input("First Deposit "))
#     accounts[account_number] = {
#         "name" : account_name,
#         "pin" : account_pin,
#         "balance" : initial_deposit
#     }
#     print(f"Your Account Number is {account_number}")
#     print("Account created successfully!")

#     next_account_number += 1

# def deposit():
#     account_number = input("Enter account number: ")
   
#     if account_number in accounts:
#         account_pin = input("Enter a 4-digit PIN: ")
#         if account_pin == accounts[account_number]["pin"]:
#             amount = int(input("Enter an amount: "))
#             if amount <= 0:
#                 print("Invalid amount, please enter a valid amount")
#             else:
#                 accounts[account_number]["balance"] += amount
#                 print(f"{amount} deposited successfully!")
#                 print(f"Total Blance = {accounts[account_number]['balance']}")
#         else:
#             print("Incorrect PIN. Try again!")
#     else:
#         print(f"Sorry your account number {account_number} doesn't exist")      

# def withdraw():
#     account_number = input("Enter account number: ")
#     if account_number in accounts:
#         account_pin = input("Enter a 4-digit PIN: ")
#         if account_pin == accounts[account_number]["pin"]:
#             amount = int(input("Enter amount: "))
#             if amount <= 0:
#                 print("Invalid amount, please enter a valid amount")
#             elif amount > accounts[account_number]["balance"]:
#                 print("Insufficient funds!")
#             else:
#                 accounts[account_number]['balance'] -= amount
#                 print(f"{amount} withdrawn sucessfully!")
#                 print(f"Total Blance = {accounts[account_number]['balance']}")
#         else:
#             print("Incorrect PIN. Try again")
#     else:
#         print(f"Sorry your account numbr {account_number} doesn't exist")

# def transfer():
#     sender = input("Enter sender account: ")
#     receiver = input("Enter receiver account: ")

#     if sender in accounts and receiver in accounts:
#         sender_pin = input("Enter a 4-digit PIN: ")

#         if sender_pin == accounts[sender]["pin"]:
#             amount = int(input("Enter amount: "))

#             if amount <= 0:
#                 print("Invalid amount, please enter a valid amount")

#             elif amount> accounts[sender]["balance"]:
#                 print("Sender has insufficient funds!")

#             else:
#                 accounts[sender]["balance"] -= amount
#                 accounts[receiver]["balance"] += amount
#                 print(f"{amount} transfered sucessfully!")
#                 print(f"{sender} remaining Blance = {accounts[sender]['balance']}")

#         else:
#              print("Incorrect PIN. Try again")

#     else:
#         print("Either of both account is not correct, so please check well")

# def check_balance():
#     account_number = input("Enter account number: ")
#     account_pin = input("Enter your 4-digit pin: ")

#     if account_number in accounts:
#         if account_pin == accounts[account_number]["pin"]:
#             print(f"Your balance is = {accounts[account_number]['balance']}")
#         else:
#             print("Incorrect PIN")
#     else:
#         print("Invalid account number")


# while True:
#     print("\n ---- MINI BANKING SYSTEM ----")
#     print("1. Create account. ")
#     print("2. Withdraw. ")
#     print("3. Deposit. ")
#     print("4. Transfer")
#     print("5. Check Balance. ")
#     print("6. Exit. ")

#     choice = int(input("Pick an option: "))

#     if choice == 1:
#         create_account()
#     elif choice == 2:
#         withdraw()
#     elif choice == 3:
#         deposit()
#     elif choice == 4:
#         transfer()
#     elif choice == 5:
#         check_balance()
#     elif choice == 6:
#         print("Thank you for stoping by. GoodBye!!!")
#         break
#     else:
#         print("Please enter a vald option ")
    