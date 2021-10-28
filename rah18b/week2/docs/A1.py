#!/usr/bin/env/python3

#Program Requirements
#Author: Rachel Hester
#Class: LIS4905: Enterprise Application Solutions
#Semester: Summer 2021

print("Tip Calculator")

print("\n Program Requirements:\n1. Must use float data type for user input (except, \"Party Number\").\n2. Must round calculations to two decimal places.\n3. Must format currency with dollar sign, and two decimal places")

#User Input

print("\nUser Input:")
meal_cost = float(input("Cost of meal:"))
tax_percent = float(input("Tax percent: "))
tip_percent = float(input("Tip percent: "))
people_num = int(float(input("Party number: ")))

#calculating tax, tip and total amounts:
tax_amount = round(meal_cost * (tax_percent/100), 2)
due_amount = round(meal_cost + tax_amount, 2)
tip_amount = round((due_amount) * (tip_percent / 100), 2)

#percentage of cost and tax
total = round(meal_cost * (tax_percent / 100), 2)
split = round(total / people_num, 2)

# display results w/proper formatting from video
print("\nProgram Output:")
print("Subtotal:\t", "${0:,.2f}".format(meal_cost)) 
print("Tax:\t\t", "${0:,.2f}".format(tax_amount))
print("Amount due:\t", "${0:,.2f}".format(due_amount))
print("Gratuity:\t", "${0:,.2f}".format(tip_amount))
print("Split " + "(" + str(people_num) + "):\t", "${0:,.2f}".format(split))
