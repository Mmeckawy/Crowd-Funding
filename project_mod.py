import re
import json
from datetime import datetime

projects = {}

def validate_target(target="target"):
    if target.isdigit():
        return True
    else:
        return False

def validate_date(start_date=None, end_date=None):
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

def generate_project_id(projects):
    # Find the maximum ID in the existing projects
    existing_ids = [int(project['id']) for project in projects.values()]
    max_id = max(existing_ids, default=0)
    
    # Increment the maximum ID to generate a new unique ID
    new_id = max_id + 1
    return str(new_id)

def new_project(id, email, title, details, target, start_date, end_date):
    if validate_target(target) is True:
        pass
    else:
        return "Enter digits only"

    if not validate_date(start_date, end_date) == "Valid":
        return "Enter Date Again"
    else:
        project_id = generate_project_id(projects)
        projects[project_id] = {'id': project_id, 'email': email, 'title': title, 'details': details, 'target': target, 'start_date': start_date, 'end_date': end_date}
        save_project(projects)
        print(projects)
        return "Project Created successfully"

"""Files"""
def read_all_projects():
    try:
        with open("projects.json", "r") as fileobject:
            projects = json.load(fileobject)
    except FileNotFoundError:
        projects = {}
    except Exception as e:
        print(e)
        projects = {}
    return projects

def save_all_projects(projects: dict):
    with open("projects.json", 'w') as fileobject:
        json.dump(projects, fileobject, indent=4)

def save_project(projects: dict):
    projects_all = read_all_projects()
    projects_all.update(projects)
    users_saved = save_all_projects(projects_all)
    print(users_saved)
