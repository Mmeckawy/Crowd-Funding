import re
import json
from datetime import datetime

projects = {}

def validate_target(target="target"):
    if target.isdigit():
        return True
    else:
        return False
    
def validate_date(start_date = None, end_date = None):
   pattern = r'\d{2}-\d{2}-\d{4}'

   if not re.match(pattern, start_date) or not re.match(pattern, end_date):
       return "Invalid Date"
   else:
       try:
           start_date = datetime.strptime(start_date, '%d-%m-%Y')
           end_date = datetime.strptime(end_date, '%d-%m-%Y')
       except ValueError:
           return "Invalid Date"

       if start_date > end_date:
           return "Invalid End Date"
       else:
           return "Valid"

def new_project(id, email, title, details, target, start_date, end_date):
    if validate_target(target) == True:
        pass
    else:
        return "Enter digits only"
    
    if not validate_date(start_date,end_date) == "Valid":
        return "Enter Date Again"
    else:
        projects[id] = {'id' : id, 'email' : email, 'title' : title, 'details': details, 'target' : target, 'start_date' : start_date, 'end_date' : end_date}
        print(projects)
        return "Project Created successfully"
    
