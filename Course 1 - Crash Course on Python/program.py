import hr
import disgruntled

salary_employee = hr.SalaryEmployee(1, "John Smith", 1500)
hourly_employee = hr.HourlyEmployee(2, "Harmonie Grenger", 40, 15)
commission_employee = hr.CommissionEmployee(3, "Harry Potter", 1000, 250)
disgruntled_employee = disgruntled.DisgruntledEmployee(4, "Anonymous")
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll([
   salary_employee,
   hourly_employee,
   commission_employee,
   disgruntled_employee
])

# employee = hr.Employee(4, "Habib")
# print(employee.name)