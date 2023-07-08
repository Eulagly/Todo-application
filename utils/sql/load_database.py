from tkinter import messagebox
import mysql.connector
import customtkinter


class ToDoMysql:
    def __init__(self):
        self.connector = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Eula",
            database="todo"
        )

        self.cursor = self.connector.cursor()


def load():
    db = ToDoMysql()
    return db


def quit_app(screen: customtkinter.CTk, db: ToDoMysql):
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        screen.destroy()
        db.connector.close()
        db.cursor.close()
