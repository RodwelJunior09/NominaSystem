import datetime
import mongoengine

class Employees(mongoengine.EmbeddedDocument):
    employee_name = mongoengine.StringField(required=True) 
    work_days = mongoengine.ListField(field=mongoengine.StringField(), required=True, max_length=7)
    register_date = mongoengine.DateTimeField(default=datetime.datetime.now)