import re

users = {}

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
        users[email] = { 'first_name': first_name, 'last_name': last_name, 'password': password, 'phone': phone}
        print(users)
        return "Registered Successfully"

def authenticate_user(email, password):
    user = users.get(email)
    print("Logged in")
    return user['password'] == password