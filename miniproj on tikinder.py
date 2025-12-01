import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("Login Portal")
root.geometry("400x250")
root.config(bg="#f0f0f0")

title=tk.Label(root,text="User login",font=("Times new roman",16),bg="#f0f0f0",fg="blue")
title.grid(row=0,column=0,columnspan=2,pady=20)

tk.Label(root,text="Username:",font=("Times new roman",16),bg="#f0f0f0").grid(row=1,column=0,padx=10,pady=5,sticky='e')
username=tk.Entry(root,width=25,font=('Times new roman',16))
username.grid(row=1,column=1,padx=10,pady=5)

tk.Label(root,text="Password:",font=("Times new roman",12),bg="#f0f0f0").grid(row=2,column=0,padx=10,pady=5,sticky='e')
password=tk.Entry(root,show='*',width=25,font=("Times new roman",16))
password.grid(row=2,column=1,padx=10,pady=5)

def login():
    user =username.get()
    pwd=password.get()
    if user=="Devanandini" and pwd=="123":
        messagebox.showinfo("Login","login succesful")
    else:
        messagebox.showinfo("Login","Invalid credentials")
#Login button
btn_login=tk.Button(root,text="Login",command=login,width=15,font=("times new roman",12),bg="lightblue")
btn_login.grid(row=3,column=0,columnspan=2,pady=20)
root.mainloop()