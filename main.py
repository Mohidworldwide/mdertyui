from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTK

root=Tk()
root.title('Denomination Counter')
root.configure(bg="cyan")
root.geometry("650x400")

upload=Image.open("workkkkk.PNG")

upload=upload.resize((290, 370))
image=ImageTK.PhotoImage(upload)
label=Label(root, image=image, bg='blue')
label.place(x=180, y=20)

label1=Label(root, text="hey dude! Welcome to Denomination counter website thingy :)", bg='cyan')

label1.plave(relx=0.5, y=340, anchor=CENTER)


def msg():
    MsgBox=messagebox.showinfo("Alert", "Do you want to calculate thedenomination count?")
    if MsgBox=="ok":
        topwin()

button1=Button(root, text="time to start", command=msg,bg='brown', fg='white')
button1.place(x=250, y=300)



def topwin():
    top=Toplevel()
    top.title("some sort of calculator")
    top.configure(bg='light blue')
    top.geometry("600x350+50+50")

    label=Label(top, text="Enter the total amout and wait while the magic is performed", bg='cyan')
    entry=Entry(top)
    lbl=Label(top, text="Here is the magic done for each denomination", bg='cyan')

    l1=Label(top, text="1000", bg='cyan')
    l2=Label(top, text="500", bg='cyan')
    l3=Label(top, text="100", bg='cyan')

    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)

    def calculator():
        try:
            global amount
            amount=int(entry.get())
            note1000=amount//1000
            amount%=1000
            note500=amount//500
            amount%=500
            note100=amount//100
        

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note1000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn=Button(top, text="Calculate", command=calculator, bg="brown", fg="white")

    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=148, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)


    top.mainloop()
root.mainloop()