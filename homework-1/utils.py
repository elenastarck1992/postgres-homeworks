import csv
import os.path

path_employees = os.path.join("north_data", "employees_data.csv")
path_customers = os.path.join("north_data", "customers_data.csv")
path_orders = os.path.join("north_data", "orders_data.csv")

def create_employees():
    data = []
    data.clear()
    with open(path_employees, 'r', encoding='utf-8', newline='') as csv_file:
        data_file = csv.reader(csv_file)
        for employee in data_file:
            data.append(employee)
    return data


def create_customers():
    data = []
    data.clear()
    with open(path_customers, 'r', encoding='utf-8', newline='') as csv_file:
        data_file = csv.reader(csv_file)
        for customer in data_file:
            data.append(customer)
    return data


def create_orders():
    data = []
    data.clear()
    with open(path_orders, 'r', encoding='utf-8', newline='') as csv_file:
        data_file = csv.reader(csv_file)
        for customer in data_file:
            data.append(customer)
    return data
