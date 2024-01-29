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

canvas = Canvas(window, width=bg_img.width(), height=bg_img.height())
canvas.create_image(bg_img.width()/2, bg_img.height()/2, anchor='center', image=bg_img)
canvas.pack(fill="both", expand=True)

canvas.create_text(bg_img.width()/2, 150, text="Topic", font=("Arial", 16, "bold"), fill="white")



topic_entry = Entry(width=45)
canvas.create_window(bg_img.width()/2, 260, window=topic_entry, anchor="center")

# Define button width and height
button_width = 80
button_height = 30

# Calculate the horizontal space between buttons
horizontal_space = (552 - (3 * button_width)) / 4

# Create three buttons
button1 = Button(canvas, text="✔")
button2 = Button(canvas, text="❌")
button3 = Button(canvas, text="♻️")

# Place the buttons using the calculated positions
button1.place(relx=0.35, rely=300 / bg_img.height(), anchor="center")
button2.place(relx=0.5, rely=300 / bg_img.height(), anchor="center")
button3.place(relx=0.65, rely=300 / bg_img.height(), anchor="center")


window.mainloop()