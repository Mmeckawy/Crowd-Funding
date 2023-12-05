import re

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
        if start_date[6:9] > end_date[6:9]:
            return "Invalid End Date"
        elif start_date[6:9] == end_date[6:9]:
            if start_date[3:4] > end_date[3:4]:
                return "Invalid End Date"
            elif start_date[3:4] == end_date[3:4]:
                if start_date[1:2] > end_date[1:2]:
                    return "Invalid End Date"
                else:
                    return "Valid"
            else:
                return "Valid"
        else:
            return "Valid"

def new_project(title, details, target, start_date, end_date):
    if validate_target(target) == True:
        pass
    else:
        return "Enter digits only"
    
    if validate_date(start_date,end_date) == "Valid":
        pass
    else:
        return "Enter Date Again"
    
    projects[title] = {'title' : title, 'details': details, 'target' : target, 'start_date' : start_date, 'end_date' : end_date}
    print(projects)