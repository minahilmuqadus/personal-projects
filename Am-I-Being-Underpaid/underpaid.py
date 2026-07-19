import time
import sys
import threading
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
    print("             💸 AM I BEING UNDERPAID? 💸")
    print("=======================================================")
    print("Welcome to the world's most unnecessary")
    print("yet strangely satisfying salary tracker.")
    print()
    print("Find out exactly how much money")
    print("you're earning every second.")
    print()
    print("🚽 Featuring the legendary Potty Mode.")
    print("=======================================================")
    input("Press ENTER to begin...")

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
    print(f"Time Tracked  : {time_elapsed} seconds")
    print(f"Total Earned  : {total_earned:.2f} {employee['currency']}")
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
        print("1. View Salary Summary")
        print("2. Start Live Earnings Tracker")
        print("3. Enter Employee Information Again")
        print("4. Exit")
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
            print("\nThank you for using 'Am I Being Underpaid?'")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")

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
        print("\nWelcome Back,", employee["name"] + "!")
        print("====================================")
        print("1. Continue with saved employee")
        print("2. Enter new employee")
        print("====================================")

        choice = get_valid_int("Enter your choice: ")

        if choice == 1:
            run_application(employee)

        elif choice == 2:
            employee = user_info_collection()
            save_employee(employee)
            run_application(employee)

        else:
            print("Invalid choice.")
            return

    else:

     print("No saved employee found.")
     employee = user_info_collection()
     save_employee(employee)
     run_application(employee)

def salary_analysis(employee):
    monthly_salary = employee["monthly_salary"]
    if monthly_salary < 35000:
        print("🔴 Salary Status")
        print("Underpaid")
        print("💡 Advice")
        print("Consider negotiating your salary,")
        print("learning high-income skills,")
        print("or exploring better opportunities.")
    elif monthly_salary >= 35000 and monthly_salary <=75000:
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
        
start_application()