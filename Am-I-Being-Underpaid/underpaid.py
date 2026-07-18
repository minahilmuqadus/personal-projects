import time
import sys
import threading
import os

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
        final_report(employee, time_elapsed, total_earned)

def final_report(employee, time_elapsed, total_earned):
    print("====================================")
    print("        FINAL REPORT")
    print("====================================")
    print(f"Name          : {employee['name']}")
    print(f"Company       : {employee['company_name']}")
    print(f"Currency      : {employee['currency']}")
    print("------------------------------------")
    print(f"Time Tracked  : {time_elapsed} seconds")
    print(f"Total Earned  : {total_earned:.2f} {employee['currency']}")
    print("====================================")

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
            earnings = calculate_earnings(employee)
            summary(employee, earnings)

        elif user_choice == 4:
            print("\nThank you for using 'Am I Being Underpaid?'")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")





welcome()
employee = user_info_collection()
earnings = calculate_earnings(employee)
summary(employee, earnings)
live_tracking(employee, earnings)
main_menu(employee , earnings)