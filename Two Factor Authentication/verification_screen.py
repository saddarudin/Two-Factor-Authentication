import tkinter

import customtkinter
from tkinter import messagebox
import otp_generator
import send_email
import two_factor_authentication

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("600x360")


def verify_button():
    otp = entry.get()
    if otp == otp_generator.otp():
        messagebox.showinfo('OTP Verification', 'Successful')
    else:
        messagebox.showinfo('OTP Verification', "Failure! Click on Resend")


def resend_button():
    with open('email.txt', 'r') as f:
        send_email.send_mail(f.readline())
    messagebox.showinfo('Email Resend', 'You will receive another email wait. Wait for 1 minute before resend again')
    

entry = customtkinter.CTkEntry(master=app, placeholder_text="Enter OTP Here")
entry.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
verify = customtkinter.CTkButton(master=app, text="Verify", command=verify_button)
verify.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)
resend = customtkinter.CTkButton(master=app, text="Resend OTP", command=resend_button)
resend.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

app.mainloop()