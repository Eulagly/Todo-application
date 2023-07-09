import asyncio
import tkinter as tk
from tkinter import messagebox

import mysql.connector
import customtkinter as ctk

import utils.sql.load_database as database
import utils.sql.login as lg


class Todo(ctk.CTk):
    """Main application class for the TO-DO app."""

    def __init__(self):
        """Initialize the application."""
        super().__init__()
        self.db = database.load()
        self.title("TO-DO")
        self.geometry("500x500")
        self.resizable(False, False)
        self.logged_in = False
        self.protocol("WM_DELETE_WINDOW", lambda: database.quit_app(self, self.db))
        self.create_login_screen()

    def create_login_screen(self):
        """Create the login screen widgets."""
        login_frame = ctk.CTkFrame(self)
        login_frame.place(anchor="c", relx=.5, rely=.5)

        self.login = ctk.CTkLabel(login_frame, text="LOGIN: ", text_color="white", font=("arial", 30, "bold"))
        self.login.grid(row=0, column=0, sticky="E")
        self.login_texbox = ctk.CTkEntry(login_frame, placeholder_text="Username or Email", fg_color="White")
        self.login_texbox.grid(row=0, column=1)

        self.password = ctk.CTkLabel(login_frame, text="PASSWORD: ", text_color="white", font=("arial", 30, "bold"))
        self.password.grid(row=1, column=0, sticky="E")
        self.password_texbox = ctk.CTkEntry(login_frame, placeholder_text="Password", fg_color="White")
        self.password_texbox.grid(row=1, column=1)

        login_button = ctk.CTkButton(login_frame, text="LOGIN", command=self.login_to_app)
        login_button.grid(row=2, column=0, columnspan=2)

        signup_button = ctk.CTkButton(login_frame, text="SIGN UP", command=self.create_signup_screen)
        signup_button.grid(row=3, column=0, columnspan=2)

    def create_signup_screen(self):
        """Create the signup screen widgets."""
        signup_frame = ctk.CTkFrame(self)
        signup_frame.place(anchor="c", relx=.5, rely=.5)

        self.signup = ctk.CTkLabel(signup_frame, text="SIGN UP: ", text_color="white", font=("arial", 30, "bold"))
        self.signup.grid(row=0, column=0, sticky="E")
        self.signup_texbox = ctk.CTkEntry(signup_frame, placeholder_text="Username", fg_color="White")
        self.signup_texbox.grid(row=0, column=1)

        self.email = ctk.CTkLabel(signup_frame, text="EMAIL: ", text_color="white", font=("arial", 30, "bold"))
        self.email.grid(row=1, column=0, sticky="E")
        self.email_texbox = ctk.CTkEntry(signup_frame, placeholder_text="Email", fg_color="White")
        self.email_texbox.grid(row=1, column=1)

        self.password_signup = ctk.CTkLabel(signup_frame, text="PASSWORD: ", text_color="white", font=("arial", 30, "bold"))
        self.password_signup.grid(row=2, column=0, sticky="E")
        self.password_texbox_signup = ctk.CTkEntry(signup_frame, placeholder_text="Password", fg_color="White")
        self.password_texbox_signup.grid(row=2, column=1)

        signup_button = ctk.CTkButton(signup_frame, text="SIGN UP", command=self.signup_to_app)
        signup_button.grid(row=3, column=0, columnspan=2)

    async def check_login(self, user_login, password):
        """Check the login credentials asynchronously.

        Args:
            user_login (str): The username or email entered by the user.
            password (str): The password entered by the user.

        Returns:
            tuple or str: If the login is successful, returns a tuple of user details.
                          If the credentials are invalid, returns an appropriate error message.
        """
        login = lg.login(self.db, user_login, password)
        return login

    async def check_signup(self, username, email, password):
        """Check the signup credentials asynchronously.

        Args:
            username (str): The username entered by the user.
            email (str): The email entered by the user.
            password (str): The password entered by the user.

        Returns:
            int or str: If the signup is successful, returns a user ID.
                        If the username or email is already taken, returns an appropriate error message.
        """
        signup = lg.signup(self.db, email, username, password)
        return signup

    async def handle_login(self):
        """Handle the login process asynchronously."""
        user_login = self.login_texbox.get()
        password = self.password_texbox.get()

        result = await self.check_login(user_login, password)

        if isinstance(result, tuple):
            self.logged_in = True
            messagebox.showinfo("Login Success", "Logged in successfully!")
        elif result == "INVALID_USERNAME_OR_EMAIL":
            messagebox.showerror("Login Error", "Make sure to include a valid username or email")
        elif result == "INVALID_PASSWORD":
            messagebox.showerror("Login Error", "Make sure to include a valid password")
        else:
            self.login_texbox.delete(0, tk.END)
            self.password_texbox.delete(0, tk.END)
            messagebox.showerror("Login Error", "Invalid email or password. Please try again.")

    async def handle_signup(self):
        """Handle the signup process asynchronously."""
        username = self.signup_texbox.get()
        email = self.email_texbox.get()
        password = self.password_texbox_signup.get()
        if not username or not email or not password:
            messagebox.showinfo("Fields", "Make sure to fill out all fields.")
            return
        if '@' not in email or '.' not in email:
            messagebox.showinfo("Invalid Email", "Make sure to give a valid email")
            return
        result = await self.check_signup(username, email, password)

        if isinstance(result, int):
            messagebox.showinfo("Signup Success", "Signed up successfully!")
            self.create_login_screen()
        elif result == "USERNAME_TAKEN":
            messagebox.showerror("Signup Error", "Username already taken. Please choose a different one.")
        elif result == "EMAIL_TAKEN":
            messagebox.showerror("Signup Error", "Email already taken. Please choose a different one.")
        else:
            self.signup_texbox.delete(0, tk.END)
            self.email_texbox.delete(0, tk.END)
            self.password_texbox_signup.delete(0, tk.END)
            messagebox.showerror("Signup Error", "Failed to sign up. Please try again.")

    def login_to_app(self):
        """Trigger the login process."""
        asyncio.run(self.handle_login())

    def signup_to_app(self):
        """Trigger the signup process."""
        asyncio.run(self.handle_signup())


if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()
