from data.models.Projects import Projects
from data.models.Employees import Employees

def create_project(name, owner):
    project = Projects()
    project.project_name = name
    project.project_owner = owner

    project.save()

def find_all_projects():
    return Projects.objects()

def delete_project(object_id):
    return Projects.objects(id=object_id).delete()

def add_employee(name, days_worked):
    employee = Employees()
    employee.employee_name = name
    employee.work_days = days_worked

