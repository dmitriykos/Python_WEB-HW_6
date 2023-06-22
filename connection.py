
from psycopg2 import connect, Error
from contextlib import contextmanager


@contextmanager
def create_connection():
    """ create a database connection to a postgres database """
    connection = None
    try:
        connection = connect(host='localhost', user='postgres', password='13486', database='postgres', port=5432)
        yield connection
        connection.commit()
    except Error as err:
        print(err)
        connection.rollback()
    finally:
        if connection:
            connection.close()