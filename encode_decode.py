from tkinter import *
import base64

root = Tk()
root.geometry('750x400')
root.configure(background='aqua')
root.title("Encode and Decode Messages Using Python")

Label(root, text='Python Message Encoder and Decoder', font='arial 25 bold', fg='white', bg="purple").pack()

Text = key = mode = Result = StringVar()

def Encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)


def Mode():
    if (mode.get() == 'E'):
        Result.set(Encode(key.get(), Text.get()))
    elif (mode.get() == 'D'):
        Result.set(Decode(key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')

def Exit():
    root.destroy()

def Reset():
    Text.set("")
    key.set("")
    mode.set("")
    Result.set("")

Label(root, font='arial 17 bold', text='Message', fg='black', bg="aqua").place(x=60, y=100)
Entry(root, font='arial 15', textvariable=Text, bg='white').place(x=450, y=100)

Label(root, font='arial 17 bold', text='Key', fg='black', bg="aqua").place(x=60, y=130)
Entry(root, font='arial 15', textvariable=key, bg='white').place(x=450, y=130)

Label(root, font='arial 17 bold', text='Mode(E-Encode, D-Decode)', fg='black', bg="aqua").place(x=60, y=160)
Entry(root, font='arial 15', textvariable=mode, bg='white').place(x=450, y=160)

Label(root, font='arial 17 bold', text='Text', fg='black', bg="aqua").place(x=60, y=190)
Entry(root, font='arial 15 bold', textvariable=Result, bg='white').place(x=450, y=190)

Button(root, font='arial 15 bold', text='Result', padx=2, bg='Light Gray', command=Mode).place(x=100, y=240)
Button(root, font='arial 15 bold', text='Reset', width=6, command=Reset, bg='Green', padx=2).place(x=300, y=240)
Button(root, font='arial 15 bold', text='Stop', width=6, command=Exit, bg='Red', padx=2, pady=2).place(x=500, y=240)

root.mainloop()
