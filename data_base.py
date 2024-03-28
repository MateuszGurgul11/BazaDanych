import sqlite3
from sqlite3 import Error
import adding_data

def create_connection(db_file):
    """Connection to sqlite database"""
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        print(f"Polaczono z baza danych {db_file}")
    except sqlite3.Error as e:
        print(e)

    return conn

def execute_sql(conn, sql):
    """Executing sql script
    :param conn: conneting object
    :param sql: sql script
    :return:
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        print("utworzono tabelke")
    except Error as e:
        print(e)

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

def select_all(conn, table):
    """Selecting data by status
    :param conn: connecting object
    :param status:
    :return:
    """

    cursor = conn.cursor()
    cursor.execute (f"""SELECT * FROM {table}""")

    rows = cursor.fetchall()

    return rows

def select_where(conn, table, **query):
    """Quary tasks from table with data form quary
    :param conn: connecting object
    :param table:
    :param quary:
    :return:
    """
    cursor = conn.cursor()
    qs = []
    value = ()

    for k, v in query.items():
        qs.append(f"{k} = ?")
        value += (v, )
    q = " AND ".join(qs)
    cursor.execute(f"SELECT * FROM {table} WHERE {q}", value)
    rows = cursor.fetchall()

    return rows

def update(conn, table, id, **kwargs):
    """Update tasks
    :param conn:
    :param table:
    :param id:
    :pram kwargs:
    :return:
    """
    param = [f"{k} = ?" for k in kwargs]
    param = ", ".join(param)
    values = tuple(v for v in kwargs.values())
    values += (id, )

    sql = f"""UPDATE {table}
    SET {param} WHERE id = ?
    """

    try:
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
    except Error as e:
        print(e)

def delete_all(conn, table):
    """Delete all data from table
    :param conn:
    :param table:
    :return:
    """

    sql = f"DELETE FROM {table}"

    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print("Deleted all data")

def delete_where(conn, table, **kwargs):
    """Delete atributs from table
    :param conn:
    :param table:
    :param kwargs:
    :return:
    """

    qs = []
    values = ()
    for k, v in kwargs.items():
        qs.append(f"{k} = ?")
        values += (v, )
    q = "AND".join(qs)
    sql = f"DELETE FROM {table} WHERE {q}"
    cursor = conn.cursor()
    cursor.execute(sql, values)
    conn.commit()

if __name__ == "__main__":
    create_projects_table = """CREATE TABLE IF NOT EXISTS projects(
    "id"	INTEGER,
	"nazwa"	TEXT,
	"start_date"	INTEGER,
	"end_date"	INTEGER,
	PRIMARY KEY("id")
    );
    """

    create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks(
        id integer PRIMARY KEY,
      projekt_id integer NOT NULL,
      nazwa VARCHAR(250) NOT NULL,
      opis TEXT,
      status VARCHAR(15) NOT NULL,
      start_date text NOT NULL,
      end_date text NOT NULL,
      FOREIGN KEY (projekt_id) REFERENCES projects (id)
    );
    """
 
    db_file = "database.db"
    conn = create_connection(db_file)

    #project = ("cos", "2024-12-2", "2024-12-5")
    #pr_id = add_project(conn, project)

    task = (
       #pr_id,
       "Czasowniki regularne",
       "Zapamiętaj czasowniki ze strony 30",
       "started",
       "2020-05-11 12:00:00",
       "2020-05-11 15:00:00"
   )

    task_id = add_task(conn, task)
    #update(conn, "tasks", 2, status = "ended")
    #delete_all(conn, "tasks")

    conn.commit()
    conn.close()