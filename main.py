from tkinter import *

# List of topics to study
topics = []
# put topics in or remove them

# view topics

# random choice

# tkinter UI

window = Tk()
window.title('Study Topic Selector')
window.geometry("552x351")


bg_img = PhotoImage(file="background.png")
canvas = Canvas(width=532, height=351)
bg_label = Label(image=bg_img)
bg_label.place(x=0, y=0)

canvas.create_text(266, 176, text="Topic")
canvas.place(relx=0.5, rely=100 / 351, anchor="center")

canvas.create_text(266, 0, text="Topic", font=("Arial", 16, "bold"), anchor="n")


topic_entry = Entry(width=45)
topic_entry.place(relx=0.5, rely=260 / 351, anchor="center")

# Define button width and height
button_width = 80
button_height = 30

# Calculate the horizontal space between buttons
horizontal_space = (552 - (3 * button_width)) / 4

# Create three buttons
button1 = Button(text="✔")
button2 = Button(text="❌")
button3 = Button(text="♻️")

# Place the buttons using the calculated positions
button1.place(relx=(horizontal_space + button_width) / 552, rely=300 / 351, anchor="center")
button2.place(relx=0.5, rely=300 / 351, anchor="center")
button3.place(relx=(552 - (button_width + horizontal_space)) / 552, rely=300 / 351, anchor="center")



window.mainloop()