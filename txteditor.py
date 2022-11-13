import os
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import tkinter.filedialog as fd
import pyperclip

'''
目前仅支持txt编辑
'''

# 设置主参数
editor = Tk()
editor.title('文本编辑器')
editor.geometry('600x400')


def open_file():
    global path
    path = fd.askopenfilename(title='选择你的txt文件!!!',
                              filetypes=[('txt文件', '*.txt')])
    with open(path, 'r+') as f:
        lines = f.read()
        f.close()
    text.delete(0.0, END)
    text.insert(INSERT, lines)


def save_file():
    with open(path, 'w') as f:
        try:
            f.write(text.get(0.0, END))
            f.flush()
            basename = os.path.basename(path)
            tkinter.messagebox.showinfo(title='Well Done!', message='%s  saved successfully' % basename.title())
        except:
            tkinter.messagebox.showinfo(title='Ops! ', message='Save Failure')


def save_other():
    path2 = fd.asksaveasfilename(title='选择你的路径!!!!',
                                 initialdir=r'D:',
                                 initialfile='new.txt',
                                 filetypes=[('txt文件', '*.txt')])
    with open(path2, 'w') as f:
        f.write(text.get(0.0, END))
        basename = os.path.basename(path2)
        tkinter.messagebox.showinfo(title='message', message='%s  saved successfully' % basename)
        f.close()


def showhelp():
    h = 'This is the help doc\n' \
        'Note that ONLY TXT files are supported.\n' \
        'In File menu you can select the file you want to write in or save it.\n' \
        'In tools menu you can copy, cut, paste and undo.\n' \
        'And you can read this help again by pressing the Help menu~'
    tkinter.messagebox.showinfo(title='Usage Guide', message=h)


def rollback():
    text.edit_undo()


def copy():
    sel = text.get(SEL_FIRST, SEL_LAST)
    editor.clipboard_clear()
    editor.clipboard_append(sel)


def cut():
    sel = text.get(SEL_FIRST, SEL_LAST)
    text.delete(SEL_FIRST, SEL_LAST)
    editor.clipboard_clear()
    editor.clipboard_append(sel)


def paste():
    sel = editor.clipboard_get()
    text.insert(INSERT, sel)


files = Menu(editor, tearoff=0)
files.add_command(label="Open", command=open_file)
files.add_command(label="Save", command=save_file)
files.add_command(label="Save as", command=save_other)
files.add_command(label="Exit", command=editor.destroy)

tools = Menu(editor, tearoff=0)
tools.add_command(label="Copy", accelerator="Ctrl+C", command=copy)
tools.add_command(label="Paste", accelerator="Ctrl+V", command=paste)
tools.add_command(label="Cut", accelerator="Ctrl+X", command=cut)
tools.add_command(label="Undo", command=rollback)

menu = Menu(editor)
menu.add_cascade(label="File", menu=files)
menu.add_cascade(label="Tools", menu=tools)
menu.add_command(label="Help", command=showhelp)

text = Text(editor, width=200, height=20, font=("微软雅黑", 15), undo=True, maxundo=3)
text.pack(side=LEFT, fill=Y)
scroll = Scrollbar()
scroll.pack(side=RIGHT, fill=Y)

scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
editor.config(menu=menu)

editor.mainloop()
