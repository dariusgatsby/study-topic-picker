from tkinter import *
from tkinter import messagebox
from random import choice

# List of topics to study
topics = []


# put topics in or remove them
def add_topic():
    topic_to_add = topic_entry.get()
    if len(topic_to_add) == 0:
        messagebox.showerror(title="Invalid Entry", message="Topic box empty")
        return None
    topic_entry.delete(0, END)
    topic_to_add = topic_to_add.strip()
    topic_to_add = topic_to_add.title()
    topics.append(topic_to_add + '\n')
    with open("study_topics.txt", 'w') as file:
        file.writelines(topics)


# view topics
def show_list_of_topics():
    try:
        with open("study_topics.txt", 'r') as file:
            content = file.readlines()
            contents = [str(x) for x in content]
            msg = '--------- \n'.join(contents)
            if len(content) == 0:
                messagebox.showerror(title="Invalid Entry", message="Topic list empty")
                return None
            messagebox.showinfo(title="Study list", message=msg)
    except FileNotFoundError:
        messagebox.showerror(title="Invalid Entry", message="Topic list empty")


# random choice
def choose_topic():
    try:
        with open("study_topics.txt", 'r') as file:
            content = file.readlines()
            if len(content) == 0:
                messagebox.showerror(title="Invalid Entry", message="Topic list empty")
                return None
            topic_to_display = choice(content)
            canvas.itemconfig(display_topic, text=f"{topic_to_display} excellent choice, stranger")
    except FileNotFoundError:
        messagebox.showerror(title="Invalid Entry", message="Topic list empty")


def delete_item():
    try:
        with open("study_topics.txt", 'r') as file:
            delete_topic = topic_entry.get()
            content = file.readlines()
            if len(content) == 0:
                messagebox.showerror(title="Invalid Entry", message="Topic list empty")
                return None
            delete_topic = delete_topic.strip()
            delete_topic = delete_topic.title()
            print(delete_topic)
            print(content)
        content.remove(delete_topic + '\n')
        with open("study_topics.txt", 'w') as file:
            file.writelines(content)
        topic_entry.delete(0, END)
    except FileNotFoundError:
        messagebox.showerror(title="Invalid Entry", message="Topic list empty")


# tkinter UI
window = Tk()
window.title('Study Topic Selector')
window.geometry("552x358")

bg_img = PhotoImage(file="merchant_bg.png")

canvas = Canvas(window, width=bg_img.width(), height=bg_img.height())
canvas.create_image(bg_img.width() / 2, bg_img.height() / 2, anchor='center', image=bg_img)
canvas.pack(fill="both", expand=True)

display_topic = canvas.create_text(bg_img.width() / 1.65, 200, text="What're ya studying?", font=("Arial", 16, "bold"),
                                   fill="white")

topic_entry = Entry(width=45)
canvas.create_window(bg_img.width() / 2, 260, window=topic_entry, anchor="center")
submit_button = Button(canvas, text="Show topics", command=show_list_of_topics)
canvas.create_window(bg_img.width() / 2 + topic_entry.winfo_reqwidth() / 2 + 10, 260, window=submit_button, anchor="w")

# Define button width and height
button_width = 80
button_height = 30

# Calculate the horizontal space between buttons
horizontal_space = (552 - (3 * button_width)) / 4

# Create three buttons
add_button = Button(canvas, text="✔", command=add_topic)
delete_button = Button(canvas, text="❌", command=delete_item)
pick_button = Button(canvas, text="♻️", command=choose_topic)

# Place the buttons using the calculated positions
add_button.place(relx=0.35, rely=300 / bg_img.height(), anchor="center")
delete_button.place(relx=0.5, rely=300 / bg_img.height(), anchor="center")
pick_button.place(relx=0.65, rely=300 / bg_img.height(), anchor="center")

window.mainloop()
