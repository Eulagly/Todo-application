from tkinter import messagebox
import mysql.connector
import customtkinter
import os
from dotenv import load_dotenv
class ToDoMysql:
    def __init__(self):
        load_dotenv()
        self.connector = mysql.connector.connect(
            host=os.getenv("SQL_HOST"),
            user=os.getenv("SQL_USERNAME"),
            password=os.getenv("SQL_PASSWORD"),
            database=os.getenv("SQL_DATABASE")
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
