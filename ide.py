from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.ttk import Button, Label
import subprocess
import os

compiler = Tk()
compiler.title('My IDE')
file_path = ''


def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py'), ('Javascript Files', '*.js'), ('CPP Files', '*.cpp')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)
        compiler.title(f"MY IDE - {file_path}")


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py'), ('Javascript Files', '*.js'), ('CPP Files', '*.cpp')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)


def runpy():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0',  error)

def runjs():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'node {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0',  error)

def runcpp():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    dir_path = os.path.dirname(os.path.realpath(file_path))
    file_name = file_path.replace(f"{dir_path}/", "")
    command = f' cd "{dir_path}" && g++ {file_name} -o {file_name[:-4]} && "{dir_path}/"{file_name}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0',  error)

menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Runpy', command=runpy)
run_bar.add_command(label="Runjs", command=runjs)
run_bar.add_command(label="Runcpp", command=runcpp)
menu_bar.add_cascade(label='Run', menu=run_bar)

compiler.config(menu=menu_bar)

pybutton = Button(compiler, text="Run python", command=runpy)
pybutton.pack()

jsbutton = Button(compiler, text="Run javascript", command=runjs)
jsbutton.pack()

cppbutton = Button(compiler, text="Run c++", command=runcpp)
cppbutton.pack()

editor = Text(height=20, width=100)
editor.pack()

code_output = Text(height=10, width=100)
code_output.pack()

compiler.mainloop()