import tkinter as tk
from PIL import ImageTk, Image
import random

para = 0


def coin():
    global para
    para += 10
    Para.config(text="Para: {0}".format(para))


def buy_confirmation():
    confirmation_label.place(x=30, y=400)
    confirmation_label.config(text="300 para karşılığı satın almak istiyor musunuz?")
    yes_button.place(x=30, y=430)
    no_button.place(x=110, y=430)
    boxesb.config(state="disabled")


def confirm_action():
    global para
    if para >= 300:
        confirmation_label.config(text="Satın alma işlemi tamamlandı.")
        yes_button.place_forget()
        no_button.place_forget()
        boxesb.config(state="normal")
        para -= 300
        Para.config(text="Para: {0}".format(para))
        confirmation_label.after(1000, cancel_action)
        show_random_item()
    else:
        confirmation_label.config(text="Yetersiz Para")
        confirmation_label.after(1000, cancel_action)


def cancel_action():
    confirmation_label.config(text="")
    yes_button.place_forget()
    no_button.place_forget()
    boxesb.config(state="normal")
    confirmation_label.place_forget()


def show_random_item():
    ihtimal = random.randint(1, 101)
    if ihtimal < 46:
        item_image = Image.open('C:/Users/HP/Downloads/Break-Tower-main/Break-Tower-main/Karambit.png')
    elif 44 <= ihtimal <= 91:
        item_image = Image.open('C:/Users/HP/Downloads/Break-Tower-main/Break-Tower-main/Hammer.png')
    elif 90 <= ihtimal <= 96:
        item_image = Image.open('C:/Users/HP/Downloads/Break-Tower-main/Break-Tower-main/Axe.png')
    elif 94 <= ihtimal <= 101:
        item_image = Image.open('C:/Users/HP/Downloads/Break-Tower-main/Break-Tower-main/Sword.png')

    resized_item = item_image.resize((100, 100))
    item_photo = ImageTk.PhotoImage(resized_item)
    item_label = tk.Label(root, image=item_photo)
    item_label.place(x=root.winfo_width() // 2 - 50, y=root.winfo_height() // 2 - 50)
    animate_item(item_label)


def animate_item(item_label):
    for i in range(10):
        item_label.place(x=item_label.winfo_x() + (i % 2) * 10 - 5, y=item_label.winfo_y())
        item_label.update()
        item_label.after(100)
    item_label.place_forget()


root = tk.Tk()
root.geometry('1920x1080')

world_bg = Image.open('C:/Users/HP/Downloads/Break-Tower-main/Break-Tower-main/World - Bg.png')
resized_image = world_bg.resize((1400, 720))
world_bg = ImageTk.PhotoImage(resized_image)

tower_image = Image.open('C:/Users/HP/Downloads/Break-Tower-main/Break-Tower-main/Tower.png')
resized_tower = tower_image.resize((480, 480))
tower_photo = ImageTk.PhotoImage(resized_tower)

WBg = tk.Label(root, image=world_bg)
WBg.pack()

tower_button = tk.Button(root, image=tower_photo, bd=0, highlightthickness=0, command=coin)
tower_button.place(x=890, y=175)

boxes = Image.open('C:/Users/HP/Downloads/Break-Tower-main/Break-Tower-main/Sky - Giftbox.png')
resized_boxes = boxes.resize((100, 100))
boxes_photo = ImageTk.PhotoImage(resized_boxes)

boxesb = tk.Button(root, image=boxes_photo, bd=0, highlightthickness=0, command=buy_confirmation)
boxesb.place(x=30, y=275)

confirmation_label = tk.Label(root, text="", font=("Arial", 12))

yes_button = tk.Button(root, text="Evet", font=("Arial", 12), command=confirm_action)
no_button = tk.Button(root, text="Hayır", font=("Arial", 12), command=cancel_action)

Para = tk.Label(root, text="Para: {0}".format(para), font=("Arial Bold", 20))
Para.place(x=1200, y=10)

root.mainloop()
