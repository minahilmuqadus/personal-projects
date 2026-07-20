import time
import os
import json


TEA_PRICE = 50
BURGER_PRICE = 500
BUS_TICKET_PRICE = 80
PIZZA_SLICE_PRICE = 250

def get_valid_float(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_valid_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def welcome():
    print("=======================================================")
    print("       💸 AM I BEING UNDERPAID? 💸                     ")  
    print("=======================================================")
    print()
    print("Welcome to the world's most unnecessary")
    print("yet strangely satisfying salary tracker.")
    print()
    print("Find out exactly how much money")
    print("you're earning every second.")
    print()
    print("🚽 Featuring the legendary Potty Mode.")
    print("🌟 Chase your dream with Dream Progress.")
    print()
    print("=======================================================")
    print("Press ENTER to begin...")



def user_info_collection():
    name = input("Enter Name: ")
    company_name = input("Enter your Company Name: ")
    monthly_salary = get_valid_float("Enter your monthly salary: ")
    currency = input("Enter your currency: ")
    working_hours_per_week = get_valid_int("Enter your working hours per week: ")

    employee = {
        "name": name,
        "company_name": company_name,
        "monthly_salary": monthly_salary,
        "currency": currency,
        "working_hours_per_week": working_hours_per_week,
    }
    return employee

def calculate_earnings(employee):
    monthly_salary = employee["monthly_salary"]
    working_hours_per_week = employee["working_hours_per_week"]

    total_working_hours_per_month = working_hours_per_week * 4
    salary_per_hour = monthly_salary / total_working_hours_per_month
    salary_per_minute = salary_per_hour / 60
    salary_per_second = salary_per_minute / 60

    earnings = {
        "salary_per_hour": salary_per_hour,
        "salary_per_minute": salary_per_minute,
        "salary_per_second": salary_per_second,
    }
    return earnings

def summary(employee, earnings):
    print("====================================")
    print("        EMPLOYEE SUMMARY")
    print("====================================")
    print(f"Name               : {employee['name']}")
    print(f"Company Name       : {employee['company_name']}")
    print(f"Monthly Salary     : {employee['monthly_salary']} {employee['currency']}")
    print("-------------------------------------")
    print(f"Salary Per Hour    : {earnings['salary_per_hour']:.2f} {employee['currency']}")
    print(f"Salary Per Minute  : {earnings['salary_per_minute']:.2f} {employee['currency']}")
    print(f"Salary Per Second  : {earnings['salary_per_second']:.2f} {employee['currency']}")
    print("====================================")

def live_tracking(employee, earnings):
    salary_per_second = earnings["salary_per_second"]
    currency = employee["currency"]
    time_elapsed = 0
    total_earned = 0
    try:
        while True:
            time.sleep(1)
            time_elapsed += 1
            total_earned += salary_per_second
            os.system("cls")  # use "clear" if on macOS/Linux
            print("====================================")
            print("LIVE TRACKER")
            print("====================================")
            print(f"Time Elapsed : {time_elapsed}")
            print(f"Money Earned : {total_earned:.2f} {currency}")
            print("====================================")
    except KeyboardInterrupt:
     final_report(employee, earnings, time_elapsed, total_earned)

def potty_mode(employee, earnings):
    print("====================================")
    print("        🚽 POTTY MODE")
    print("====================================")
    print("Go do your business...")
    print("Timer Started!")
    print()

    start_time = time.time()

    input("Press ENTER when you're back...")

    end_time = time.time()

    time_elapsed = int(end_time - start_time)

    salary_per_second = earnings["salary_per_second"]
    total_earned = salary_per_second * time_elapsed

    potty_report(employee, earnings, time_elapsed, total_earned)
    

def potty_report(employee, earnings, time_elapsed, total_earned):
    print("====================================")
    print("        🚽 POTTY REPORT")
    print("====================================")

    formatted_time = time.strftime("%H:%M:%S", time.gmtime(time_elapsed))

    print(f"Bathroom Time : {formatted_time}")
    print(f"Money Earned  : {total_earned:.2f} {employee['currency']}")

    print("====================================")

    
    print("🚽 Bathroom Rating")
    print("------------------------------------")

    if time_elapsed < 120:
     print("⚡ Speed Runner")
     print("You broke the land speed record.")

    elif time_elapsed < 300:
     print("⭐ Perfect Balance")
     print("Quick, efficient, and productive.")

    elif time_elapsed < 600:
     print("😌 Relaxed Visit")
     print("Hope you solved all of life's problems.")

    elif time_elapsed < 1200:
     print("📱 Scrolling Detected")
     print("Let's be honest... you were scrolling.")

    else:
     print("🏠 New Address Registered")
     print("Should we update your mailing address?")

print("====================================")

def final_report(employee, earnings , time_elapsed, total_earned  ):
    print("====================================")
    print("        📊 SESSION REPORT")
    print("====================================")

    print("👤 Employee Information")
    print("-------------------------------------")
    print(f"Name          : {employee['name']}")
    print(f"Company       : {employee['company_name']}")
    print(f"Currency      : {employee['currency']}")

    #print("💰 Session Statistics")
    #print("------------------------------------")
    
    salary_per_hour = earnings["salary_per_hour"]
    salary_per_minute = earnings["salary_per_minute"]
    salary_per_second = earnings["salary_per_second"]

    projected_1_hour = salary_per_hour
    projected_8_hours = salary_per_hour * 8
    projected_monthly = employee["monthly_salary"]

    print("💰 Session Statistics")
    print("------------------------------------")

    formatted_time = time.strftime("%H:%M:%S", time.gmtime(time_elapsed))

    print(f"Time Tracked  : {formatted_time}")
    print(f"Total Earned  : {total_earned:.2f} {employee['currency']}")
    print(f"Per Hour      : {salary_per_hour:.2f} {employee['currency']}")
    print(f"Per Minute    : {salary_per_minute:.2f} {employee['currency']}")
    print(f"Per Second    : {salary_per_second:.2f} {employee['currency']}")
    
    
    print("📈 Projections")
    print("-------------------------------------")
    print(f"1 Hour        : {projected_1_hour:.2f} {employee['currency']}")
    print(f"8 Hours       : {projected_8_hours:.2f} {employee['currency']}")
    print(f"Monthly Salary: {projected_monthly:.2f} {employee['currency']}")

    print("====================================")
    print("Thanks for using the tracker!")
    print("====================================")

    print("🎯 Fun Facts")
    print("------------------------------------")
    cups_of_tea   = int(total_earned / TEA_PRICE )
    print(f"☕ Cups of Tea    : {cups_of_tea}")
    burgers = int(total_earned / BURGER_PRICE)
    print(f"🍔 Burgers          : {burgers}")
    bus_tickets = int(total_earned / BUS_TICKET_PRICE)
    print(f"🚌 Bus Tickets      : {bus_tickets}")
    pizza_slices = int(total_earned / PIZZA_SLICE_PRICE)
    print(f"🍕 Pizza Slices      : {pizza_slices}")
    print("------------------------------------")

def main_menu( employee , earnings):
    while True:
        print("==============================================")
        print("                 MAIN MENU")
        print("==============================================")
        print("1. 📊 Salary Summary")
        print("2. 💸 Live Earnings Tracker")
        print("3. 👤 Change Employee")
        print("4. 🚽 Potty Mode")
        print("5. 🌟 My Dream Progress")
        print("6. 🚪 Exit")
        print("")
        print("==============================================")

        
        user_choice = get_valid_int("Enter your choice: ")
        

        if user_choice == 1:
            summary(employee, earnings)

        elif user_choice == 2:
            live_tracking(employee, earnings)

        elif user_choice == 3:
            employee = user_info_collection()
            save_employee(employee)
            run_application(employee)
            break

        elif user_choice == 4:
            potty_mode(employee, earnings)

        

        elif user_choice == 5:
         my_dream_progress(employee)

        elif user_choice == 6 :
            
            print("\nEvery second you work is buying something.")
            print("Make sure it's buying the life you want.")
            print("Goodbye!")
            break
        else:
            print("Invalid")

def save_employee(employee):
    with open ("employee.json" , "w" ) as file :
        json.dump(employee , file , indent=4)


def load_employee():
    try:
        with open("employee.json", "r") as file:
            employee = json.load(file)
            return employee

    except FileNotFoundError:
        return None
    
def run_application(employee):
    earnings = calculate_earnings(employee)

    salary_analysis(employee)


    main_menu(employee, earnings)


def start_application():
    welcome()

    employee = load_employee()

    if employee is not None:
     print("====================================")
     print(f"👋 Welcome Back, {employee['name']}!")
     print("------------------------------------")
     print(f"🏢 Company : {employee['company_name']}")
     print(f"💰 Salary  : {employee['monthly_salary']:.2f} {employee['currency']}")
     print("====================================")

     print("1. Continue with saved employee")
     print("2. Enter employee information again")
     print("3. Exit")
     print("------------------------------------")

     choice = get_valid_int("Enter your choice: ")

    if choice == 1:
        run_application(employee)

    elif choice == 2:
        employee = user_info_collection()
        save_employee(employee)
        run_application(employee)

    elif choice == 3:
        print("\nGoodbye!")
        return

    else:
        print("\n❌ Invalid choice.")
        return

def salary_analysis(employee):
    monthly_salary = employee["monthly_salary"]
    if monthly_salary < 35000:
        print("🔴 Salary Status")
        print("Underpaid")
        print("💡 Advice")
        print("Consider negotiating your salary,")
        print("learning high-income skills,")
        print("or exploring better opportunities.")
    elif monthly_salary <= 75000:
        print("🟡 Salary Status: ")
        print("Fair Salary")
        print("💡 Advice")
        print("You're doing okay.")
        print("Keep improving your skills")
        print("to move into a higher salary bracket.")
    else:
        print("🟢 Salary Status")
        print("Well Paid")
        print("💡 Advice")
        print("Great job!")
        print("Keep learning and investing in yourself.")

def save_dream(dream):
    with open("dream.json", "w") as file:
        json.dump(dream, file, indent=4)


def load_dream():
    try:
        with open("dream.json", "r") as file:
            dream = json.load(file)
            return dream
    except FileNotFoundError:
        return None


def dream_progress(employee, dream):
    dream_price = dream["dream_price"]
    monthly_salary = employee["monthly_salary"]

    # -------------------------------
    # Dream ETA Calculation
    # -------------------------------

    months = dream_price / monthly_salary

    whole_months = int(months)

    decimal_part = months - whole_months

    days = round(decimal_part * 30)

    # -------------------------------
    # Progress Calculation
    # -------------------------------

    progress = (monthly_salary / dream_price) * 100

    if progress > 100:
        progress = 100

    filled_blocks = int(progress / 5)   # 20 blocks total
    empty_blocks = 20 - filled_blocks

    progress_bar = ("█" * filled_blocks) + ("░" * empty_blocks)

    # -------------------------------
    # Dream Report
    # -------------------------------

    print("------------------------------------")
    print(f"🎯 Dream            : {dream['dream_name']}")
    print(f"💰 Dream Price      : {dream_price:.2f} {employee['currency']}")
    print(f"💵 Monthly Salary   : {monthly_salary:.2f} {employee['currency']}")

    if whole_months == 0:
        print(f"⏳ Estimated Time   : {days} Days")
    elif days == 0:
        if whole_months == 1:
            print("⏳ Estimated Time   : 1 Month")
        else:
            print(f"⏳ Estimated Time   : {whole_months} Months")
    else:
        if whole_months == 1:
            print(f"⏳ Estimated Time   : 1 Month {days} Days")
        else:
            print(f"⏳ Estimated Time   : {whole_months} Months {days} Days")

    print("------------------------------------")
    print("🌟 Dream Progress")
    print(f"{progress_bar} {progress:.0f}%")
    print("------------------------------------")

    # -------------------------------
    # Motivation
    # -------------------------------

    if progress >= 100:
        print("🎉 You can buy your dream now!")
    elif progress >= 75:
        print("🔥 You're almost there!")
    elif progress >= 50:
        print("💪 Keep grinding. You're halfway there!")
    elif progress >= 25:
        print("🚀 Great start. Keep saving!")
    else:
        print("🌱 Every journey begins with one step.")

    print("------------------------------------")

def my_dream_progress(employee):
    print("====================================")
    print("      🌟 MY DREAM PROGRESS")
    print("====================================")

    dream = load_dream()

    if dream is None:
        print("No dream found.")
        print("Let's set one!\n")

        dream_name = input("Enter your dream: ")
        dream_price = get_valid_float("Enter your dream price: ")

        dream = {
            "dream_name": dream_name,
            "dream_price": dream_price
        }

        save_dream(dream)

        print("\n✅ Dream saved successfully!\n")

    dream_progress(employee, dream)

start_application()