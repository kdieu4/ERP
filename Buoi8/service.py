def add_employee(employees, employee):
    employees.append(employee)

def find_employee(employees, code):
    for employee in employees:
        if employee.code == code:
            return employee
    return None

def update_salary(employees, code, new_salary):
    employee = find_employee(employees, code)
    
    if employee:
        employee.salary = new_salary
        return True
    return False

def delete_employee(employees, code):
    employee = find_employee(employees, code)
    if employee:
        employees.remove(employee)
        return True
    return False
    

def show_employees(employees):
    for employee in employees:
        print(f"Mã nhân viên: {employee.code}")
        print(f"Họ tên: {employee.name}")
        print(f"Mức lương: {employee.salary}")
        print(f"Số ngày công: {employee.days}")
        print(f"Tiền lương: {employee.salary_value()}")
        print("-" * 60)

def filter_working(employees):
    return [employee for employee in employees if employee.days > 0]

def total_salary(employees):
    total = 0
    
    for employee in employees:
        total += employee.salary_value()
        
    return total