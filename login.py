import tkinter as tk  # python 3
import time
from app_database import AdminTable
from handlers.dashboard_handler import DashboardHandler
import tkinter.messagebox as tmsg
from send_otp_mail import SendMail


class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#3d3d5c")
        self.controller = controller
        self.controller.state("zoomed")

        tk.Label(self, text="Password Manager", font=("orbitron", 45, "bold"),
                 foreground="white", background="#3d3d5c").pack(pady=25)
        tk.Label(self, height=4, bg="#3d3d5c").pack()
        tk.Label(self, text="Enter your username", font=("orbitron", 13),
                 fg="white", bg="#3d3d5c").pack(pady=10)

        username = tk.StringVar()
        password = tk.StringVar()
        username_entry_box = tk.Entry(self, textvariable=username, font=("orbitron", 12), width=22)
        username_entry_box.focus_set()
        username_entry_box.pack(ipady=7)

        tk.Label(self, text="Enter your password", font=("orbitron", 13),
                 fg="white", bg="#3d3d5c").pack(pady=10)

        password_entry_box = tk.Entry(self, textvariable=password, font=("orbitron", 12), width=22)
        password_entry_box.pack(ipady=7)

        def handle_focus_in(_):
            password_entry_box.configure(fg='black', show='*')

        password_entry_box.bind('<FocusIn>', handle_focus_in)

        def check_password():
            if username.get():
                if password.get():
                    admin = AdminTable()
                    response = admin.login(username.get(), password.get())
                    if response:
                        user_id, user_name, data = response[0], response[1], response[2]
                        DashboardHandler(parent, controller, user_id, user_name, data)
                        incorrect_password_label['text'] = ''
                    else:
                        incorrect_password_label['text'] = 'Incorrect Username and Password'
                    username.set('')
                    password.set('')
                else:
                    incorrect_password_label['text'] = 'Invalid Password'
            else:
                incorrect_password_label['text'] = 'Invalid Username'

        enter_button = tk.Button(self, text="Login", font=("orbitron", 13),
                                 command=check_password, relief="raised",
                                 borderwidth=3, height=2, width=15)
        enter_button.pack(pady=20)

        forget_pass_signup_button_frame = tk.Frame(self, relief='raised', bg="#33334d")
        forget_pass_signup_button_frame.pack(fill='both', expand=True)

        incorrect_password_label = tk.Label(forget_pass_signup_button_frame, text='', font=("orbitron", 13),
                                            fg="#ff0000", bg="#33334d", anchor='n')
        incorrect_password_label.pack(pady=10)

        def sign_up():

            pop = tk.Toplevel(self)
            pop.title("Sign Up")
            pop.config(bg="#3d3d5c")
            pop.wm_iconbitmap("Image\\cloud-computing.ico")
            pop.geometry("400x400+450+150")
            pop.focus_force()
            pop.grab_set()

            tk.Label(pop, text="Enter your username", font=("orbitron", 13),
                     fg="white", bg="#3d3d5c").pack(pady=10)

            new_username = tk.StringVar()
            new_password = tk.StringVar()
            confirm_password = tk.StringVar()
            new_username_entry_box = tk.Entry(pop, textvariable=new_username, font=("orbitron", 12), width=22)
            new_username_entry_box.focus_set()
            new_username_entry_box.pack(ipady=7)

            tk.Label(pop, text="Enter your password", font=("orbitron", 13),
                     fg="white", bg="#3d3d5c").pack(pady=10)

            new_password_entry_box = tk.Entry(pop, textvariable=new_password, font=("orbitron", 12), width=22)
            new_password_entry_box.pack(ipady=7)

            tk.Label(pop, text="Confirm your password", font=("orbitron", 13),
                     fg="white", bg="#3d3d5c").pack(pady=10)

            confirm_password_entry_box = tk.Entry(pop, textvariable=confirm_password, font=("orbitron", 12), width=22)
            confirm_password_entry_box.pack(ipady=7)

            def Seconnd_handle_focus_in(_):
                new_password_entry_box.configure(fg='black', show='*')
                confirm_password_entry_box.configure(fg='black', show='*')

            new_password_entry_box.bind('<FocusIn>', Seconnd_handle_focus_in)
            confirm_password_entry_box.bind('<FocusIn>', Seconnd_handle_focus_in)

            def register():
                if new_username.get():
                    if new_password.get() != confirm_password.get():
                        incorrect_info_label["text"] = "New Password and Confirm Password are not same."
                    else:
                        admin = AdminTable()
                        if admin.sign_up(new_username.get(), new_password.get()):
                            pop.destroy()
                            tmsg.showinfo("Register", "Your registration successful.")
                        else:
                            incorrect_info_label["text"] = "This Username already exist."
                else:
                    incorrect_info_label["text"] = "Please enter user name."

            register_button = tk.Button(pop, text="Register", font=("orbitron", 13),
                                        relief="raised", command=register,
                                        borderwidth=3, height=2, width=15)
            register_button.pack(pady=20)

            incorrect_info_label = tk.Label(pop, text='', font=("orbitron", 13),
                                            fg="#ff0000", bg="#3d3d5c", anchor='n')
            incorrect_info_label.pack(pady=10)
            # end of sign up function

        # ------------- Reset Function
        def reset_password():
            if username.get() == "":
                tmsg.showerror('ERROR', 'Please Fill up the email box.')
            else:
                # SendMail(username.get(), otp=890)
                pop2 = tk.Toplevel(self)
                pop2.title("Reset Password")
                pop2.config(bg="#3d3d5c")
                pop2.wm_iconbitmap("Image\\cloud-computing.ico")
                pop2.geometry("450x400+450+150")
                pop2.focus_force()
                pop2.grab_set()

                tk.Label(pop2, text="Enter OTP", font=("orbitron", 13),
                         fg="white", bg="#3d3d5c").grid(row=0, column=0, padx=10)

                otp = tk.StringVar()
                reset_new_password = tk.StringVar()
                confirm_reset_password = tk.StringVar()
                otp_entry_box = tk.Entry(pop2, textvariable=otp, font=("orbitron", 12), width=22)
                otp_entry_box.focus_set()
                otp_entry_box.grid(row=1, column=0, padx=10)

                otp_verify_button = tk.Button(pop2, text='Verify OTP',
                                              relief='raised', bg="#3d3d5c",
                                              font=("orbitron", 10), fg="white")
                otp_verify_button.grid(row=1, column=1, padx=10)

                tk.Label(pop2, text="Enter your New password", font=("orbitron", 13),
                         fg="white", bg="#3d3d5c").grid(row=2, column=0, padx=10, pady=20)

                reset_password_entry_box = tk.Entry(pop2, textvariable=reset_new_password, font=("orbitron", 12), width=22)
                reset_password_entry_box.grid(row=3, column=0, padx=10)

                tk.Label(pop2, text="Confirm your password", font=("orbitron", 13),
                         fg="white", bg="#3d3d5c").grid(row=4, column=0, padx=10, pady=20)

                confirm_reset_password_entry_box = tk.Entry(pop2, textvariable=confirm_reset_password,
                                                            font=("orbitron", 12), width=22)
                confirm_reset_password_entry_box.grid(row=5, column=0, padx=10)

                reset_button = tk.Button(pop2, text="Reset", font=("orbitron", 13),
                                            relief="raised")
                reset_button.grid(row=6, column=0, padx=30, pady=30)

                incorrect_info_label = tk.Label(pop2, text='t', font=("orbitron", 13),
                                                fg="#ff0000", bg="#3d3d5c", anchor='n')
                incorrect_info_label.grid(row=7, column=0, padx=30, pady=10)
                # end of reset function

        forget_password_button = tk.Button(forget_pass_signup_button_frame, command=reset_password,
                                           text='Forget Password', relief='raised',
                                           bg="#3d3d5c", fg="white", font=("orbitron", 13))
        forget_password_button.pack(pady=15)
        sign_up_button = tk.Button(forget_pass_signup_button_frame, text='Sign Up',
                                   command=sign_up, relief='raised', bg="#3d3d5c",
                                   font=("orbitron", 13), fg="white")
        sign_up_button.pack(pady=5)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack()
        tick()
