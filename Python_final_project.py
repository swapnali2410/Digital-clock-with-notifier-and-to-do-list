import tkinter as tk
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime

def date_time():
    time_now = datetime.datetime.now()
    hr = time_now.strftime('%I')
    mi = time_now.strftime('%M')
    sec = time_now.strftime('%S')
    am = time_now.strftime('%p')

    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)

    lab_hr.after(200, date_time)

def show_reminder():
    notification.notify(
        title=reminder_title,
        message=reminder_msg,
        app_name="Notifier",
        timeout=10
    )

def get_details():
    global reminder_title, reminder_msg, reminder_time
    reminder_title = title.get()
    reminder_msg = msg.get()
    reminder_time = time1.get()

    if reminder_title == "" or reminder_msg == "" or reminder_time == "":
        messagebox.showerror("Alert", "All fields are required!")
    else:
        int_time = int(float(reminder_time))
        min_to_sec = int_time * 60
        messagebox.showinfo("Notifier set", "Set notification?")
        t.after(min_to_sec * 1000, show_reminder)



def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        pass

# Main Tkinter window
t = tk.Tk()
t.title('Digital Clock with Notifier and To-Do List')
t.config(bg="#c1e6dc")

# Digital clock layout
frame_clock = tk.Frame(t)
frame_clock.pack(side=tk.TOP, pady=20)

lab_hr = tk.Label(frame_clock, text="00", font=('Time New Roman', 50, 'bold'), fg="black")
lab_hr.pack(side=tk.LEFT, padx=10)

lab_dot =tk.Label(frame_clock, text=":", font=('Time New Roman', 50, 'bold'), fg="black")
lab_dot.pack(side=tk.LEFT, padx=10)

lab_min = tk.Label(frame_clock, text="00", font=('Time New Roman', 50, 'bold'), fg="black")
lab_min.pack(side=tk.LEFT, padx=10)

lab_dot =tk.Label(frame_clock, text=":", font=('Time New Roman', 50, 'bold'), fg="black")
lab_dot.pack(side=tk.LEFT, padx=10)

lab_sec = tk.Label(frame_clock, text="00", font=('Time New Roman', 50, 'bold'), fg="black")
lab_sec.pack(side=tk.LEFT, padx=10)

lab_am = tk.Label(frame_clock, text="AM", font=('Time New Roman', 40, 'bold'), fg="black")
lab_am.pack(side=tk.LEFT, padx=10)

# Notifier layout
frame_notifier = tk.Frame(t,bg="#496860")
frame_notifier.pack(pady=20)

t_label = tk.Label(frame_notifier, text="Title to Notify :", font=("poppins", 10))
t_label.pack(pady=5)

title = tk.Entry(frame_notifier, width="40", font=("poppins", 13))
title.pack(pady=5)

m_label = tk.Label(frame_notifier, text="Display Message :", font=("poppins", 10))
m_label.pack(pady=5)

msg = tk.Entry(frame_notifier, width="40", font=("poppins", 13))
msg.pack(pady=5)

time_label = tk.Label(frame_notifier, text="Set Time (in minutes) :", font=("poppins", 10))
time_label.pack(pady=5)

time1 = tk.Entry(frame_notifier, width="5", font=("poppins", 13))
time1.pack(pady=5)


but = tk.Button(frame_notifier, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="black", bg="#c1e6dc", width=20,
                relief="raised", command=get_details)
but.pack(pady=20)




# To-Do List layout
frame_tasks = tk.Frame(t,bg="#496860")
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set,fg="#496860",font="bold")
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(frame_tasks, width=50)
entry_task.pack(pady=5)

button_add_task = tk.Button(frame_tasks, text="Add task", width=48, command=add_task)
button_add_task.pack(pady=5)

button_delete_task = tk.Button(frame_tasks, text="Delete task", width=48, command=delete_task)
button_delete_task.pack(pady=5)



# Schedule the initial reminder check and start the main loop
t.after(0, date_time)
t.mainloop()
