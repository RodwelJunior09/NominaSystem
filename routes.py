from flask import Flask, render_template, request
import data.services.data_services as srv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("homePage.html")

@app.route('/project_registration', methods=["GET", "POST"]) # Timeout because of a ssl error - maybe a mac issue.
def project_name():
    if request.method == "POST":
        srv.create_project(request.form.get('project-title'), request.form.get('owner-name'))
        print("Project Saved")
    return render_template("project_name.html")

@app.route('/employee_registration', methods=["GET", "POST"])
def employeeRegistration():
    return render_template("employee_register.html")