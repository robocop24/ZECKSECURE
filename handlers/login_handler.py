from login import Login


class LoginHandler:
    def __init__(self, parent, controller):
        self.par = parent
        self.con = controller
        self.login_frame()

    def login_frame(self):
        frame = Login(self.par, self.con)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
