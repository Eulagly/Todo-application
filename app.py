import tkinter as tk
import customtkinter as ctk
import tkinter.messagebox as messagebox

class Todo(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("TO-DO")
        self.geometry("500x500")
        self.resizable(False, False)
        self.logged_in = False

        information_frame = ctk.CTkFrame(self)
        information_frame.place(anchor="c", relx=.5, rely=.5)

        self.login = ctk.CTkLabel(information_frame, text="LOGIN: ", text_color="white", font=("arial", 30, "bold"))
        self.login.grid(row=0, column=0, sticky="E")
        self.login_texbox = ctk.CTkEntry(information_frame, placeholder_text="Username or Email", fg_color="White")
        self.login_texbox.grid(row=0, column=1)

        self.password = ctk.CTkLabel(information_frame, text="PASSWORD: ", text_color="white", font=("arial", 30, "bold"))
        self.password.grid(row=1, column=0, sticky="E")
        self.password_texbox = ctk.CTkEntry(information_frame, placeholder_text="Password", fg_color="White")
        self.password_texbox.grid(row=1, column=1)

        login_button = ctk.CTkButton(information_frame, text="LOGIN",
                                    command=self.login_to_app)
        login_button.grid(row=2, column=0, columnspan=2)

    def login_to_app(self):
        user_login = self.login_texbox.get()
        password = self.password_texbox.get()

        if user_login == '':
            messagebox.showerror("Login Error", "Make sure to include a valid username")
            pass
        elif password == '':
            messagebox.showerror("Login Error", "Make sure to include a valid password")
            pass
        elif "@" in user_login:
            login_type = "email"
        else:
            login_type = "username"



        # Perform MySQL check if the login is legitimate.
        # If it is, set self.logged_in to True.
        # If it's not, the return value will be "PASS ERROR" or "EMAIL OR USERNAME ERROR".
        # If the error is "PASS ERROR", clear the password and show an error message.
        # If the error is "EMAIL OR USERNAME ERROR", clear both the login box and the password box and show an error message.

        # Example implementation:
        # if login_type == "email":
        #     # Check login using email
        # else:
        #     # Check login using username

        # TODO: Implement the login check with MySQL

        # For testing purposes, let's assume the login is not successful
        error_message = "EMAIL OR USERNAME ERROR" if login_type == "email" else "PASS ERROR"
        if error_message == "PASS ERROR":
            password = ''
            messagebox.showerror("Login Error", "Invalid password. Please try again.")
        elif error_message == "EMAIL OR USERNAME ERROR":
            self.login_texbox.delete(0, tk.END)
            self.password_texbox.delete(0, tk.END)
            messagebox.showerror("Login Error", "Invalid email or username. Please try again.")

        # Clear the login and password entry fields
        self.login_texbox.delete(0, tk.END)
        self.password_texbox.delete(0, tk.END)

if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()
