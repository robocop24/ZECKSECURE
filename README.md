<h1 align="center" style="color:#3D3D5C">ZECKSECURE</h1>


Secure your passwords by your own application.

Zecksecure is a pure python app and Tkinter is the lib used for developing it's GUI (Graphical User Interface).

Purpose : Multiple users create an account to store their credentials like username, password along with their website link in a single device.

Content :

Login page : login by email id and password.
            - For forget password, send OTP email verfication to reset password. (I used "Sendgrid" for sending mail.)
            - Sign up for register new user.

Dashboard page : A table view for showing user data.
                 - Show password : message pop to show selected row password and also copy in clipboard.
                 - Delete : delete the selected row.
                 - Add : add new entry.
                 - Update : update existing row/data.
                 - Delete all entries : delete all data in table by uesr id.
                 - Logout

Backend / Database : I used sqlite3 for it's db.
                     - There are 2 tables, "users" table for store all users credentials and "users_data" table for store all users data.
                     - for distinguish between different users data, primary key "user_id" of "users" table is act as foreign key in the "users_data" table. 


[![ZECKSECURE](http://img.youtube.com/vi/JflR5g-7Rn8/0.jpg)](http://www.youtube.com/watch?v=JflR5g-7Rn8)
