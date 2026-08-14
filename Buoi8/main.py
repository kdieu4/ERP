from employee import Employee
import service
import os

def show_menu():
    print("\n==== QUẢN LÝ NHÂN VIÊN ====")
    print("1. Hiển thị danh sách")
    print("2. Thêm nhân viên")
    print("3. Tìm nhân viên")
    print("4. Cập nhật mức lương")
    print("5. Xóa nhân viên")
    print("6. Lọc nhân viên đang làm việc")
    print("7. Tính tổng tiền lương")
    print("0. Thoát")

def clear_screeen():
    os.system("cls" if os.name == "nt" else "clear")
    
employees = [
    Employee("NV01", "Nguyễn Văn An", 500000, 26),
    Employee("NV02", "Trần Thị Bình", 450000, 24),
    Employee("NV03", "Lê Văn Cường", 600000, 22),
    Employee("NV04", "Phạm Thị Dung", 550000, 0),
    Employee("NV05", "Hoàng Xuân Thiên", 480000, 25),
]

def handle_show_employees():
    print("==== DANH SÁCH NHÂN VIÊN ====")
    service.show_employees(employees)

def handle_add_employee():
    print("==== THÊM NHÂN VIÊN ====")
    
    code = input("Nhập mã nhân viên: ")
    name = input("Nhập họ tên: ")
    salary = float(input("Nhập mức lương: "))
    days = int(input("Nhập số ngày công: "))
    
    employee = Employee(code, name, salary, days)
    service.add_employee(employees, employee)
    
    print("\nThêm nhân viên thành công")

def handle_find_employee():
    print("==== TÌM NHÂN VIÊN ====")
    code = input("Nhập mã nhân viên: ")
    employee = service.find_employee(employees, code)
    
    if employee:
        print("\nThông tin nhân viên: ")
        print(f"Mã nhân viên: {employee.code}")
        print(f"Họ tên: {employee.name}")
        print(f"Mức lương: {employee.salary}")
        print(f"Số ngày công: {employee.days}")
        print(f"Tiền lương: {employee.salary_value()}")
    else:
        print("Không tìm thấy nhân viên!")
    
def handle_update_salary():
    print("==== CẬP NHẬT MỨC LƯƠNG ====")
    
    code = input("Nhập mã nhân viên: ")
    new_salary = float(input("Nhập mức lương mới: "))
    
    if service.update_salary(employees, code, new_salary):
        print("\nCập nhật thành công!")
    else:
        print("\nKhông tìm thấy nhân viên!")
    
def handle_delete_employee():
    print("==== XÓA NHÂN VIÊN ====")
    
    code = input("Nhập mã nhân viên cần xóa: ")
    if (service.delete_employee(code)):
        print("\nXóa thành công")
    else:
        print("\nKhông tìm thấy nhân viên")
        
def handle_filter_working():
    print("==== NHÂN VIÊN ĐANG LÀM VIỆC ====")
    
    working = service.filter_working(employees)
    service.show_employees(working)
    
def handle_total_salary():
    print("==== TỔNG TIỀN LƯƠNG ====")
    
    total = service.total_salary(employees)
    print(f"Tổng tiền lương: {total}")
    

def main():
    while True:
        show_menu()
        choice = input("Nhập lựa chọn: ")
        clear_screeen()
        
        if choice == "1":
            handle_show_employees()
        elif choice == "2":
            handle_add_employee() 
        elif choice == "3":
            handle_find_employee()
        elif choice == "4":
            handle_update_salary()
        elif choice == "5":
            handle_delete_employee()
        elif choice == "6":
            handle_filter_working()
        elif choice == "7":
            handle_total_salary()
        elif choice == "0":
            print("Kết thúc chương trình!")
            break    
        else:
            print("Lựa chọn không hợp lệ!")
        
        input("\nNhấn Enter để quay lại menu...")
              
if __name__ == "__main__":
    main()