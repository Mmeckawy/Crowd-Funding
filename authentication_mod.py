import re
import json

users = {}
email_unique =""

def validate_name(first_name="name", last_name="name"):

     if not first_name.isalpha() or not last_name.isalpha():
          return "Invalid names"
     else:
          pass
          

def validate_email(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(pattern, email)

def validate_phone(phone):
       pattern = r'^\+20\d{10}$' 
       return re.match(pattern, phone)

def register_user(first_name, last_name, email, password, phone):
    if validate_name(first_name, last_name) == "Invalid names":
        return "Invalid names"
         
    if not validate_email(email):
        return "Invalid email"
    
    if not validate_phone(phone):
        return "Invalid phone number"
    else:
        users[email] = {'first_name': first_name, 'last_name': last_name, 'password': password, 'phone': phone}
        save_user(users)
        print(users)
        return "Registered Successfully"

def authenticate_user(email, password):
    users = read_all_users()

    for user_dict in users:
        user_email = next(iter(user_dict.keys()), None)
        user_data = user_dict.get(user_email, {})
        
        if user_email == email and user_data.get('password') == password:
            global email_unique
            email_unique = email
            print("Logged in")
            return True

    print("Invalid email or password")
    return False


    
"""Files"""
def read_all_users():
    try:
        fileobject = open("users.json", "r")
    except Exception as e:
        print(e)
        return False
    else:
        user = fileobject.read()
        # print(data)
        if user:
            user = json.loads(user) 
        else:
            user = []
        fileobject.close()
        return user

def save_all_users(users : list):
    users = json.dumps(users, indent=4)
    try:
        fileobject = open("users.json", 'w')
    except Exception as e:
        print(e)
        return  False
    else:
        fileobject.write(users)
        return  True

def save_user(users :dict ):
    users_all = read_all_users()
    users_all.append(users)
    users_saved = save_all_users(users_all)
    print(users_saved)