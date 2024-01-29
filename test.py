from tkinter import Tk, PhotoImage, Canvas, Entry, Button

def button_click(button_number):
    print(f"Button {button_number} clicked!")

window = Tk()
window.title('Study Topic Selector')
window.geometry("552x351")

bg_img = PhotoImage(file="background.png")

# Set canvas dimensions to match the image
canvas = Canvas(window, width=bg_img.width(), height=bg_img.height())
canvas.create_image(bg_img.width()/2, bg_img.height()/2, anchor='center', image=bg_img)
canvas.pack(fill="both", expand=True)

# Create text in the middle of the canvas
canvas.create_text(bg_img.width()/2, 100, text="Topic", font=("Arial", 16, "bold"), anchor="n")


topic_entry = Entry(width=45)
canvas.create_window(bg_img.width()/2, 260, window=topic_entry, anchor="center")

# Define button width and height
button_width = 80
button_height = 30

# Create three buttons
button1 = Button(canvas, text="✔", command=lambda: button_click(1))
button2 = Button(canvas, text="❌", command=lambda: button_click(2))
button3 = Button(canvas, text="♻️", command=lambda: button_click(3))

# Place the buttons evenly spaced along the width of the canvas
button1.place(relx=0.35, rely=300 / bg_img.height(), anchor="center")
button2.place(relx=0.5, rely=300 / bg_img.height(), anchor="center")
button3.place(relx=0.65, rely=300 / bg_img.height(), anchor="center")

window.mainloop()
