from tkinter import *
from tkinter import filedialog
import pandas as pd
import detecter as detect
import urllib.request
from PIL import Image, ImageTk
import io

root = Tk()
root.title('Vehicle Classification and Counting')
root.geometry("850x480")


def upload():

    global res
    res = [2, 3, 1, 0, 3, 1, 0, 0]
    root.filename = filedialog.askopenfilename(initialdir=r"Documents",
                                               title="Select A File", filetypes=(("mp4 files", "*.mp4"), ("all files", "*.*")))
    res = detect.foo(root.filename)
    changepage1()


def webcam():
    global res
    res = [2, 3, 1, 0, 3, 1, 0, 0]
    res = detect.foo(0)
    changepage1()

def page1(root):

    # img_url = "https://media.istockphoto.com/id/903246714/photo/motion-blurred-photograph-of-traffic-at-in-night-in-the-rain-on-a-british-motorway-with-police.jpg?b=1&s=170667a&w=0&k=20&c=naKM2NR4zxugJbZMs9VodqeMryNBQTuMDInw3s8giYQ="
    # global bg
    # with urllib.request.urlopen(img_url) as connection:
    #     raw_data = connection.read()
    # im = Image.open(io.BytesIO(raw_data))
    bg = Image.open("bg.jpg")
    resized = bg.resize((850, 480), Image.ANTIALIAS)
    bg = ImageTk.PhotoImage(resized)

    canvas1 = Canvas(root, width=400,
                     height=400)

    canvas1.pack(fill="both", expand=True)

    # Display image
    canvas1.create_image(0, 0, image=bg,
                         anchor="nw")

    canvas1.create_text(420, 120, text="VEHICLE CLASSIFICATION AND COUNTING",
                                                fill="white", font=('Helvetica 21 bold'))
    canvas1.create_text(660, 170, text="Made by: Nimarta",
                                                fill="white", font=('Helvetica 18 italic'))

    button1 = Button(root, text="       Browse File      ",
                                             fg='black', font=("Helvetica", 20), command=upload)

    button1_canvas = canvas1.create_window(280, 280, anchor="nw",
                                                                   window=button1)

    button2 = Button(root, text="   Open WebCam    ",
                     fg='black', font=("Helvetica", 20), command=webcam)

    button1_canvas = canvas1.create_window(280, 360, anchor="nw",
                                           window=button2)

    # Execute tkinter
    root.mainloop()


def page2(root):
    page = Frame(root)
    page.pack()

    Label(page, text='', fg='black', font=(
        "Helvetica", 25)).grid(row=1, column=3, columnspan=2)
    Label(page, text='RESULTS', fg='black', font=(
        "Helvetica", 25)).grid(row=2, column=3, columnspan=2)
    Label(page, text='', fg='black', font=(
        "Helvetica", 25)).grid(row=3, column=3, columnspan=2)
    Label(page, text='   ', fg='#20b2aa', font=("Helvetica", 5)).grid(
        row=5, column=3, columnspan=2)
    Label(page, text='Car', fg='#20b2aa', font=(
        "Helvetica", 18)).grid(row=6, column=2)
    Label(page, text='Motorbike', fg='#20b2aa', font=(
        "Helvetica", 18)).grid(row=7, column=2)
    Label(page, text='Bus', fg='#20b2aa', font=(
        "Helvetica", 18)).grid(row=8, column=2)
    Label(page, text='Truck', fg='#20b2aa', font=(
        "Helvetica", 18)).grid(row=9, column=2)
    Label(page, text='Total', fg='#3902b5', font=(
        "Helvetica", 18)).grid(row=10, column=2)
    Label(page, text='Upwards', fg='#3902b5', font=(
        "Helvetica", 18)).grid(row=5, column=4)
    Label(page, text=res[0], fg='#20b2aa', font=(
        "Helvetica", 18)).grid(row=6, column=4)
    Label(page, text=res[1], fg='#20b2aa', font=(
        "Helvetica", 18)).grid(row=7, column=4)
    Label(page, text=res[2], fg='#20b2aa', font=(
        "Helvetica", 18)).grid(row=8, column=4)
    Label(page, text=res[3], fg='#20b2aa', font=(
        "Helvetica", 18)).grid(row=9, column=4)
    Label(page, text=(res[0]+res[1]+res[2]+res[3]), fg='#3902b5', font=(
        "Helvetica", 18)).grid(row=10, column=4)
    Label(page, text='Downwards', fg='#3902b5', font=(
        "Helvetica", 18)).grid(row=5, column=5)
    Label(page, text=res[4], fg='#20b2aa', font=(
        "Helvetica", 18)).grid(row=6, column=5)
    Label(page, text=res[5], fg='#20b2aa', font=(
        "Helvetica", 18)).grid(row=7, column=5)
    Label(page, text=res[6], fg='#20b2aa', font=(
        "Helvetica", 18)).grid(row=8, column=5)
    Label(page, text=res[7], fg='#20b2aa', font=(
        "Helvetica", 18)).grid(row=9, column=5)
    Label(page, text=(res[4]+res[5]+res[6]+res[7]), fg='#3902b5', font=(
        "Helvetica", 18)).grid(row=10, column=5)
    Label(page, text='', fg='#20b2aa', font=(
        "Helvetica", 18)).grid(row=11, column=5)
    Label(page, text='', fg='#20b2aa', font=(
        "Helvetica", 18)).grid(row=12, column=5)
    Button(page, text='BACK', fg='black', font=("Helvetica", 18), command=changepage2).grid(
        row=15, column=4)


def changepage1():
    global pagenum, root
    for widget in root.winfo_children():
        widget.destroy()
    page2(root)

def changepage2():
    global pagenum, root
    for widget in root.winfo_children():
        widget.destroy()
    page1(root)

pagenum = 1

page1(root)

root.mainloop()
