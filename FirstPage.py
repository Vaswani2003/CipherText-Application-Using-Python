import tkinter as tk
import icecream as ice


def MainFunction():
    win = tk.Tk()
    win.title('Cryptogram')
    win.config(bg='black')

    canvas = tk.Canvas(win, width=400, height=150, relief='groove', bg='Black')
    canvas.pack()

    title = tk.Label(text='Secret Cypher', fg='lime', bg='black')
    title.config(font=("Times", "25", "bold"))
    canvas.create_window(200, 30, window=title)

    subtitle = tk.Label(text="Will they try the same old tricks?", fg='lime', bg='black')
    subtitle.config(font=('Helvetica', '12', 'bold'))
    canvas.create_window(200, 73, window=subtitle)

    encode = tk.Button(win, text='  Encrypt  ', command=lambda: ice.Encode(win), bg='lime', fg='black', font=('Times', 10))
    canvas.create_window(130, 115, window=encode)

    decode = tk.Button(win, text='  Decrypt  ', command=lambda: ice.Decode(win), bg='lime', fg='black', font=('Times', 10))
    canvas.create_window(260, 115, window=decode)

    win.mainloop()
