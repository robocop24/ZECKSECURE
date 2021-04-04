import tkinter as tk  # python 3
from handlers.login_handler import LoginHandler


class PasswordManagerApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.minsize(self, 750, 600)

        self.title("Password Manager App")
        self.wm_iconbitmap("Image\\cloud-computing.ico")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        LoginHandler(parent=container, controller=self)


if __name__ == "__main__":
    app = PasswordManagerApp()
    app.mainloop()
