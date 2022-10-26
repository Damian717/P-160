from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

root = Tk()
root.minsize(650,650)
root.maxsize(650,650)

open_img =  ImageTk.PhotoImage(Image.open("open.png"))
save_img =  ImageTk.PhotoImage(Image.open("save.png"))
exit_img =  ImageTk.PhotoImage(Image.open("exit.jpg"))

label_file_name = Label(root, text="File name")
label_file_name.place(relx=0.28,rely=0.03,anchor= CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.46,rely=0.03,anchor= CENTER)

my_text= Text(root,height=35,width=40)
my_text.place(relx= 0.5,rely= 0.55,anchor= CENTER)

open_button=Button(root,image=open_img,text="Openfile")
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)

save_button=Button(root,image=save_img,text="Savefile")
save_button.place(relx=0.11,rely=0.03,anchor=CENTER)

exit_button=Button(root,image=exit_img,text="Exitfile")
exit_button.place(relx=0.17,rely=0.03,anchor=CENTER)

name = ""
def openFile():
    global name
    my_text.delete(1.0, END)
    text_file = filedialog.askopenfilename(title=" Open Text File", filetypes=(("Text Files", "*.txt"),))
    print(text_file)
    name = os.path.basename(text_file)
    formated_name.insert(END, formated_name)
    root.title(format_name)
    text_file = open(name,'r')
    paragraph=text_file.read()
    my_text.insert(END, paragraph)
    text_file.close()
    
open_button = Button(root, image=open_img, command =  openFile)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)
root.mainloop()