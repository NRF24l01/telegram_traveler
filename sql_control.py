import sqlite3
import config

def create_user_if_exist(user_id):
    try:
        conn = sqlite3.connect(config.db_name)
        cursor = conn.cursor()

        # cursor.execute("INSERT INTO 'users' (user_id) VALUES ('1000')")
        rang = cursor.execute("SELECT rang FROM Users WHERE user_id == ?", (str(user_id),)).fetchall()
        if len(rang) == 0:
            cursor.execute("INSERT INTO 'Users' (user_id, rang) VALUES (?,?)", (user_id, 0))
            return 1

        conn.commit()

    except sqlite3.Error as error:
        print("Error create sql: ", error)

    finally:
        if (conn):
            conn.close()
    return 0

def get_sity():
    try:
        conn = sqlite3.connect(config.db_name)
        cursor = conn.cursor()
        norm_sitys = []

        # cursor.execute("INSERT INTO 'users' (user_id) VALUES ('1000')")
        sity = cursor.execute("SELECT sity FROM Plases").fetchall()[0]
        for i in sity:
            if i not in norm_sitys:
                norm_sitys.append(i)

        conn.commit()

    except sqlite3.Error as error:
        print("Error create sql: ", error)

    finally:
        if (conn):
            conn.close()
    return norm_sitys
