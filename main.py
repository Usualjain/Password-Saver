from tkinter import *
from tkinter import messagebox
import winsound
import random
import json

bgcolor = "#CBC3E3"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def not_empty():
    if textbox1.get() == "" or textbox2.get() == "" or textbox3.get() == "" or len(textbox3.get()) < 8:
        return False
    return True


def generate():
    rand = ""
    textbox3.delete(0, END)
    for i in range(random.randint(8, 16)):
        rand += chr(random.randint(33, 126))
    textbox3.insert(0, rand)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def reset():
    textbox3.delete(0, END)
    textbox2.delete(0, END)
    textbox1.delete(0, END)
    textbox1.focus()


def search():
    with open("pass.json", "r") as x:
        data = json.load(x)
        try:
            idpass = data[textbox1.get()]
        except :
            messagebox.showwarning(title="Oops", message="Wrong Website")
        else:
            id = idpass["Email"]
            psw = idpass["Password"]
            messagebox.showinfo(title=f"{textbox1.get()}'s Password", message=f"Id: {id} \nPassword: {psw}")
            print(id, psw)


def save():
    dicti = {
        textbox1.get(): {
            "Email": textbox2.get(),
            "Password": textbox3.get()
        }
    }
    if not_empty():
        correct = messagebox.askyesno(title="Confirm", message="Confirm if the details entered are correct")
        if correct:
            with open("pass.json", 'r') as f:
                try:
                    data = json.load(f)
                except:
                    with open("pass.json", 'w') as f:
                        json.dump(dicti, f, indent=4)
                else:
                    data.update(dicti)
                    with open("pass.json", 'w') as f:
                        json.dump(data, f, indent=4)
                finally:
                    winsound.Beep(2500, 1500)
                    reset()
    else:
        if len(textbox3.get()) < 8:
            messagebox.showwarning(title="Oops", message="Make sure password has 8 or more characters")
            textbox3.delete(0, END)
            textbox3.focus()
        else:
            messagebox.showwarning(title="Oops", message="Please make sure you haven't left any fields empty")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pass Saver")
window.config(padx=50, pady=50, bg=bgcolor)

canvas = Canvas(width=200, height=200, bg=bgcolor, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

label1 = Label(text="Website : ", bg=bgcolor)
label1.grid(row=1, column=0)

textbox1 = Entry(width=32)
textbox1.focus()
textbox1.grid(row=1, column=1)

label2 = Label(text="Email/Username : ", bg=bgcolor)
label2.grid(row=2, column=0)

textbox2 = Entry(width=49)
textbox2.grid(row=2, column=1, columnspan=2)

label3 = Label(text="Password : ", bg=bgcolor)
label3.grid(row=3, column=0)

textbox3 = Entry(width=32)
textbox3.grid(row=3, column=1)

button1 = Button(text="Generate Password", borderwidth=0, width=14, fg="white", bg="green", command=generate)
button1.grid(row=3, column=2)

button2 = Button(text="Add", borderwidth=0, width=34, fg="white", bg="black", command=save)
button2.grid(row=4, column=1, columnspan=2)

button3 = Button(text="Search", borderwidth=0, width=14, fg="white", bg="orange", command=search)
button3.grid(row=1, column=2)








window.mainloop()