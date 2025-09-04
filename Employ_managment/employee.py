from database import get_connection

class Employee:
    def __init__(self, name, age, department, salary):
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO employees (name, age, department, salary) VALUES (?, ?, ?, ?)",
            (self.name, self.age, self.department, self.salary)
        )
        conn.commit()
        conn.close()
        print(f"Employee {self.name} added successfully...")

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()
        conn.close()
        return rows
