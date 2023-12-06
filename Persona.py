import tkinter as tk
from tkinter import messagebox
import pickle
import hashlib
import os
import binascii
import os


class Persona:
    def __init__(self, codigo_persona, usuario, nombre, apellido, tipo_documento, documento, contraseña, correo, num_telefono):
        self.codigo_persona = codigo_persona
        self.usuario = usuario
        self.nombre = nombre
        self.apellido = apellido
        self.tipo_documento = tipo_documento
        self.documento = documento
        self.contraseña = self._hash_password(contraseña)
        self.correo = correo
        self.num_telefono = num_telefono
        self.documento_verificado = False
        self.contacto_verificado = False
        self.es_admin = False
        self.es_host = False
        self.historial_alquileres = []

    def _hash_password(self, password):
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        hashed_password = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
        hashed_password = binascii.hexlify(hashed_password)
        return (salt + hashed_password).decode('ascii')

    def verify_password(self, password):
        stored_password = self.contraseña[:64]
        salt = self.contraseña[64:]
        hashed_password = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt.encode('ascii'), 100000)
        hashed_password = binascii.hexlify(hashed_password).decode('ascii')
        return hashed_password == stored_password
    
    def check_and_create_files(self):
        users_file = 'C:/Users/benja/OneDrive/Documents/LCIk-2023-1/Paradigmas/FinalPrep/Entrega/Final/Users/users.pickle'
        usernames_file = 'C:/Users/benja/OneDrive/Documents/LCIk-2023-1/Paradigmas/FinalPrep/Entrega/Final/Users/usernames.pickle'

        if not os.path.exists(users_file):
            with open(users_file, 'wb') as f:
                pickle.dump({}, f)

        if not os.path.exists(usernames_file):
            with open(usernames_file, 'wb') as f:
                pickle.dump({}, f)
                
    def __str__(self):
        return f'Persona({self.codigo_persona}, {self.usuario}, {self.nombre}, {self.apellido}, {self.tipo_documento}, {self.documento}, {self.correo}, {self.num_telefono})'

class Login:
    '''def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("300x200")

        self.label_username = tk.Label(self.master, text="Username")
        self.label_password = tk.Label(self.master, text="Password")

        self.entry_username = tk.Entry(self.master)
        self.entry_password = tk.Entry(self.master, show="*")

        self.label_username.pack()
        self.entry_username.pack()
        self.label_password.pack()
        self.entry_password.pack()

        self.logbtn = tk.Button(self.master, text="Login", command=self._login_btn_clicked)
        self.logbtn.pack()'''

'''def _login_btn_clicked(self):
        # Load user data from pickle file
        persona = Persona()
        persona.check_and_create_files()

        with open('C:/Users/benja/OneDrive/Documents/LCIk-2023-1/Paradigmas/FinalPrep/Entrega/Final/Users/users.pickle', 'rb') as file:
            users = pickle.load(file)

        # Check if user exists
        if username in users:
            user = users[username]
            # Verify password
            if user.verify_password(password):
                messagebox.showinfo("Login info", f"Welcome {username}")
            else:
                messagebox.showerror("Login error", "Incorrect password")
        else:
            messagebox.showerror("Login error", "User not found")'''
pass

class Logout:
    ''' def __init__(self, master):
        self.master = master
        self.master.title("Logout")
        self.master.geometry("300x200")

        self.logoutbtn = tk.Button(self.master, text="Logout", command=self._logout_btn_clicked)
        self.logoutbtn.pack()

    def _logout_btn_clicked(self):
        messagebox.showinfo("Logout info", "You have been logged out")'''
    pass

class RegistrarUsuario:
    def __init__(self, master):
        pass