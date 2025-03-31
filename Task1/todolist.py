from tkinter import *
from tkinter import messagebox
import sqlite3

# Function to add a task
def add_new_task():
    task_text = task_input.get()
    if not task_text:
        messagebox.showwarning("Warning", "Task field is empty!")
        return
    task_items.append(task_text)
    db_cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task_text,))
    update_task_list()
    task_input.delete(0, END)

# Function to update listbox
def update_task_list():
    task_listbox.delete(0, END)
    for task in task_items:
        task_listbox.insert(END, task)

# Function to remove a selected task
def remove_task():
    try:
        selected_task = task_listbox.get(ACTIVE)
        task_items.remove(selected_task)
        db_cursor.execute("DELETE FROM tasks WHERE task = ?", (selected_task,))
        update_task_list()
    except:
        messagebox.showerror("Error", "No task selected!")

# Function to delete all tasks
def clear_all_tasks():
    if messagebox.askyesno("Confirmation", "Delete all tasks?"):
        task_items.clear()
        db_cursor.execute("DELETE FROM tasks")
        update_task_list()

# Function to close the application
def close_app():
    root.destroy()
    db_connection.commit()
    db_cursor.close()
    db_connection.close()

# Function to fetch tasks from the database
def load_tasks():
    task_items.clear()
    for row in db_cursor.execute("SELECT task FROM tasks"):
        task_items.append(row[0])
    update_task_list()

# GUI Setup
root = Tk()
root.title("Task Manager")
root.geometry("600x400")
root.configure(bg="#A2D9CE")

# Database setup
db_connection = sqlite3.connect("tasks.db")
db_cursor = db_connection.cursor()
db_cursor.execute("CREATE TABLE IF NOT EXISTS tasks (task TEXT)")

task_items = []

frame = Frame(root, bg="#76D7C4")
frame.pack(pady=20, padx=20, fill="both", expand=True)

Label(frame, text="Task Manager", font=("Arial", 16, "bold"), bg="#76D7C4").pack()

task_input = Entry(frame, font=("Arial", 12), width=40)
task_input.pack(pady=10)

Button(frame, text="Add Task", command=add_new_task, bg="#F4D03F", font=("Arial", 12)).pack()
Button(frame, text="Remove Task", command=remove_task, bg="#E74C3C", font=("Arial", 12)).pack()
Button(frame, text="Clear All", command=clear_all_tasks, bg="#E67E22", font=("Arial", 12)).pack()
Button(frame, text="Exit", command=close_app, bg="#D35400", font=("Arial", 12)).pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

task_listbox = Listbox(frame, width=50, height=10, yscrollcommand=scrollbar.set, font=("Arial", 10))
task_listbox.pack()
scrollbar.config(command=task_listbox.yview)

load_tasks()
root.mainloop()
