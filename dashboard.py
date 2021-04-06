import tkinter as tk  # python 3
import time
from tkinter import ttk
from app_database import insert
from app_database import update
from app_database import delete
from app_database import delete_user_data
from app_database import get_password
import tkinter.messagebox as msg
from handlers import login_handler


class Dashboard(tk.Frame):

    def __init__(self, parent, controller, user_id, user_name, data):
        tk.Frame.__init__(self, parent, bg="#3d3d5c")
        self.controller = controller
        self.user_id = user_id
        self.user_name = user_name
        self.data = data
        # start heading frame
        heading_frame = tk.Frame(self, bg="#33334d")
        tk.Label(heading_frame, text="Admin Name : ", font=("orbitron", 13),
                 fg="white", bg="#33334d").pack(padx=10, side='left')
        tk.Label(heading_frame, text=self.user_name, font=("orbitron", 13),
                 fg="white", bg="#33334d").pack(side='left')
        tk.Label(heading_frame, text=" " * 20, bg="#33334d").pack(padx=10, side='left')
        tk.Label(heading_frame, text="Total: ", font=("orbitron", 13),
                 fg="white", bg="#33334d", ).pack(side='left')
        total_entries = tk.Label(heading_frame, text=len(self.data), font=("orbitron", 13), fg="white", bg="#33334d", )
        total_entries.pack(side='left')

        def logout():
            login_handler.LoginHandler(parent, self.controller)
        logout_button = tk.Button(heading_frame, text="LOGOUT", command=logout, relief="raised")
        logout_button.pack(padx=10, side='right')

        heading_frame.pack(fill='x', pady=10)
        # end heading frame

        # table or tree for data
        table_frame = tk.Frame(self)
        tree_scroll = tk.Scrollbar(table_frame)
        tree_scroll.pack(side='right', fill='y')
        data_tree = ttk.Treeview(table_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
        tree_scroll.config(command=data_tree.yview)

        data_tree['columns'] = ('S.No', 'Website', 'Username', 'Password', 'Time')
        data_tree.column('#0', width=0, stretch='no')
        data_tree.column('S.No', anchor='w', width=0)
        data_tree.column('Website', anchor='center', width=30)
        data_tree.column('Username', anchor='center', width=30)
        data_tree.column('Password', anchor='center', width=30)
        data_tree.column('Time', anchor='center', width=30)

        data_tree.heading('#0', text='Label', anchor='w')
        data_tree.heading('S.No', text='S.No', anchor='w')
        data_tree.heading('Website', text='Website', anchor='center')
        data_tree.heading('Username', text='Username', anchor='center')
        data_tree.heading('Password', text='Password', anchor='center')
        data_tree.heading('Time', text='Time', anchor='center')

        # print('display data:', self.data, end='\n')
        global count
        count = 0
        for record in self.data:
            display_password = "*"*len(record[3])
            count += 1
            data_tree.insert(parent='', index='end', iid=record[0], text='', values=(count, record[1], record[2],
                                                                                     display_password, record[4]))

        data_tree.pack(fill='both', expand='True')
        table_frame.pack(fill='both', expand='True')

        # operation buttons for data table
        button_frame1 = tk.Frame(self, relief='raised', bg='#3d3d5c')

        tk.Label(button_frame1, text='website', fg="white", bg="#3d3d5c").grid(row=0, column=0)
        tk.Label(button_frame1, text='username', fg="white", bg="#3d3d5c").grid(row=0, column=1)
        tk.Label(button_frame1, text='password', fg="white", bg="#3d3d5c").grid(row=0, column=2)
        add_update_site = tk.Entry(button_frame1, textvariable='add_update_site', font=13)
        add_update_site.grid(row=1, column=0)
        add_update_username = tk.Entry(button_frame1, textvariable='add_update_username', font=13)
        add_update_username.grid(row=1, column=1)
        add_update_password = tk.Entry(button_frame1, textvariable='add_update_password', font=13)
        add_update_password.grid(row=1, column=2)

        def add_row():
            selected = data_tree.focus()
            current_time_and_date = time.strftime('%I:%M %p %d-%m-%Y')
            global count
            if selected not in data_tree.get_children():
                row = [add_update_site.get(), add_update_username.get(), add_update_password.get(),
                       current_time_and_date, self.user_id]
                new_id = insert(row)
                enc = '*'*len(add_update_password.get())
                count += 1
                data_tree.insert(parent='', index='end', iid=new_id, text='', values=(count, add_update_site.get(),
                                                                                      add_update_username.get(),
                                                                                      enc,
                                                                                      current_time_and_date))
                total_entries['text'] = count
            else:
                row = [add_update_site.get(), add_update_username.get(), add_update_password.get(),
                       current_time_and_date, self.user_id, selected]
                update(row)
                serial_number = data_tree.item(selected, 'values')[0]
                enc = '*' * len(add_update_password.get())
                data_tree.item(selected, text='', values=(serial_number, add_update_site.get(),
                                                          add_update_username.get(),
                                                          enc,
                                                          current_time_and_date))
            # clear entry boxes
            add_update_site.delete(0, 'end')
            add_update_username.delete(0, 'end')
            add_update_password.delete(0, 'end')

        add_button = tk.Button(button_frame1, command=add_row, text='Add / Update', relief="raised")
        add_button.grid(row=1, column=3, padx=20)
        button_frame1.pack(pady=10)

        button_frame = tk.Frame(self, relief='raised', bg='#33334d')

        def delete_row():
            x = data_tree.selection()
            delete(x)
            global count
            if len(x) == 1:
                data_tree.delete(x)
                count -= 1
            else:
                for i in x:
                    data_tree.delete(i)
                    count -= 1
            total_entries['text'] = count

        delete_button = tk.Button(button_frame, text='Delete', command=delete_row, relief="raised")
        delete_button.pack(pady=10, padx=10, side='left')

        def show_password():
            selected = data_tree.focus()
            if selected:
                selected_password = get_password(selected, self.user_id)
                selected_row_data = data_tree.item(selected, 'values')
                msg.showinfo("Login Credentials", "Your password for " + selected_row_data[1] + " is "
                             + selected_password + " and username is " + selected_row_data[2])
            else:
                msg.showerror("ERROR", "Please select one above")
        show_button = tk.Button(button_frame, text='Show Password', command=show_password, relief="raised")
        show_button.pack(pady=10, padx=70, side='left')

        def delete_all_row():
            decision = msg.askokcancel("Warning", "Are you sure to delete all ?")
            if decision:
                delete_user_data(self.user_id)
                for _ in data_tree.get_children():
                    data_tree.delete(_)
                global count
                count = 0
                total_entries['text'] = 0

        delete_all_button = tk.Button(button_frame, text='Delete All Entries', command=delete_all_row,
                                      relief="raised", bg='red')
        delete_all_button.pack(pady=10, padx=10, side='right')
        button_frame.pack(fill='x', pady=30)
        # end operation

        # bottom bar
        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack()
        tick()
