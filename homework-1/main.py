"""Скрипт для заполнения данными таблиц в БД Postgres."""
import os.path
import psycopg2

from utils import create_customers, create_employees, create_orders


def create_table():
    conn = psycopg2.connect(host="localhost", port="5433", database="north", user="postgres", password="12345")
    table_employees = create_employees()
    table_customers = create_customers()
    table_orders = create_orders()
    try:
        with conn:
            for employee in table_employees:
                if employee != table_employees[0]:
                    with conn.cursor() as cur:
                        cur.execute(
                            "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (employee_id) DO NOTHING",
                            (employee))
            for customer in table_customers:
                if customer != table_customers[0]:
                    with conn.cursor() as cur:
                        cur.execute("INSERT INTO customers VALUES (%s, %s, %s) ON CONFLICT (customer_id) DO NOTHING",
                                    (customer))
            for order in table_orders:
                if order != table_orders[0]:
                    with conn.cursor() as cur:
                        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (order))
    finally:
        conn.close()


if __name__ == '__main__':
    create_table()
