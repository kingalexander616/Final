import os
import os
import tkinter as tk;
import pickle;
from tkinter import messagebox;
from Persona import Persona;
from Persona import Login;


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("User Authentication System")
        self.logged_in_user = None
        self.is_admin = False

        # Menu Bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # User Menu
        self.user_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.user_menu.add_command(label="Editar Perfil", command=self.edit_profile)
        self.user_menu.add_command(label="Ver Historial", command=self.view_history)
        self.menu_bar.add_cascade(label="Usuario", menu=self.user_menu)

        # Alquileres Menu
        self.alquileres_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.alquileres_menu.add_command(label="Alquilar", command=self.alquilar)
        self.alquileres_menu.add_command(label="Buscar", command=self.buscar)
        self.menu_bar.add_cascade(label="Alquileres", menu=self.alquileres_menu)

        # Admin Menu
        self.admin_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.admin_menu.add_command(label="Admin Action 1", command=self.admin_action_1)
        self.admin_menu.add_command(label="Admin Action 2", command=self.admin_action_2)

        # Login/Register Frame
        self.login_frame = tk.Frame(root)
        self.login_frame.pack()
        self.register_frame = tk.Frame(root)
        self.register_frame.pack()

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=0, column=0, padx=10, pady=10)

        self.register_button = tk.Button(self.register_frame, text="Registrar Usuario", command=self.register_user)
        self.register_button.grid(row=0, column=1, padx=10, pady=10)

        # Placeholder for logged-in user display
        self.logged_in_label = tk.Label(self.root, text="")
        self.logged_in_label.pack(anchor="nw", padx=10, pady=10)

    def login(self):
        # Implement your login logic here
        # For simplicity, let's assume successful login
        self.label_username = tk.Label(self.login_frame, text="Username")
        self.label_password = tk.Label(self.login_frame, text="Password")

        self.entry_username = tk.Entry(self.login_frame)
        self.entry_password = tk.Entry(self.login_frame, show="*")

        self.label_username.grid(row=1, column=0, padx=10, pady=10)
        self.entry_username.grid(row=1, column=1, padx=10, pady=10)
        self.label_password.grid(row=2, column=0, padx=10, pady=10)
        self.entry_password.grid(row=2, column=1, padx=10, pady=10)

        self.logbtn = tk.Button(self.login_frame, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.update_display()
        
    def _login_btn_clicked(self):
        # Load user data from pickle file
        with open('C:/Users/benja/OneDrive/Documents/LCIk-2023-1/Paradigmas/FinalPrep/Entrega/Final/Users/users.pickle', 'rb') as file:
            users = pickle.load(file)
        
        username = self.entry_username.get()
        password = self.entry_password.get()
        print("Attempting login for username:", username)

        # Check if user exists
        if isinstance(users, dict) and username in users:
            user = users[username]
            # Verify password
            if user.verify_password(password):
                messagebox.showinfo("Login info", f"Welcome {username}")
            else:
                messagebox.showerror("Login error", "Incorrect password")
        else:
            messagebox.showerror("Login error", "User not found")


    def register_user(self):
        self.label_usuario = tk.Label(self.register_frame, text="Usuario")
        self.label_nombre = tk.Label(self.register_frame, text="Nombre")
        self.label_apellido = tk.Label(self.register_frame, text="Apellido")
        self.label_tipo_documento = tk.Label(self.register_frame, text="Tipo de Documento")
        self.label_documento = tk.Label(self.register_frame, text="Documento")  # Add this line
        self.label_contraseña = tk.Label(self.register_frame, text="Contraseña")
        self.label_correo = tk.Label(self.register_frame, text="Correo")
        self.label_num_telefono = tk.Label(self.register_frame, text="Número de Teléfono")
        

        self.entry_usuario = tk.Entry(self.register_frame)
        self.entry_nombre = tk.Entry(self.register_frame)
        self.entry_apellido = tk.Entry(self.register_frame)
        self.entry_tipo_documento = tk.Entry(self.register_frame)
        self.entry_documento = tk.Entry(self.register_frame)
        self.entry_contraseña = tk.Entry(self.register_frame, show="*")
        self.entry_correo = tk.Entry(self.register_frame)
        self.entry_num_telefono = tk.Entry(self.register_frame)
        
        self.label_usuario.grid(row=1, column=0, padx=10, pady=10)
        self.entry_usuario.grid(row=1, column=1, padx=10, pady=10)
        self.label_nombre.grid(row=2, column=0, padx=10, pady=10)
        self.entry_nombre.grid(row=2, column=1, padx=10, pady=10)
        self.label_apellido.grid(row=3, column=0, padx=10, pady=10)
        self.entry_apellido.grid(row=3, column=1, padx=10, pady=10)
        self.label_tipo_documento.grid(row=4, column=0, padx=10, pady=10)
        self.entry_tipo_documento.grid(row=4, column=1, padx=10, pady=10)
        self.label_documento.grid(row=5, column=0, padx=10, pady=10)
        self.entry_documento.grid(row=5, column=1, padx=10, pady=10)
        self.label_contraseña.grid(row=6, column=0, padx=10, pady=10)
        self.entry_contraseña.grid(row=6, column=1, padx=10, pady=10)
        self.label_correo.grid(row=7, column=0, padx=10, pady=10)
        self.entry_correo.grid(row=7, column=1, padx=10, pady=10)
        self.label_num_telefono.grid(row=8, column=0, padx=10, pady=10)
        self.entry_num_telefono.grid(row=8, column=1, padx=10, pady=10)
        self.logbtn = tk.Button(self.register_frame, text="Registrar", command=self._registrar_btn_clicked)
        self.logbtn.grid(row=9, column=0, columnspan=2, padx=10, pady=10)
        self.update_display()



    def _registrar_btn_clicked(self):
        # Replace the hardcoded value with your logic to generate unique code
        # Assuming you have a variable `last_codigo_persona` that stores the last generated code
        usuario = self.entry_usuario.get()

        users_file = 'C:/Users/benja/OneDrive/Documents/LCIk-2023-1/Paradigmas/FinalPrep/Entrega/Final/Users/users.pickle'

        if os.path.exists(users_file) and os.path.getsize(users_file) > 0:
            with open(users_file, 'rb') as f:
                usuarios = pickle.load(f)
                ultimo_codigo_persona = max(usuarios.keys())
        else:
            ultimo_codigo_persona = 0
        codigo_persona = ultimo_codigo_persona + 1
        ultimo_codigo_persona = codigo_persona
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        tipo_documento = self.entry_tipo_documento.get()
        documento = self.entry_documento.get()
        contraseña = self.entry_contraseña.get()
        correo = self.entry_correo.get()
        num_telefono = self.entry_num_telefono.get()

        users_file = 'C:/Users/benja/OneDrive/Documents/LCIk-2023-1/Paradigmas/FinalPrep/Entrega/Final/Users/users.pickle'
        usernames_file = 'C:/Users/benja/OneDrive/Documents/LCIk-2023-1/Paradigmas/FinalPrep/Entrega/Final/Users/usernames.pickle'

        with open(users_file, 'ab') as f:
            usuarios = {}
            if os.path.getsize(users_file) > 0:
                usuarios = pickle.load(f)
        if usuario not in usuarios:
            usuarios[usuario] = Persona(usuario, codigo_persona, nombre, apellido, tipo_documento, documento, contraseña, correo, num_telefono)
        with open('C:/Users/benja/OneDrive/Documents/LCIk-2023-1/Paradigmas/FinalPrep/Entrega/Final/Users/usernames.pickle', 'ab') as f:
            pickle.dump(usuario, f)

        persona = Persona(
            codigo_persona=codigo_persona,
            usuario=usuario,
            nombre=nombre,
            apellido=apellido,
            tipo_documento=tipo_documento,
            documento=documento,
            contraseña=contraseña,
            correo=correo,
            num_telefono=num_telefono
        )
        with open('C:/Users/benja/OneDrive/Documents/LCIk-2023-1/Paradigmas/FinalPrep/Entrega/Final/Users/users.pickle', 'ab') as f:
            pickle.dump(persona, f)

    def logout(self):
        self.logged_in_user = None
        self.is_admin = False
        self.update_display()

    def update_display(self):
        if self.logged_in_user:
            self.login_frame.pack_forget()
            self.logged_in_label.config(text=f"Usuario: {self.logged_in_user}")
            self.logged_in_label.pack(anchor="nw", padx=10, pady=10)
            self.user_menu.entryconfig("Editar Perfil", state="normal")
            self.user_menu.entryconfig("Ver Historial", state="normal")
            self.alquileres_menu.entryconfig("Alquilar", state="normal")
            self.alquileres_menu.entryconfig("Buscar", state="normal")
            self.menu_bar.add_command(label="Logout", command=self.logout)
            if self.is_admin:
                self.menu_bar.add_cascade(label="Admin", menu=self.admin_menu)
            else:
                self.menu_bar.delete("Admin")
        else:
            self.logged_in_label.pack_forget()
            self.login_frame.pack()
            self.user_menu.entryconfig("Editar Perfil", state="disabled")
            self.user_menu.entryconfig("Ver Historial", state="disabled")
            self.alquileres_menu.entryconfig("Alquilar", state="disabled")
            self.alquileres_menu.entryconfig("Buscar", state="disabled")
            # Add more menu entries and configurations as needed
            self.menu_bar.delete("Logout")
            self.menu_bar.delete("Admin")

    def edit_profile(self):
        # Implement your edit profile logic here
        messagebox.showinfo("Editar Perfil", "Editando perfil del usuario.")

    def view_history(self):
        # Implement your view history logic here
        messagebox.showinfo("Ver Historial", "Viendo historial del usuario.")

    def alquilar(self):
        # Implement your alquilar logic here
        messagebox.showinfo("Alquileres", "Realizando alquiler.")

    def buscar(self):
        # Implement your buscar logic here
        messagebox.showinfo("Alquileres", "Buscando alquileres disponibles.")

    def admin_action_1(self):
        # Implement your admin action 1 logic here
        messagebox.showinfo("Admin", "Realizando acción de administrador 1.")

    def admin_action_2(self):
        # Implement your admin action 2 logic here
        messagebox.showinfo("Admin", "Realizando acción de administrador 2.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
