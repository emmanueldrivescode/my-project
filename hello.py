# ---------- To Do List ---------

# tasks = []

# while True:
#     print("-- To Do List --")
#     print("1. Add task... ")
#     print("2. Remove task... ")
#     print("3. View task... ")
#     print("4. Exist... ")

#     choice = input("Pick a number from the above? ")

#     if choice == "1":
#         add_items = input("Enter a task to add: ")
#         tasks.append(add_items)
#         print("Task added succesfully!")
#     elif choice == "2":
#         remove_items = input("Enter a task to remove: ")
#         if remove_items in tasks:
#             tasks.remove(remove_items)
#             print("Task removed successfully!")
#         else:
#             print("Task not found!")
#     elif choice == "3":
#         print("-- Your tasks --")
#         if len(tasks) == 0:
#             print("No task has been added yet!")
#         else:
#             for task in tasks:
#                 print("-", task)
#     elif choice == "4":
#         print("GoodBye!!!")
#         break
#     else:
#         print("Invalid choice")

# ------ Student Scpre Tracker -------------

# scores = []

# while True:
#     score = input("Enter a score or type 'done' to end the program: ")

#     if score == "done":
#         break

#     scores.append(float(score))

# print("Your scores are: \n", scores)

# if len(scores) > 0:
#     high = max(scores)
#     low = min(scores)
#     avg = sum(scores)/len(scores)

#     print(highest_number)
#     print(lowest_numbers)
#     print(avg)

# else:
#     print("No scores has been entered yet!")

# --------- Shoping List --------

# shopping_list = []

# while True:
#     print("--- Shopping Quota ---")
#     print("1. Add Item... ")
#     print("2. Remove Item... ")
#     print("3. Total Item... ")
#     print("4. View Item... ")
#     print("5. Exit... ")

#     choice = input("Pick an option from the list above: ")

#     if choice == "1":
#         add = input("Enter an item to add: ")
#         shopping_list.append(add)
#         print(add, "has been added to your shopping list.")
#     elif choice == "2":
#         remove = input("Enter an item to remove: ")
#         if remove.lower() in shopping_list:
#             shopping_list.remove(remove)
#             print(remove, "has been deleted from your shopping list.")
#         else:
#             print(remove, "has not been included in oyur shopping list yet")
#     elif choice == "3":
#         if len(shopping_list) > 0:
#             print("Total Items: ", len(shopping_list))
#         else:
#             print("No item has been added yet!")
#     elif choice == "4":
#         print("-- Your Items --- \n")
#         for item in shopping_list:
#             print("-", item)
#     elif choice == "5":
#         print("GoodBye!!!... ")
#         break

# ------ Word Filter Program ------

# words = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'pineapple', 'grape', 'watermelon', 'orange', 'strawberry']

# new_words = []
# for word in words:
#     if "a" in word or len(word) < 5:
#         new_words.append(word)

# new_words = [word for word in words if "e" in word and len(word) > 5]

# print(new_words)

# ----- Number Analyzer ---------

# numbers =  []

# while True:
#     number = input("Enter a number or type 'done' to end the progran: ")

#     if number.lower() == 'done':
#         break

#     numbers.append(float(number))

# if len(numbers) > 0:
#     even = [num for num in numbers if num %2 == 0]
#     odd = [num for num in numbers if num %2 != 0]
#     high = max(numbers)
#     low = min(numbers)
#     avg = sum(numbers)/len(numbers)

#     print("Even Numbers: ", even)
#     print("Odd Numbers: ", odd)
#     print("Highest Number: ", high)
#     print("Lowest Number: ", low)
#     print("Average: ", avg)
# else:
#     print("No number has been added yet!")

# --------  QUiz Game ------------

# questions = [
#     'What is the capital of Nigeria?',
#     'What planet is known as the Red Planet?',
#     'How many days are in a leap year?',
#     'Who invented Telephone?',
#     'What is the largest ocean in the world?',
#     'Which animal is called the king of the Jungle?',
#     'What is the boiling point of water?',
#     'What continent is Egypt?',
#     'What gas do humans breathe in to survive?',
#     'How many continents are there in the world?'
# ]

# anwers = [
#     'Abuja',
#     'Mars',
#     '366 days',
#     'Grahams Bell',
#     'Pacific Ocean',
#     'Lion',
#     '100c',
#     'Africa',
#     'Oxygen',
#     '7',
# ]

