from flask import Flask, render_template, request, redirect
import data.services.data_services as srv

app = Flask(__name__, template_folder="templates")

@app.route('/', methods=["GET"])
def homePage():
    collection_projects = srv.find_all_projects()
    return render_template("homePage.html", title="HomePage", projects=collection_projects)

@app.route('/delete/<object_id>', methods=["GET", "POST"])
def deleteProject(object_id):
    if request.method == "POST":
        srv.delete_project(object_id)
        print("Project Deleted")
        return redirect('/')
    else:
        return render_template("DeleteProject.html")

@app.route('/project_registration', methods=["GET", "POST"]) # Timeout because of a ssl error - maybe a mac issue.
def projectRegistration():
    if request.method == "POST":
        srv.create_project(request.form.get('project-title'), request.form.get('owner-name'))
        print("Project Saved")
        return redirect("/")
    return render_template("ProjectRegistration.html")

@app.route('/employee_registration', methods=["GET", "POST"])
def employeeRegistration():
    return render_template("EmployeeRegistration.html")