import FirstPage
import happy
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd


def Encode(x):
    x.destroy()

    win = tk.Tk()
    win.title('Encrypt')
    win.config(bg='black')

    canvas = tk.Canvas(win, width=400, height=300, relief='groove', bg='black')
    canvas.pack()

    heading = tk.Label(text="Type your message in the box", fg='lime', bg='black')
    heading.config(font=('Arial', '18', 'bold'))
    canvas.create_window(200, 30, window=heading)

    TextEditor = tk.Text(win, width=38, height=7, bg='black', font='Arial', fg='lime')
    canvas.create_window(200, 121, window=TextEditor)

    FileLabel = tk.Label(text="Name your file :", fg='lime', bg='black')
    FileLabel.config(font=('Verdana', '14', 'bold'))
    canvas.create_window(115, 220, window=FileLabel)

    entry1 = tk.Entry(win)
    canvas.create_window(270, 220, window=entry1)

    def DL_function():
        x1 = TextEditor.get("1.0", 'end-1c')
        x2 = entry1.get()
        happy.ItsDownloadTime(x1, x2, win)

    DLButton = tk.Button(win, text='  Download  ', command=DL_function, bg='Black', fg='lime', font=('Times', 10))
    canvas.create_window(200, 275, window=DLButton)

    win.mainloop()


def Decode(x):
    x.destroy()

    win = tk.Tk()
    win.title('Decrypt')
    win.config(bg='black')

    canvas = tk.Canvas(win, width=400, height=150, relief='groove', bg='black')
    canvas.pack()

    heading = tk.Label(text="Open the file to decrypt:", fg='lime', bg='black')
    heading.config(font=('Arial', '20', 'bold'))
    canvas.create_window(200, 30, window=heading)

    file_select = tk.Label(text='Click to choose file :', fg='lime', bg='black')
    file_select.config(font=("Helvetica", "16", "bold"))
    canvas.create_window(125, 80, window=file_select)

    def FileExplorer():
        FileName = fd.askopenfilename(initialdir='/', title='Select a File',
                                      filetypes=(('Text files', '*.txt*'), ("All files", "*.*")))
        subtitle = Label(text=('File :' + FileName), fg='lime', bg='black', font=('Arial', '16', 'bold'))
        canvas.create_window(165, 120, window=subtitle)
        ItsDecipherTime(win, FileName)

    FS_Button = tk.Button(win, text='  Browse Files  ', command=lambda: FileExplorer(), fg='lime', bg='black',
                          font=('Arial', '11'))
    canvas.create_window(290, 80, window=FS_Button)

    win.mainloop()


def ItsDecipherTime(root, filepath):
    root.destroy()
    text = happy.ReadFile(filepath)
    Final_Text = happy.simplified(text)

    win = tk.Tk()
    win.title('DeCrypt')

    canvas1 = tk.Canvas(win, width=400, height=330, relief='raised', bg='Black')
    canvas1.pack()

    label1 = tk.Label(win, text='De-Coded Message', fg='lime', bg='black', font=('Arial', '20', 'bold'))
    canvas1.create_window(200, 35, window=label1)

    text_box = tk.Text(win, height=8, width=35, font=('Arial', '13', 'bold'), fg='lime', bg='black')
    canvas1.create_window(200, 145, window=text_box)
    text_box.insert('end', Final_Text)

    def HomeTime(x):
        x.destroy()
        FirstPage.MainFunction()

    HomeButton = tk.Button(win, text='  Home  ', command=lambda: HomeTime(win), fg='black', bg='lime',
                          font=('Arial', '11', 'bold'))
    canvas1.create_window(200, 250, window=HomeButton)

    ExitButton = tk.Button(win, text='  Exit  ',command=lambda: win.destroy(), fg='black', bg='lime',
                          font=('Arial', '11', 'bold'))
    canvas1.create_window(200, 300, window=ExitButton)

    win.mainloop()