# score = 0

# for i in range(len(questions)):
#     print("Question ", i +1, ": ")
#     print(questions[i])

#     user_answer = input("Anwer: ")

#     if user_answer.strip().lower() == anwers[i].lower():
#         print("Correct")
#         score +=1
#     else:
#         print("Worng answer!")

# print("Game Over!")
# print("You got", score, "over", len(questions))

#----- Dictionaries ----------

# student1 = {
#     'name' : 'Emmanuel',
#     'matricNo' : 'F/ND/2/3210067',
#     'course' : 'Computer science'
# }
# student2 = {
#     'name' : 'Pamilerin',
#     'matricNo' : 'F/ND/2/3210114',
#     'course' : 'Computer science'
# }
# student3 = {
#     'name' : 'Deborah',
#     'matricNo' : 'F/ND/2/3210185',
#     'course' : 'Computer science'
# }

# student_info = {
#     'student1' : student1,
#     'student2' : student2,
#     'student' : student3,
# }

# student_info = {
#     'student1' : {
#         'name' : 'Pamilerin',
#         'matricNo' : 'F/ND/2/3210114',
#         'course' : 'Computer science'
#     },
#     'student2' : {
#         'name' : 'Deborah',
#         'matricNo' : 'F/ND/2/3210185',
#         'course' : 'Computer science'
#     },
#     'student3' : {
#         'name' : 'Oyemesi',
#         'matricNo' : 'F/ND/2/3210067',
#         'course' : 'Computer science'
#     }
# }

# print(student_info['student1']['matricNo'])
# print(student_info['student2']['matricNo'])
# print(student_info['student3']['matricNo'])


# phonebook = {
#     'Emmanuel' : '07068960114',
#     'Toyosi' : '08144283848',
#     'Bidemi' : '09065826119',
#     'Powell' : '08055353436',
#     'Ore' : '09122334455',
# }

# user_input = input('Enter a name: ').lower().strip()

# if user_input in phonebook:
#     print(phonebook[user_input])

# else:
#     print('Contact not found')

#------ Practcial exercise ---------

# print("--- Welcome to our Customer servie, what would you like us to offer you? ")
# print("1. Buy Airtime... ")
# print("2. Buy Data... ")
# print("3. Borrow Credit... ")
# print("4. Check Balance... ")

# choose = int(input("Pick an option: "))

# match choose:
#     case 1:
#         user1 = input("Pick from the options below: \n 1. 100\n 2. 200 \n 3. 500 \n 4. 1000 \n 5. 1500 \n")

#         if user1 in ['1', '2' '3' '4' '5']:
#             print("Airtime purchased succesfully!")

#     case 2:
#         print("Pick from the options below: \n 1. Daily Plan \n 2. Weekly Plan \n 3. Monthly Plan \n 4. Unlimited")

#         user2 = (input("Choose a data plan: "))

#         if user2 == "1": 
#             print("1. 100 = 110MB \n 2. 200 = 230MB \n 3. 500 = 1GB \n 4. 1000 = 3.2GB")
#         elif user2 == "2":
#             print("1. 1000 =  3.5GB \n 2. 1500 = 5.5GB \n 3. 2000 = 7GB \n 4. 5000 = 10GB")
#         elif user2 == "3":
#             print("1. 5000 =  10GB \n 2. 7500 = 13GB \n 3. 10000 = 20GB \n 4. 20000 = 40GB")
#         elif user2 == "4":
#             print("Dail *312*1*2#...")
#         else:
#             print("Choose a valid Data plan")
#     case 3:
#         print("Dail *303# to borrow airtime")
#     case 4:
#         user4 =  input("To check your balance type in 1: ")

#         if user4 == "1":
#             print("You have sufficient airtime")
#         else:
#             print("Insuffcient airtime")
#     case _:
#         print("Invalid Option!")

#-- WHile & For Loop -------

# i = 0

# while i < 10:
#     i += 1
#     if i == 5:
#         continue
#     print(i)

# for i in range(2, 51, 2):
#     print(i)

# total = 0

# for i in range(1, 101):
#     total += i

# print(total)

# i = 10

# while i >= 1:
#     print(i)
#     i -= 1

# print("Blast Off!")

# number = int(input("Enter a number: "))

# for i in range(1, 13):
#     print(number, "x", i, "=", number * i)

