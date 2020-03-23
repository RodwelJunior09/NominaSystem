import datetime
import mongoengine
from data.models.Employees import Employees

class Projects(mongoengine.Document):
    project_name = mongoengine.StringField(required=True)
    project_owner = mongoengine.StringField(required=True)
    register_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    project_employees = mongoengine.EmbeddedDocumentListField(Employees)