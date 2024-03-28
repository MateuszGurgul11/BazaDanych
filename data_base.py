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

    project = ("cwiczenia", "2024-12-1", "2024-12-5")
    pr_id = adding_data.add_project(conn, project)

    task = (pr_id, "pompki", "100 pompek", "started", "2024-12-1", "2024-12-5")
    task_id = adding_data.add_task(conn, task)
    conn.close()