# secret_number = 10
# user_guess = ""

# while secret_number != user_guess:
#     user_guess = int(input("Enter a secret number: "))

# else:
#     print("You win!")

# bal = 100000

# while True:
#     print("--- ATM Menu ---")
#     print("1. Check Balance.")
#     print("2. Deposit.")
#     print("3. Withdraw.")
#     print("4. Exit.")

#     user = int(input("Pick an option: "))

#     match user:
#         case 1:
#             print(bal)
#         case 2:
#             deposit = int(input("Enter the amount to deposit: "))
#             bal += deposit
#             print("Money deosited succesfully!")
#             print("Total Balance:", bal)
#         case 3:
#             withdraw = int(input("Enter the amount to withdraw: "))

#             if withdraw <= bal:
#                 bal -= withdraw
#                 print("Withdrawal succesfull!")
#                 print("Remaining Balance =", bal)
#             else:
#                 print("Insufficient funds!")
#         case 4:
#             print("GoodBye!!!")
#             break
#         case _:
#             print("Inavlid option, Try again!")

# scores = []

# while True:
#     score = input("Enter score or type 'done' to end the program: ")

#     if score == 'done':
#         break
#     else:
#         scores.append(int(score))

# print("Scores: ", scores)

# if len(scores) > 0:
#     print("Highest Number: ", max(scores))
#     print("Lowest Number: ", min(scores))
#     print("Average: ", sum(scores)/len(scores))
#     print("Total Number: ", len(scores))
# else:
#     print("No scores added yet!")

# username = "Emmanuel"
# password = "12345"
# guess_username = ""
# guess_password = ""
# guess_count = 0
# guess_limit = 5
# out_of_guess = False

# while (guess_username != username) or (guess_password != password) and not(out_of_guess):
#     if guess_count < guess_limit:
#         guess_username = input("Enter your username: ").lower()
#         guess_password = input("Enter your password: ")
#         guess_count += 1
#     else:
#         out_of_guess  = True

# if  out_of_guess:
#     print("No more chance, YOU LOOSE!")
# else:
#     print("YOU WIN!")

#----- Mini Restaurant Menu -----

# orders = []
# total = 0

# menu = {
#     1 : ("Rice and Chicken", 3500),
#     2 : ("Bread and Beans", 2500),
#     3 : ("Yam and Egg", 3000),
#     4 : ("Jolof Rice", 4000),
#     5 : ("Sharwama", 5000),
#     6 : ("Burger", 4500),
#     7 : ("Pizza", 8000),
#     8 : ("Soft Drink", 1000),
#     9 : ("Ice Cream", 2000),
# }

# while True:
#     print("--- RESTAURANT MENU ---")

#     for key, value in menu.items():
#         print(key, ".", value[0], "= #" + str(value[1]))

#     print("10. Exit")

#     choice = int(input("Pick an option from the menu: "))

#     if choice in menu:
#         food_name, price = menu[choice]
#         orders.append(food_name)
#         total += price

#         print(food_name, "added succesfully")

#     elif choice == 10:
#         print("Your Orders:")

#         for food in orders:
#             print("-", food)

#         print("Total Bill =", total)
#         break

#     else:
#         print("Invalid option")

#----- FUNCTIONs ------

# def myfunction(username, **kwargs):
#     print('My username is', username)
#     print('My name is', kwargs['name'])
#     print('Age:', kwargs['age'])
#     print('School:', kwargs['school'])

# myfunction('Loneerr', name = 'Emmanuel', age = 21, school = 'YABATECH')


# x = 'global'

# def outerFunction():
#     x = 'Outer'
#     def innerFunction():
#         x = 'Inner'
#         print('Inner:', x)
#     innerFunction()
#     print('Outer:', x)

# outerFunction()
# print('Global:', x)

# def outerFunction():
#     x = 'Henry'
#     def innerFunction():
#         nonlocal x
#         x = 'David'
#         print(x)
#     innerFunction()
#     # print(x)

# outerFunction()

# def changelook(func):
#     def myinner(*args, **kwargs):
#         return func(*args, **kwargs).upper()
#     return myinner

# @changelook
# def myFunction(name, greetings, gender):
#     return "Hello " + name + ' ' + greetings + ' ' + gender

# print(myFunction('World', 'welcome', gender = 'boy'))

