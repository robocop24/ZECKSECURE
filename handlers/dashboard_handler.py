from dashboard import Dashboard


class DashboardHandler:
    def __init__(self, parent, controller, user_id, user_name, data):
        self.par = parent
        self.con = controller
        self.user_id = user_id
        self.user_name = user_name
        self.data = data
        self.dashboard_frame()

    def dashboard_frame(self):
        frame = Dashboard(self.par, self.con, self.user_id, self.user_name, self.data)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
