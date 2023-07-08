import tkinter as tk
import tkinter.messagebox as messagebox
import customtkinter as ctk
import asyncio
import utils.sql.load_database as database
import utils.sql.login as lg


class Todo(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.db = database.load()
        self.title("TO-DO")
        self.geometry("500x500")
        self.resizable(False, False)
        self.logged_in = False
        self.protocol("WM_DELETE_WINDOW",lambda: database.quit_app(self, self.db))
        self.create_login_screen()

    def create_login_screen(self):
        login_screen_frame = ctk.CTkFrame(self)
        login_screen_frame.place(anchor="c", relx=.5, rely=.5)

        self.login = ctk.CTkLabel(login_screen_frame, text="LOGIN: ", text_color="white",
                                  font=("arial", 30, "bold"))
        self.login.grid(row=0, column=0, sticky="E")
        self.login_texbox = ctk.CTkEntry(login_screen_frame, placeholder_text="Username or Email",
                                          fg_color="White")
        self.login_texbox.grid(row=0, column=1)

        self.password = ctk.CTkLabel(login_screen_frame, text="PASSWORD: ", text_color="white",
                                     font=("arial", 30, "bold"))
        self.password.grid(row=1, column=0, sticky="E")
        self.password_texbox = ctk.CTkEntry(login_screen_frame, placeholder_text="Password",
                                             fg_color="White")
        self.password_texbox.grid(row=1, column=1)

        login_button = ctk.CTkButton(login_screen_frame, text="LOGIN", command=self.login_to_app)
        login_button.grid(row=2, column=0, columnspan=2)

    async def check_login(self, user_login, password):
        login = lg.login(self.db, user_login, password)
        return login

    async def handle_login(self):
        user_login = self.login_texbox.get()
        password = self.password_texbox.get()

        result = await self.check_login(user_login, password)

        if type(result) == tuple:
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

    def login_to_app(self):
        asyncio.run(self.handle_login())



if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()