# def changecase(n):
#     def changecase(func):
#         def myinner():
#             if n <= 5:
#                 a = func().upper()
#             else:
#                 a = func().lower()
#             return a
#         return myinner
#     return changecase

# @changecase(12)
# def myFunction():
#     return 'Hello Sally'

# print(myFunction())

# import functools

# def add_a_greetings(func):
#     @functools.wraps(func)
#     def myinner():
#         return 'Hello ' + func() + '. Welcome to our humble abode'
#     return myinner

# def changecase(func):
#     @functools.wraps(func)
#     def myinner():
#         return func().upper()
#     return myinner

# @changecase
# @add_a_greetings
# def myFunction():
#     return 'Emmanuel'

# print(myFunction())

# print(myFunction.__name__)

# numbers =  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# doubler = list((filter(lambda x  : x % 2 == 0, numbers)))

# print(doubler)
# students = [('Emmanuel', 26), ('Abraham', 22), ('Deborah', 34)]
# sorted_student = sorted(students, key=lambda x: len(x))

# print(sorted_student)

# def average(scores):
#     return sum(scores)/len(scores)

# def grade_system(avg):
#     if avg >= 70:
#         return 'A'
#     elif avg >= 60:
#         return 'B'
#     elif avg >= 50:
#         return 'C'
#     elif avg >= 40:
#         return 'D'
#     else:
#         return 'F'
    
# while True:
#     scores = []

#     student = input('Your name: ')

#     print('Enter the scores for the following subjects --')
#     scores.append(int(input('Mathematics: ')))
#     scores.append(int(input('English: ')))
#     scores.append(int(input('Biology: ')))
#     scores.append(int(input('Chemistry: ')))
#     scores.append(int(input('Physics: ')))

#     avg = average(scores)
#     grade = grade_system(avg)

#     print(f'Student Name: {student}')
#     print(f'Average: {avg}')
#     print(f'Grade: {grade}')

#     break

# balance = 500000

# def check_balance():
#     print(f'Your Balance = {balance}')

# def deposit():
#     global balance
#     amount =float(input('Enter amount to deposit: '))

#     if amount > 0:
#         balance += amount
#         print(f'{amount} deposited succesfully!!')
#     else:
#         print('Invalid amount')

# def withdraw():
#     global balance
#     amount = float(input('Enter the amount to withdraw: '))

#     if amount > balance:
#         print('Insuffcient funds!')
#     elif amount <= 0:
#         print('Invalid amount!')
#     else:
#         balance -= amount
#         print(f'{amount} withdrawn succesfully!')
    
# while True:
#     print('---- ATM MAINTENANCE ----')
#     print('Choose from the options below: ')
#     print('1. Check Balance... ')
#     print('2. Deposit.... ')
#     print('3. Withdraw.... ')
#     print('4. Exit.... ')

#     choice = int(input('Pick an option: '))

#     if choice == 1:
#         check_balance()
#     elif choice == 2:
#         deposit()
#     elif choice == 3:               
#         withdraw()
#     elif choice ==  4:
#         print('GoodBye!!!')
#         break
#     else:
#         print('Invalid Option')


# contacts = {}

# def add_contacts():
#     add = input('Enter a name: ')
#     add_no = input('Enter phone number: ')
#     contacts[add] = add_no
#     print(f'{add} added successfully!')

# def search_contacts():
#     search = input('Enter search name: ')

#     if search in contacts:
#         print(f'{search} : {contacts[search]}')
#     else:
#         print('Contact not found!')

# def view_contacts():
#     if len(contacts) == 0:
#         print('No contact saved yet!')
#     else:
#         for name, phone in contacts.items():
#             print(f'{name} : {phone}')

# def delete_contacts():
#     delete = input('Enter a conact to delete: ')
#     if delete in contacts:
#         del contacts[delete]
#         print(f'{delete} successfully removed!')
#     else:
#         print('Contact doesn\'t exist yet!')

# while True:
#     print('----- CONTACT LIST MENU -----')
#     print('1. Add contact ')
#     print('2. Search contact ')
#     print('3. View contact ')
#     print('4. Delete contact ')
#     print('5. Exit ')

#     choice = int(input('Pick an option: '))

#     if choice == 1:
#         add_contacts()
#     elif choice == 2:
#         search_contacts()
#     elif choice == 3:
#         view_contacts()
#     elif choice == 4:
#         delete_contacts()
#     elif choice == 5:
#         print('GoodBye!!!')
#         break
#     else:
#         print('Invalid Option, TRY AGAIN!!!')


