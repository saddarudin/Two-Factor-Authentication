import customtkinter
import send_email


if __name__ == '__main__':
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    app = customtkinter.CTk()
    app.geometry("600x360")


    def send_button():
        receiver_email = entry.get()
        send_email.send_mail(receiver_email)
        app.destroy()
        with open('email.txt', "w") as f:
            f.write(receiver_email)
        import verification_screen


    entry = customtkinter.CTkEntry(master=app, placeholder_text="Enter Email Address")
    entry.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
    send = customtkinter.CTkButton(master=app, text="Send OTP", command=send_button)
    send.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

    app.mainloop()