import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Manager")
        self.master.geometry("650x500")
        self.master.config(bg="#1abc9c")
        self.task_list = []

        self.input_field = tk.Entry(master, width=45, font=('Helvetica', 14))
        self.input_field.grid(row=0, column=0, padx=10, pady=15)

        add_btn = tk.Button(master, text="Add Task", command=self.add_task, font=('Helvetica', 12), bg="#27ae60", fg="#ffffff", width=12)
        add_btn.grid(row=0, column=1, padx=10, pady=15)

        self.task_display = tk.Listbox(master, width=55, height=15, font=('Helvetica', 12), bg="#ecf0f1", fg="#34495e", selectbackground="#1abc9c")
        self.task_display.grid(row=1, column=0, columnspan=2, padx=10, pady=15)

        delete_btn = tk.Button(master, text="Delete Task", command=self.delete_task, font=('Helvetica', 12), bg="#e74c3c", fg="#ffffff", width=12)
        delete_btn.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        mark_done_btn = tk.Button(master, text="Mark as Done", command=self.mark_done, font=('Helvetica', 12), bg="#f1c40f", fg="#ffffff", width=12)
        mark_done_btn.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.task_display.bind('<Double-Button-1>', lambda event: self.mark_done())

    def add_task(self):
        task = self.input_field.get()
        if task:
            self.task_list.append(task)
            self.refresh_task_display()
            self.input_field.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_task_index = self.task_display.curselection()
        if selected_task_index:
            self.task_list.pop(selected_task_index[0])
            self.refresh_task_display()

    def mark_done(self):
        selected_task_index = self.task_display.curselection()
        if selected_task_index:
            completed_task = self.task_list.pop(selected_task_index[0])
            completed_task = f"[Done] {completed_task}"
            self.task_list.append(completed_task)
            self.refresh_task_display()

    def refresh_task_display(self):
        self.task_display.delete(0, tk.END)
        for task in self.task_list:
            self.task_display.insert(tk.END, task)

if __name__ == "__main__":
    master = tk.Tk()
    app = TaskManagerApp(master)
    master.mainloop()
