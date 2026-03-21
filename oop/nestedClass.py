class Company:
    
    class Employee:
        def __init__(self, name, post):
            self.name = name
            self.post = post

        def get_details(self):
            return f"{self.name} {self.post}"
    
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, post):
        new_employee = self.Employee(name, post)
        self.employees.append(new_employee)
        pass

    def list_employee(self):
        return [employee.get_details() for employee in self.employees]

company = Company("ABC")

company.add_employee("Harry", "Data Engineer")
company.add_employee("Ron", "Data Analyst")

print(company.list_employee())
