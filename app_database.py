import sqlite3


def database():
    # create a database or connect to  password_manager_app.db
    conn = sqlite3.connect("password_manager_app.db")
    # create cursor
    cursor = conn.cursor()
    # create admin table
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            user_id varchar PRIMARY KEY,
            user_name text,  
            password text,
            token text
            )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS users_data(
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


# admins table
def sign_up(new_username, new_password):
    conn = sqlite3.connect("password_manager_app.db")
    # create cursor
    cursor = conn.cursor()
    sql = "SELECT user_name FROM users WHERE user_name=?"
    result = cursor.execute(sql, (new_username,)).fetchone()
    if result:
        result = 0
    else:
        new_user_id = 'A1'
        sql = "SELECT user_id FROM users ORDER BY user_id DESC LIMIT 1"
        last_id = cursor.execute(sql).fetchone()
        if last_id:
            last_row_id = last_id[0]
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
        sql = """INSERT INTO users(user_id,user_name,password)
        VALUES (?,?,?)"""
        cursor.execute(sql, data)
        result = 1

    # save changes
    conn.commit()
    # close connection
    conn.close()
    return result


def login(username, password):

    conn = sqlite3.connect("password_manager_app.db")
    # create cursor
    cursor = conn.cursor()
    query = "SELECT user_id,user_name,password FROM users WHERE user_name = ?"
    cursor.execute(query, (username,))
    request = cursor.fetchone()
    if request:
        if request[2] == password:
            user_id = request[0]
            query = "SELECT * FROM users_data WHERE user_id= ?"
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


def insert_otp(user_name, otp):
    conn = sqlite3.connect("password_manager_app.db")
    # create cursor
    cursor = conn.cursor()
    sql = "UPDATE users SET token=? WHERE user_name=?"
    cursor.execute(sql, (otp, user_name))
    # print(cursor.execute("PRAGMA table_info(users);").fetchall())
    # print(cursor.execute("select * from users;").fetchall())
    # save changes
    conn.commit()
    # close connection
    conn.close()


def otp_verification(username, otp):
    result = 0
    conn = sqlite3.connect("password_manager_app.db")
    # create cursor
    cursor = conn.cursor()
    sql = "SELECT token FROM users WHERE user_name=? AND token=?"
    get_token = cursor.execute(sql, (username, otp)).fetchone()
    if get_token:
        fetch_otp = get_token[0]
        print(fetch_otp)
        sql2 = "UPDATE users SET token=? WHERE user_name=?"
        cursor.execute(sql2, (None, username))
        result = 1
    conn.commit()
    conn.close()
    return result


def set_reset_password(username, password):
    conn = sqlite3.connect("password_manager_app.db")
    cursor = conn.cursor()
    sql = "UPDATE users SET password=? WHERE user_name=?"
    cursor.execute(sql, (password, username))
    conn.commit()
    conn.close()


def insert(data):
    conn = sqlite3.connect("password_manager_app.db")
    # create cursor
    cursor = conn.cursor()
    sql = """INSERT INTO users_data(website,user_name,password,time,user_id)
     VALUES (?,?,?,?,?)"""
    cursor.execute(sql, data)
    last_row_id = cursor.lastrowid
    # print(cursor.execute("select * from user_table").fetchall())
    # save changes
    conn.commit()
    # close connection
    conn.close()
    return last_row_id


def update(data):
    conn = sqlite3.connect("password_manager_app.db")
    # create cursor
    cursor = conn.cursor()
    sql = "UPDATE users_data SET website=?,user_name=?,password=?,time=?,user_id=? WHERE id=?"
    cursor.execute(sql, data)
    # print(cursor.execute("select * from user_table").fetchall())
    # save changes
    conn.commit()
    # close connection
    conn.close()


def delete(row_id):
    conn = sqlite3.connect("password_manager_app.db")
    # create cursor
    cursor = conn.cursor()
    sql = "DELETE FROM users_data WHERE id IN ({})".format(', '.join('?' * len(row_id)))
    cursor.execute(sql, row_id)
    # print(cursor.execute("select * from user_table").fetchall())
    # save changes
    conn.commit()
    # close connection
    conn.close()


def delete_user_data(user_id):
    conn = sqlite3.connect("password_manager_app.db")
    # create cursor
    cursor = conn.cursor()
    sql = "DELETE FROM users_data WHERE user_id=?"
    cursor.execute(sql, (user_id,))
    # print(cursor.execute("select * from user_table").fetchall())
    # save changes
    conn.commit()
    # close connection
    conn.close()


def get_password(row_id, user_id):
    conn = sqlite3.connect("password_manager_app.db")
    # create cursor
    cursor = conn.cursor()
    sql = "SELECT password FROM users_data WHERE id = ? AND user_id = ?"
    requested_password = cursor.execute(sql, (row_id, user_id)).fetchone()[0]
    # save changes
    conn.commit()
    # close connection
    conn.close()
    return requested_password
