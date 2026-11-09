# csv_practice.py
#Author: Roman Medina
#Module 12 Lab: Read a Sales CSV, Write a Cleaned up report

import csv
from datetime import datetime

SALES_FILE = "sales.csv"
CLEANED_FILE = "cleaned_sales.csv"
LOG_FILE = "run_log.txt"

print("--Exercise 1--")
with open(SALES_FILE, "r") as f:
    print(f"Opened {SALES_FILE}.")

print("--Exercise 2--")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)