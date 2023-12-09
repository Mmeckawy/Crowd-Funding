import tkinter as tk
from tkinter import messagebox,ttk
import authentication_mod as auth
import project_mod as proj
import json
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import base64
from tkinter.filedialog import askopenfilename


def register():
   first_name = first_name_entry.get()
   last_name = last_name_entry.get()
   email = email_entry.get()
   password = password_entry.get()
   confirm_password = confirm_password_entry.get()
   phone = phone_entry.get()

   if password != confirm_password:
       messagebox.showerror("Registeration", "Passwords don't match")
       return

   result = auth.register_user(first_name, last_name, email, password, phone)
   messagebox.showinfo("Result", result)

def projects():
   project_gui = tk.Toplevel()
   project_gui.title("Project")
   project_gui.geometry("500x400")
   project_gui['background']='#b5a8fb'
   
   title_label = tk.Label(project_gui, text = "Title", background='#b5a8fb').place(x = 50,y = 30)
   title_entry = tk.Entry(project_gui)
   title_entry.place(x = 180, y = 30)

   details_label = tk.Label(project_gui, text = "Details", background='#b5a8fb').place(x = 50,y = 60)
   details_entry = tk.Entry(project_gui)
   details_entry.place(x = 180, y = 60)

   target_label = tk.Label(project_gui, text = "Target", background='#b5a8fb').place(x = 50,y = 90)
   target_entry = tk.Entry(project_gui)
   target_entry.place(x = 180, y = 90)

   start_date_label = tk.Label(project_gui, text = "Start Date", background='#b5a8fb').place(x = 50,y = 120)
   start_date_entry = tk.Entry(project_gui)
   start_date_entry.place(x = 180, y = 120)

   end_date_label = tk.Label(project_gui, text = "End Date", background='#b5a8fb').place(x = 50,y = 150)
   end_date_entry = tk.Entry(project_gui)
   end_date_entry.place(x = 180, y = 150)

   project_listbox = tk.Listbox(project_gui)
   project_listbox.place(x = 400, y = 400)

    # Create a Treeview widget
   tree = ttk.Treeview(project_gui)

   # Define the columns
   tree["columns"]=("one","two","three","four","five","six")
   tree.column("#0", width=100, minwidth=25)
   tree.column("one", width=100, minwidth=25)
   tree.column("two", width=100, minwidth=25)
   tree.column("three", width=100, minwidth=25)
   tree.column("four", width=100, minwidth=25)
   tree.column("five", width=100, minwidth=25)
   tree.column("six", width=100, minwidth=25)

   # Define the headings
   tree.heading("#0",text="Project ID",anchor=tk.W)
   tree.heading("one", text="email",anchor=tk.W)
   tree.heading("two", text="Title",anchor=tk.W)
   tree.heading("three", text="Details",anchor=tk.W)
   tree.heading("four", text="Target",anchor=tk.W)
   tree.heading("five", text="start_date",anchor=tk.W)
   tree.heading("six", text="end_date",anchor=tk.W)


   for project_id in proj.projects:
      project_listbox.insert(tk.END, project_id)

   def create():
      title = title_entry.get()
      details = details_entry.get()
      target = target_entry.get()
      start_date = start_date_entry.get()
      end_date = end_date_entry.get()


      result = proj.new_project(id,auth.email_unique ,title, details, target, start_date, end_date)
      messagebox.showinfo("Result", result)

   def view():
      tree.place(x=320, y=50)
      # Clear the Treeview
      for item in tree.get_children():
        tree.delete(item)

       # Insert the data from the file
      projects_data = load_projects_from_file()
      for project_id, project_details in projects_data.items():
        tree.insert("", tk.END, text=project_id, values=(
            project_details['email'], project_details['title'],
            project_details['details'], project_details['target'],
            project_details['start_date'], project_details['end_date']
        ))

   def update():
      selected_item = tree.selection()[0]
      project_id = tree.item(selected_item, 'text')

      title = title_entry.get()
      details = details_entry.get()
      target = target_entry.get()
      start_date = start_date_entry.get()
      end_date = end_date_entry.get()

      tree.item(selected_item, values=(auth.email_unique, title, details, target, start_date, end_date))

      # Update the project in the file
      projects_data = load_projects_from_file()
      projects_data[project_id].update({
      'id': project_id,
      'email': auth.email_unique,
      'title': title,
      'details': details,
      'target': target,
      'start_date': start_date,
      'end_date': end_date
    })
      save_projects_to_file(projects_data)

   def delete():
    if tree.selection():
        selected_item = tree.selection()[0]
        project_id = tree.item(selected_item, 'text')

        # Clear the Treeview
        for item in tree.get_children():
            tree.delete(item)

        # Delete the project from the file
        projects_data = load_projects_from_file()
        del projects_data[project_id]
        save_projects_to_file(projects_data)


   create_button = tk.Button(project_gui, text="Create", command=create)
   create_button.place(x = 70, y = 250)

   update_button = tk.Button(project_gui, text="Update", command=update)
   update_button.place(x = 150, y = 250)

   view_button = tk.Button(project_gui, text="View", command=view)
   view_button.place(x = 220, y = 250)

   delete_button = tk.Button(project_gui, text="Delete", command=delete)
   delete_button.place(x = 270, y = 250)

   project_gui.mainloop()

