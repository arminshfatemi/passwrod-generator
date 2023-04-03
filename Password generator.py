import string
from tkinter import *
import random
import pyperclip  as pyco

root = Tk()
root.title("Password Generator")
root.geometry("750x350")
root.resizable(False, False)



upper_cases = string.ascii_uppercase
lower_cases = string.ascii_lowercase
var_numbers = string.digits
symbols = string.punctuation



def type_pass():

    if check_value.get() == 0:
        entry_error.delete(0,END)
        entry_error.insert(0, "Please choose atleast one type of password")

    if check_value.get() == 1:
        current_password = str(lower_cases)

        return current_password



    elif check_value.get() == 2 :
        current_password = str(lower_cases) + str(var_numbers)

        return current_password



    elif check_value.get() == 3 :
        current_password = str(lower_cases) + str(var_numbers) + str(upper_cases)

        return current_password


    elif check_value.get() == 4 :
        current_password = str(lower_cases) + str(var_numbers) + str(upper_cases) + str(symbols)

        return current_password









def clipboard_copy():
    pass_copy = show_entry.get()
    pyco.copy(pass_copy)



def generate():
    try:
        len_k = int(length_entry.get())
    except:
        entry_error.delete(0,END)
        entry_error.insert(0,"Please write a the length !!")
    if len_k == 0 :
        entry_error.delete(0,END)
        entry_error.insert(0,"Length cant be 0 !!")



    pass_random = random.choices(type_pass(),k=len_k)
    show_entry.delete(0, END)
    for x in pass_random:
        show_entry.insert(10,x)










frame = LabelFrame(root, text="Write down the LENGTH of password.", labelanchor="n", )
frame.grid(pady=30,padx=30, row=0,column=0)



length_entry = Entry(frame, width=30, bd=5,)
length_entry.grid(pady=20, padx=20)


check_value = IntVar()

frame_checkbox = LabelFrame(root,text="choose type of password.",labelanchor="n")
frame_checkbox.grid(padx=20,pady=10,row=0,column=1,columnspan=2)

checkbox_1 = Radiobutton(frame_checkbox,text="Weak", value=1, variable=check_value,)
checkbox_2 = Radiobutton(frame_checkbox,text="Medium", value=2, variable=check_value,)
checkbox_3 = Radiobutton(frame_checkbox,text="Strong", value=3, variable=check_value,)
checkbox_4 = Radiobutton(frame_checkbox,text="Excellent", value=4, variable=check_value,)

checkbox_1.grid(padx=10,row=0,column=0)
checkbox_2.grid(padx=10,row=0,column=1)
checkbox_3.grid(padx=10,row=0,column=2)
checkbox_4.grid(padx=10,row=0,column=3)

button_copy = Button(root,text="copy",padx=20,command=clipboard_copy)
button_generate = Button(root,text="Generate",padx=20,command=generate)
button_copy.grid(row=1,column=1)
button_generate.grid(row=1,column=2)


frame_entry = LabelFrame(root,text="Generated Password",labelanchor="n",)

show_entry = Entry(frame_entry,width=30,bd=5)

frame_entry.grid(row=1,column=0)
show_entry.grid(padx=20,pady=20)



frame_status = LabelFrame(root,text="errors")
frame_status.grid(row=2,column=0,padx=30,pady=20)

entry_error = Entry(frame_status,width=40,bd=5)
entry_error.pack(pady=20,padx=20)

root.mainloop()
