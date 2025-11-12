import tkinter as tk
def create_window():
    global if_it_zer0,entry,window
    # Create the main window
    window = tk.Tk()
    window.title("hard passowrd maker")
    window.config(bg="lighgreen")
    window.geometry("600x600")
   # Add a label and entry to the window
    label = tk.Label(window, text="hello to !!hard password maker!!", font=("Arial", 20))
    label.pack(pady=20)
    if_it_zer0=tk.Label(window,text="plese dont write 0 in the plase",font=("Arial",15))
    entry=tk.Entry(window,bg="white")
    entry.pack()
    # make a enter button
    b1=tk.Button(window,text="enter",fg="darkblue",command=git_from_entry)
    b1.pack()
    window.mainloop()   


def check_if_zer0(number):
    if number==0:
        if_it_zer0.pack()
        window.after(2000,if_it_zer0.pack_forget)
        return False
    else:
        return True

def git_from_entry():
    x=entry.get()
    ruselt=check_if_zer0(x)
    if ruselt:
        return x
    
    