# course_registered = []
# course_dropped = []


# def register_course():
#     course = input('Enter a course to register: ')
#     if course in course_registered:
#         print('Course already registered')
#     else:
#         course_registered.append(course)
#         print(f'{course} registered successfully!')

# def drop_course():
#     course = input('Enter the course to drop: ')
#     if course in course_registered:
#         course_registered.remove(course)
#         course_dropped.append(course)
#         print(f'{course} dropped succesfully!')
#     else:
#         print('Course not found among registered courses')

# def view_registered_courses():
#     if len(course_registered) == 0:
#         print('No course registered yet!')
#     else:
#         for course in course_registered:
#             print('-', course)

# def view_dropped_courses():
#     if len(course_dropped) == 0:
#         print('No course dropped yet!')
#     else:
#         for course in course_dropped:
#             print('-', course)

# while  True:
#     print('---- STUDENT COURSE REGISTRATION ----')
#     print('1. Register Course ')
#     print('2. Drop Course ')
#     print('3. View Registered Courses ')
#     print('4. View Dropped Courses ')
#     print('5. Exit ')

#     choice = int(input('Pick an option: '))

#     if choice == 1:
#         register_course()
#     elif choice == 2:
#         drop_course()
#     elif choice == 3:
#         view_registered_courses()
#     elif choice == 4:
#         view_dropped_courses()
#     elif choice == 5:
#         print('Thanks for participating, GoodBye!!! ')
#         break
#     else:
#         print('Enter a valid option')

# def addition(a, b):
#     return a + b

# def substraction(a, b):
#     return a - b

# def multiplication(a, b):
#     return a * b 

# def division(a, b):
#     if b == 0:
#         return 'Cannot divide by zero'
#     else:
#         return a / b

# while True:
#     print('---- SIMPLE CALCULATOR----')
#     num1 = float(input('Enter the first number: '))
#     num2 = float(input('Enter the second number: '))
#     operator = input('Choose an operator to perform(+, -, /, *) or type \'done\' to end program:  ')

#     if operator ==  'done':
#         print('GoodBye!')
#         break

#     else:
#         if operator == '+':
#             result = addition(num1, num2)
#         elif operator == '-':
#             result = substraction(num1, num2)
#         elif operator == '*':
#             result = multiplication(num1, num2)
#         elif operator == '/':
#             result = division(num1, num2)
#         else:
#             print('Inavlid operator')
            
#     print('Result =', result)

# -------- FILE HANDLING (Reading & Writing Files in Python) --------

# with open("student.txt") as student_list:
#     for student in student_list:
#         names = student.split(",")
#         print(names[1])

# ---- MISCELLENEOUS ASPECT OF FUNCTIONS -----

# --------- FUNCTIONS (GENERATORS) -------

# def my_generator():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5

# for numbers in my_generator():
#     print(numbers)

# def numbers(x):
#     count = x
#     while count >= 1:
#         yield count
#         count -= 1

# for num in numbers(10):
#     print(num)

# list_comp = [i * i for i in range(10) if i % 2 == 0]
# print(list_comp)

# gen_comp = sum(x * x for x in range(10) if x % 2 != 0)
# print(gen_comp)
# print(list(gen_comp))

# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
    
# gen = fibonacci()

# for i in range(100):
#     print(next(gen))

# def recicieve_gen():
#     while True:
#         greetings = yield
#         print("Hello", greetings)

# my_gen = recicieve_gen()
# next(my_gen)
# my_gen.send("Emmanuel")
# my_gen.send("David")

# def numbers(x):
#     count = 1
#     while count <= x:
#         yield count
#         count += 1

# for num in numbers(10):
#     print(num)

# def echo_gen():
#     while True:
#         recieved = yield
#         print("Hello", recieved)

# my_gen = echo_gen()
# next(my_gen)
# my_gen.send("Timilleyin")
# my_gen.send("Daniel")

# def total_number():
#     total = 0

#     while True:
#         num = yield
#         total += num
#         print("Total =", total)

# my_gen = total_number()
# next(my_gen)
# my_gen.send(54)
# my_gen.send(88)
# my_gen.send(78)
# my_gen.send(13)
# my_gen.send(102)

