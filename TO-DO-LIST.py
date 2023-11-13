import tkinter as tk
from tkinter import ttk

class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.task_list = []
        
        self.create_task_entry()
        self.create_task_display()
        
    def create_task_entry(self):
        frame = ttk.LabelFrame(self.root, text="Add Task")
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        ttk.Label(frame, text="Description:").grid(row=0, column=0)
        self.description_entry = ttk.Entry(frame)
        self.description_entry.grid(row=0, column=1)

        ttk.Label(frame, text="Due Date:").grid(row=1, column=0)
        self.due_date_entry = ttk.Entry(frame)
        self.due_date_entry.grid(row=1, column=1)

        ttk.Label(frame, text="Priority:").grid(row=2, column=0)
        self.priority_entry = ttk.Entry(frame)
        self.priority_entry.grid(row=2, column=1)

        ttk.Button(frame, text="Add Task", command=self.add_task).grid(row=3, columnspan=2)

    def create_task_display(self):
        frame = ttk.LabelFrame(self.root, text="Tasks")
        frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.task_listbox = tk.Listbox(frame, height=10, width=50)
        self.task_listbox.grid(row=0, column=0, columnspan=2)
        self.task_listbox.bind("<<ListboxSelect>>", self.select_task)

        ttk.Button(frame, text="Mark as Completed", command=self.mark_completed).grid(row=1, column=0)
        ttk.Button(frame, text="Remove Task", command=self.remove_task).grid(row=1, column=1)

    def add_task(self):
        description = self.description_entry.get()
        due_date = self.due_date_entry.get()
        priority = self.priority_entry.get()
        
        if description and due_date and priority:
            task = Task(description, due_date, priority)
            self.task_list.append(task)
            self.update_task_listbox()
            self.clear_entry_fields()
        else:
            self.show_error("All fields are required.")

    def select_task(self, event):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.selected_task_index = selected_task_index[0]
        else:
            self.selected_task_index = None

    def mark_completed(self):
        if self.selected_task_index is not None:
            self.task_list[self.selected_task_index].completed = True
            self.update_task_listbox()
            self.selected_task_index = None
        else:
            self.show_error("Please select a task to mark as completed.")

    def remove_task(self):
        if self.selected_task_index is not None:
            self.task_list.pop(self.selected_task_index)
            self.update_task_listbox()
            self.selected_task_index = None
        else:
            self.show_error("Please select a task to remove.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.task_list:
            status = "Completed" if task.completed else "Incomplete"
            self.task_listbox.insert(tk.END, f"{task.description} (Due: {task.due_date}, Priority: {task.priority}, Status: {status}")

    def clear_entry_fields(self):
        self.description_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)

    def show_error(self, message):
        tk.messagebox.showerror("Error", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
