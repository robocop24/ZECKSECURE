import sqlite3


# admins table
class AdminTable:
    def __init__(self):
        # create a database or connect to  password_manager_app.db
        conn = sqlite3.connect("password_manager_app.db")
        # create cursor
        cursor = conn.cursor()
        # create admin table
        cursor.execute("""CREATE TABLE IF NOT EXISTS admin_table(
        user_id varchar PRIMARY KEY,
        user_name text,  
        password text
        )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS user_table(
                        id INTEGER PRIMARY KEY,
                        website text,
                        user_name text,  
                        password text,
                        time text,
                        user_id varchar,
                        FOREIGN KEY (user_id) REFERENCES supplier_groups (user_id) 
                        )""")
        # save changes
        conn.commit()
        # close connection
        conn.close()

    def sign_up(self, new_username, new_password):
        conn = sqlite3.connect("password_manager_app.db")
        # create cursor
        cursor = conn.cursor()
        sql = "SELECT user_name FROM admin_table WHERE user_name=?"
        result = cursor.execute(sql, (new_username,)).fetchone()
        if result:
            result = 0
        else:
            new_user_id = 'A1'
            sql = "SELECT user_id FROM admin_table ORDER BY user_id DESC LIMIT 1"
            last_row_id = cursor.execute(sql).fetchone()[0]
            if last_row_id:
                char = ord(last_row_id[0])
                number = int(last_row_id[1:])
                if 0 < number < 100:
                    number += 1
                else:
                    number = 1
                    if 64 < char < 91:
                        char += 1
                    else:
                        char = 65
                new_user_id = chr(char) + str(number)
            data = [new_user_id, new_username, new_password]
            sql = """INSERT INTO admin_table(user_id,user_name,password)
            VALUES (?,?,?)"""
            cursor.execute(sql, data)
            result = 1

        # save changes
        conn.commit()
        # close connection
        conn.close()
        return result

    def login(self, username, password):

        conn = sqlite3.connect("password_manager_app.db")
        # create cursor
        cursor = conn.cursor()
        query = "SELECT user_id,user_name,password FROM admin_table WHERE user_name = ?"
        cursor.execute(query, (username,))
        request = cursor.fetchone()
        if request:
            if request[2] == password:
                user_id = request[0]
                query = "SELECT * FROM user_table WHERE user_id= ?"
                cursor.execute(query, (user_id,))
                data = cursor.fetchall()
                request = [request[0], request[1], data]
            else:
                request = 0
        else:
            request = 0
        # save changes
        conn.commit()
        # close connection
        conn.close()

        return request


# user table
class UserTable:
    def __init__(self):
        pass

    def insert(self, data):
        conn = sqlite3.connect("password_manager_app.db")
        # create cursor
        cursor = conn.cursor()
        sql = """INSERT INTO user_table(website,user_name,password,time,user_id)
         VALUES (?,?,?,?,?)"""
        cursor.execute(sql, data)
        last_row_id = cursor.lastrowid
        # print(cursor.execute("select * from user_table").fetchall())
        # save changes
        conn.commit()
        # close connection
        conn.close()
        return last_row_id

    def update(self, data):
        conn = sqlite3.connect("password_manager_app.db")
        # create cursor
        cursor = conn.cursor()
        sql = "UPDATE user_table SET website=?,user_name=?,password=?,time=?,user_id=? WHERE id=?"
        cursor.execute(sql, data)
        # print(cursor.execute("select * from user_table").fetchall())
        # save changes
        conn.commit()
        # close connection
        conn.close()

    def delete(self, row_id):
        conn = sqlite3.connect("password_manager_app.db")
        # create cursor
        cursor = conn.cursor()
        sql = "DELETE FROM user_table WHERE id IN ({})".format(', '.join('?' * len(row_id)))
        cursor.execute(sql, row_id)
        # print(cursor.execute("select * from user_table").fetchall())
        # save changes
        conn.commit()
        # close connection
        conn.close()

    def delete_user_data(self, user_id):
        conn = sqlite3.connect("password_manager_app.db")
        # create cursor
        cursor = conn.cursor()
        sql = "DELETE FROM user_table WHERE id = ?"
        cursor.execute(sql, user_id)
        # print(cursor.execute("select * from user_table").fetchall())
        # save changes
        conn.commit()
        # close connection
        conn.close()

    def get_password(self, row_id, user_id):
        conn = sqlite3.connect("password_manager_app.db")
        # create cursor
        cursor = conn.cursor()
        sql = "SELECT password FROM user_table WHERE id = ? AND user_id = ?"
        requested_password = cursor.execute(sql, (row_id, user_id)).fetchone()[0]
        # save changes
        conn.commit()
        # close connection
        conn.close()
        return requested_password
