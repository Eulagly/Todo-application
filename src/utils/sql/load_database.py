from tkinter import messagebox
import mysql.connector
import customtkinter
import os
from dotenv import load_dotenv

load_dotenv()

class ToDoMysql:
    """Class representing a MySQL connection for the TO-DO app."""

    def __init__(self):
        """Initialize the MySQL connection."""
        self.connector = mysql.connector.connect(
            host=os.getenv("SQL_HOST"),
            user=os.getenv("SQL_USERNAME"),
            password=os.getenv("SQL_PASSWORD"),
            database=os.getenv("SQL_DATABASE")
        )
        self.cursor = self.connector.cursor()


def load() -> ToDoMysql:
    """Load the MySQL connection.

    Returns:
        ToDoMysql: An instance of the ToDoMysql class representing the MySQL connection.
    """
    db = ToDoMysql()
    return db


def quit_app(screen: customtkinter.CTk, db: ToDoMysql):
    """Quit the application.

    Args:
        screen (customtkinter.CTk): The application screen to be destroyed.
        db (ToDoMysql): The MySQL connection to be closed.

    """
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        screen.destroy()
        db.connector.close()
        db.cursor.close()