def login():
   login_gui = tk.Toplevel()
   login_gui.title("Log in")
   login_gui.geometry("500x400")
   login_gui['background']='#b5a8fb'
   email_login = tk.Label(login_gui, text = "Email", background='#b5a8fb').place(x = 150,y = 100)
   email_entry2 = tk.Entry(login_gui)
   email_entry2.place(x = 280, y = 100)
   
   password2 = tk.Label(login_gui, text = "Password", background='#b5a8fb').place(x = 150,y = 140)  
   password_entry2 = tk.Entry(login_gui, show='*')
   password_entry2.place(x = 280, y = 140)

   def submit():
      email2 = email_entry2.get()
      password_login = password_entry2.get()

      if auth.authenticate_user(email2, password_login):
        messagebox.showinfo("Log in", "Logged in successfully")
        projects()
      else:
       messagebox.showerror("Log in", "Failed to login")

   submit_button = tk.Button(login_gui, text="Log in", command=submit)
   submit_button.place(x = 205, y = 250)
   login_gui.mainloop()

def load_projects_from_file():
    try:
        with open("projects.json", "r") as file:
            projects_data = json.load(file)
        return projects_data
    except FileNotFoundError:
        return {}

def save_projects_to_file(projects_data):
    with open("projects.json", "w") as file:
        json.dump(projects_data, file)

def encrypt():

    try:
        file_path = askopenfilename(filetypes=[('Text Files', '*txt')])
        with open(file_path, 'rb') as fileobject:
            data = fileobject.read()

    except Exception as e:
        return False
    else:
        salt = os.urandom(16)
        key = b'my_secret_key'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            iterations=100000,
            salt=salt,
            length=32,  # Set key length to 32 bytes (256 bits)
            backend=default_backend()
        )
        print(kdf)

        key = base64.urlsafe_b64encode(kdf.derive(key))

        cipher = Cipher(algorithms.AES(key[:32]), modes.CFB8(salt), backend=default_backend()) 
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(data) + encryptor.finalize()
        print(encrypted_data)

        with open(file_path + '.enc', 'wb') as encrypted_file:
            encrypted_file.write(salt + encrypted_data)

# GUI Setup
gui = tk.Tk()
gui.title("Crowd-Funding")
gui.geometry("500x400")
gui['background']='#b5a8fb'

first_name = tk.Label(gui, text = "First Name", background='#b5a8fb').place(x = 150,y = 20)  
first_name_entry = tk.Entry(gui)

last_name = tk.Label(gui, text = "Last Name", background='#b5a8fb').place(x = 150,y = 50)  
last_name_entry = tk.Entry(gui)

email = tk.Label(gui, text = "Email", background='#b5a8fb').place(x = 150,y = 80)  
email_entry = tk.Entry(gui)

phone = tk.Label(gui, text = "Phone", background='#b5a8fb').place(x = 150,y = 110)  
phone_entry = tk.Entry(gui)

password = tk.Label(gui, text = "Password", background='#b5a8fb').place(x = 150,y = 140)  
password_entry = tk.Entry(gui, show='*')

confirm_password = tk.Label(gui, text = "Confirm Password", background='#b5a8fb').place(x = 150,y = 170)  
confirm_password_entry = tk.Entry(gui, show='*')


register_button = tk.Button(gui, text="Register", command=register)
login_button = tk.Button(gui, text="Login", command=login)
encrypt_button = tk.Button(gui, text="Encrypt File", command=encrypt)
result_label = tk.Label(gui, text="",background='#b5a8fb')

first_name_entry.place(x = 280, y = 20)
last_name_entry.place(x = 280, y = 50)
email_entry.place(x = 280, y = 80)
phone_entry.place(x = 280, y = 110)
password_entry.place(x = 280, y = 140)
confirm_password_entry.place(x = 280, y = 170)
register_button.place(x = 205, y = 250)
login_button.place(x = 210, y = 280)
encrypt_button.place(x = 210, y = 310)
result_label.place(x = 170, y = 320)

gui.mainloop()