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
    time_label.configure(text='')
    countdown(56)
    messagebox.showinfo('Email Resend', 'You will receive another email. Wait for 1 minute before resend again')


# timer
def countdown(time_sec):
    # Update the label with remaining time
    def update_label():
        nonlocal time_sec
        time_sec -= 1
        time_label.configure(text=str(time_sec))
        if time_sec > 0:
            # Call the update_label again after 1 second
            app.after(1000, update_label)
        else:
            time_label.configure(text="Time's up!")

    update_label()


time_label = customtkinter.CTkLabel(master=app, text='')
time_label.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
entry = customtkinter.CTkEntry(master=app, placeholder_text="Enter OTP Here")
entry.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
verify = customtkinter.CTkButton(master=app, text="Verify", command=verify_button)
verify.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)
resend = customtkinter.CTkButton(master=app, text="Resend OTP", command=resend_button)
resend.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

# update_timer(remaining_time)
countdown(56)
app.mainloop()
