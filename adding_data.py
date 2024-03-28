import sqlite3
from sqlite3 import Error

def add_project(conn, project):
    """Adding project into projects table
    :param conn: connecting object
    :param project: 
    :return: project id
    """
    sql = """INSERT INTO projects(nazwa, start_date, end_date)
    VALUES(?, ?, ?)
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql, project)
        conn.commit()
    except Error as e:
        print(e)

    return cursor.lastrowid

def add_task(conn, task):
    """Adding task into tasks object
    :param conn: connectiong object
    :param taks:
    :return: task id
    """
    sql = """INSERT INTO tasks(projekt_id, nazwa, opis, status, start_date, end_date)
    VALUES(?, ?, ?, ?, ?, ?)
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql, task)
        conn.commit()
        print("Poprawnie dodano dane")
    except Error as e:
        print(e)
    
    return cursor.lastrowid