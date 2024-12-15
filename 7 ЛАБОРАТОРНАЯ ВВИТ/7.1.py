class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f"Имя: {self.name}, ID: {self.id}"


class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department

    def manage_project(self):
        return f"Менеджер {self.name} управляет проектом в {self.department}."


class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"Технический специалист {self.name} занимается техническим обслуживанием ({self.specialization})."


class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.subordinates = []

    def manage_project(self):
        return f"Технический менеджер {self.name} ведет проект в {self.department}."

    def perform_maintenance(self):
        return f"Технический менеджер {self.name} проводит техническое обслуживание ({self.specialization})."

    def add_employee(self, employee):
        self.subordinates.append(employee)

    def get_team_info(self):
        print(f"Команда {self.name}:")
        for employee in self.subordinates:
            print(employee.get_info())


emp = Employee("Катерина", 777)
print(emp.get_info())

manager = Manager("Архип", 456, "IT")
print(manager.manage_project())

technician = Technician("Тихон", 789, "Нетворк")
print(technician.perform_maintenance())

tech_manager = TechManager("Елисей", 101, "Инженерия", "Программное обеспечение")
print(tech_manager.manage_project())
print(tech_manager.perform_maintenance())

tech_manager.add_employee(emp)
tech_manager.add_employee(technician)
tech_manager.add_employee(manager)
tech_manager.get_team_info()