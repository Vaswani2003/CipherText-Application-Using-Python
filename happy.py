import os.path
import tkinter as tk
import FirstPage as FP

Cypher = {
    'a': '|', 'b': '#', 'c': '@*', 'd': '$.', 'e': '||',
    'f': '#!@', 'g': '@*$', 'h': '$.#', 'i': '|||', 'j': '#!$',
    'k': '@*#', 'l': '$.@', 'm': '[+]', 'n': '[-]', 'o': '||||',
    'p': '#!#', 'q': '@*@', 'r': '$.$', 's': '[=]', 't': '[_]', 'u': '|||||',
    'v': '#!!', 'w': '@**', 'x': '$..', 'y': ':', 'z': '?',

    ' ': '?:??',

    '1': 'Steve', '2': 'Based', '3': 'Patrick', '4': 'Lou', '5': 'Thomas',
    '6': 'Bale', '7': 'Bruce', '8': 'Omen', '9': 'Crawler', '0': 'Sigma',

    # '1' :'I','2' :'+I','3':'++I','4':'I^+','5' :'V','6':'+V','7':'++V','8':'V^+','9':'-X','0':'X',

    '!': '1111', '@': '1221', '#': '1331', '$': '1441', '%': '1551',
    '^': '1661', '&': '1771', '*': '1881', '(': '1991', ')': '2111',
    '-': '2221', '_': '2331', '+': '2441', '=': '2551', '[': '2661',
    ']': '2771', '{': '2881', '}': '2991', '?': '2077', ',': '2049',
    '.': '2003', ':': '1234', ';': '6969'

}

DeCypher = {
    '|': 'a', '#': 'b', '@*': 'c', '$.': 'd', '||': 'e',
    '#!@': 'f', '@*$': 'g', '$.#': 'h', '|||': 'i', '#!$': 'j',
    '@*#': 'k', '$.@': 'l', '[+]': 'm', '[-]': 'n', '||||': 'o',
    '#!#': 'p', '@*@': 'q', '$.$': 'r', '[=]': 's', '[_]': 't', '|||||': 'u',
    '#!!': 'v', '@**': 'w', '$..': 'x', ':': 'y', '?': 'z',

    '?:??': ' ',

    'Steve': '1', 'Based': '2', 'Patrick': '3', 'Lou': '4', 'Thomas': '5',
    'Bale': '6', 'Bruce': '7', 'Omen': '8', 'Crawler': '9', 'Sigma': '0',

    '1111': '!', '1221': '@', '1331': '#', '1441': '$', '1551': '%',
    '1661': '^', '1771': '&', '1881': '*', '1991': '(', '2111': ')',
    '2221': '-', '2331': '_', '2441': '+', '2551': '=', '2661': '[',
    '2771': ']', '2881': '{', '2991': '}', '2077': '?', '2049': ',',
    '2003': '.', '1234': ':', '6969': ';'

}



def ItsDownloadTime(text, filename, root):  # downloads file into C drive in a folder named Encoded
    IntoDirectory(text, filename)

    new_win = tk.Tk()
    new_win.title('File Downloaded')

    canvas1 = tk.Canvas(new_win, width=400, height=200, relief='raised', bg='Black')
    canvas1.pack()

    Labelx = tk.Label(new_win, text='Your File has been downloaded', font=('Arial', '17', "bold"), fg='Lime',
                      bg='Black')
    canvas1.create_window(200, 40, window=Labelx)

    Labelx1 = tk.Label(new_win, text=r"(Check C: \\ Encoded for file)", font=('Arial', '11', "bold"), fg='Lime',
                       bg='Black')
    canvas1.create_window(215, 75, window=Labelx1)

    Home_Button = tk.Button(new_win, text='  Home  ', command=lambda: Return_To_Main(new_win, root), bg='Lime',
                            fg='Black',
                            font=('Times', 12))
    canvas1.create_window(150, 125, window=Home_Button)

    Exit_Button = tk.Button(new_win, text='  Exit  ', command=lambda: Final_exit(new_win, root), bg='Lime', fg='Black',
                            font=('Times', 12))
    canvas1.create_window(240, 125, window=Exit_Button)

    new_win.mainloop()


def IntoDirectory(text, filename):  # creates a folder and creates a file within it
    Directory, parent_dir = 'Encoded', r'C:\\'
    path = os.path.join(parent_dir, Directory)

    try:  # creates folder and writes folder into it
        os.makedirs(path, exist_ok=True)
        Encoded_text = CodeConvert(text)
        IntoFile(Encoded_text, filename, path)

    except OSError as error:  # if folder already exists then writes file into it
        Encoded_text = CodeConvert(text)
        IntoFile(Encoded_text, filename, path)


def CodeConvert(text):  # converts string to its cypher encoded variant
    text = text.lower()
    text = list(text)
    text_encoded = ''

    for i in range(0, len(text)):
        if text[i] != ' ':
            text[i] = Cypher[text[i]]
            text_encoded += text[i]
            text_encoded += '._^'
        else:
            text[i] = Cypher[text[i]]
            text_encoded += r"\t"

    return text_encoded


def simplified(string):
    text = ''
    string = string.split('._^')
    for i in range(0, len(string)):
        if string[i] != '':
            if string[i] != r'\t':
                string[i] = DeCypher[string[i]]
                text += string[i]
            else:
                string[i] = DeCypher[string[i]]
                text += string[i]
        else:
            pass

    return text


def IntoFile(text, filename, path):  # writes cypher into a binary file
    filename += '.txt'
    CompleteName = os.path.join(path, filename)
    File = open(CompleteName, 'a')
    File.write(text)
    File.close()


def ReadFile(path):  # reading the binary file
    Fh = open(path, 'r')
    text = Fh.read()
    Fh.close()
    return text


def Return_To_Main(x, y):  # returning to main file
    y.destroy()
    x.destroy()
    FP.MainFunction()


def Final_exit(x, y):  # ends the program
    y.destroy()
    x.destroy()
