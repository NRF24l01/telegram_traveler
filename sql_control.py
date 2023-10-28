import sqlite3
import config


def create_user_if_exist(user_id):
    try:
        conn = sqlite3.connect(config.db_name)
        cursor = conn.cursor()

        # cursor.execute("INSERT INTO 'users' (user_id) VALUES ('1000')")
        rang = cursor.execute("SELECT rang FROM Users WHERE user_id == ?", (str(user_id),)).fetchall()
        print(rang)
        if len(rang) == 0:
            cursor.execute("INSERT INTO Users (user_id, rang) VALUES (?,?)", (user_id, 0))
            conn.commit()
            return 1

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
        sity = cursor.execute("SELECT sity FROM Plases").fetchall()
        if len(sity) == 0:
            return []
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

def get_day(data):
    try:
        conn = sqlite3.connect(config.db_name)
        cursor = conn.cursor()
        days = []

        # cursor.execute("INSERT INTO 'users' (user_id) VALUES ('1000')")
        print(data[0])
        daY = cursor.execute("SELECT dayY FROM Plases WHERE sity == ?", (data[0],)).fetchall()
        if len(daY) == 0:
            return []
        print(daY)
        for i in daY:
            if i not in days:
                days.append(i)

        conn.commit()

    except sqlite3.Error as error:
        print("Error create sql: ", error)

    finally:
        if (conn):
            conn.close()
    return days

def get_plase(data):
    try:
        conn = sqlite3.connect(config.db_name)
        cursor = conn.cursor()

        days = []
        dt = cursor.execute("SELECT plase FROM Plases WHERE sity == ? and dayY = ?", (data[0], data[1])).fetchall()
        if len(dt) == 0:
            return []
        print(dt)
        for i in dt:
            if i not in days:
                days.append(i)

        conn.commit()
    except sqlite3.Error as error:
        print("Error create sql: ", error)

    finally:
        if (conn):
            conn.close()
    return days

def get_txt_foto_audio(data):
    try:
        conn = sqlite3.connect(config.db_name)
        cursor = conn.cursor()
        print(data)

        # cursor.execute("INSERT INTO 'users' (user_id) VALUES ('1000')")
        print(data[0])
        plase = cursor.execute("SELECT textik, audio_name FROM Plases WHERE sity == ? and dayY = ? and plase = ?", (data[0], data[1], data[2])).fetchall()[0]
        print(plase)

        conn.commit()

    except sqlite3.Error as error:
        print("Error create sql: ", error)

    finally:
        if (conn):
            conn.close()
    return plase
