import tkinter as tk
import os
from Persona import Login;
from Persona import RegistrarUsuario;
from Persona import Logout;
import pickle;

'''def show_login():
    login = Login(root)

def show_register():
    registrar = RegistrarUsuario(root)

def show_logout():
    logout = Logout(root)

if __name__ == "__main__":
    root = tk.Tk()

    menu = tk.Menu(root)
    root.config(menu=menu)

    if __name__ == "__main__":
        root = tk.Tk()

        login_menu = tk.Menu(menu)
        menu.add_cascade(label="Login", menu=login_menu)
        login_menu.add_command(label="Login", command=show_login)

        register_menu = tk.Menu(menu)
        menu.add_cascade(label="Register", menu=register_menu)
        register_menu.add_command(label="Register", command=show_register)

        user_menu = tk.Menu(menu)
        menu.add_cascade(label="User", menu=user_menu)
        user_menu.add_command(label="Logout", command=show_logout)

        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    login = Login(root)
    registrar = RegistrarUsuario(root)
    root.mainloop()'''


file_path1 = "C:/Users/benja/OneDrive/Documents/LCIk-2023-1/Paradigmas/FinalPrep/Entrega/Final/users/users.pickle"

# Print the content of users.pickle file
with open(file_path1, "rb") as file:
    content1 = pickle.load(file)
    print(content1)

file_path = "C:/Users/benja/OneDrive/Documents/LCIk-2023-1/Paradigmas/FinalPrep/Entrega/Final/users/usernames.pickle"

# Print the content of usernames.pickle file
with open(file_path, "rb") as file:
    content2 = pickle.load(file)
    print(content2)

