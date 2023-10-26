import sqlite3


def connect(name):
    connection = sqlite3.connect(name)
    cursor = connection.cursor()
