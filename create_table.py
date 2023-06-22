from psycopg2 import Error
from connection import create_connection


def create_table(conn, ex_sql):
    cur = conn.cursor()
    cur.execute(ex_sql)
    cur.close()


if __name__ == "__main__":
    sql_execute = """
        DROP TABLE IF EXISTS groups;
        CREATE TABLE IF NOT EXISTS groups (
        id SERIAL PRIMARY KEY,
        name TEXT UNIQUE
        );
        
        DROP TABLE IF EXISTS teachers;
        CREATE TABLE IF NOT EXISTS teachers (
        id SERIAL PRIMARY KEY,
        fullname TEXT
        );
        
        DROP TABLE IF EXISTS students;
        CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        fullname TEXT,
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
        );
        
        DROP TABLE IF EXISTS disciplines;
        CREATE TABLE IF NOT EXISTS disciplines (
        id SERIAL PRIMARY KEY,
        name TEXT UNIQUE,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teachers (id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
        );
        
        DROP TABLE IF EXISTS grades;
        CREATE TABLE IF NOT EXISTS grades (
        id SERIAL PRIMARY KEY,
        student_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES students (id)
            ON DELETE SET NULL
            ON UPDATE CASCADE,
        discipline_id INTEGER,
        FOREIGN KEY (discipline_id) REFERENCES disciplines (id)
            ON DELETE SET NULL
            ON UPDATE CASCADE,
        grade INTEGER,
        date_of DATE
        );
        
        """
    with create_connection() as conn:
        create_table(conn, sql_execute)
