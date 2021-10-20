# - *- coding: utf- 8 - *-

import pymysql

from data import settings as st


def ensure_connection(func):
    def decorator(*args, **kwargs):
        connection = pymysql.connect(
            host=st.HOST,
            port=st.PORT,
            user=st.USER,
            password=st.PASSWORD,
            database=st.DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        with connection as conn:
            result = func(conn, *args, **kwargs)
        return result
    return decorator


@ensure_connection
def init_db(conn):
    c = conn.cursor()
    create_table_query = "CREATE TABLE IF NOT EXISTS users (id int AUTO_INCREMENT," \
        "first_name varchar(32)," \
        "last_name varchar(32)," \
        "date varchar(32)," \
        "user_id int," \
        "numbers int, PRIMARY KEY (id));"
    create_table_query2 = "CREATE TABLE IF NOT EXISTS numbers (id int AUTO_INCREMENT," \
        "user_id int," \
        "token varchar(32)," \
        "number varchar(32)," \
        "date varchar(32), PRIMARY KEY (id));"
    c.execute(create_table_query)
    c.execute(create_table_query2)
    conn.commit()


@ensure_connection
def add_user(conn, first_name, last_name, date, user_id, numbers):
    c = conn.cursor()
    c.execute("INSERT INTO users (first_name, last_name, date, user_id, numbers) VALUES (%s, %s, %s, %s, %s)",
              (first_name, last_name, date, user_id, numbers))
    conn.commit()


@ensure_connection
def add_number(conn, user_id, token, number, date):
    c = conn.cursor()
    c.execute("INSERT INTO numbers (user_id, token, number, date) VALUES (%s, %s, %s, %s)",
              (user_id, token, number, date))
    conn.commit()


@ensure_connection
def update_user_numbers(conn, numbers, user_id):
    c = conn.cursor()
    c.execute("UPDATE users SET numbers = %s WHERE user_id = %s",
              (numbers, user_id))
    conn.commit()


@ensure_connection
def edit_token(conn, token, number, user_id):
    c = conn.cursor()
    c.execute("UPDATE numbers SET token = %s WHERE number = %s AND user_id = %s",
              (token, number, user_id))
    conn.commit()


@ensure_connection
def delete_number(conn, user_id, number):
    c = conn.cursor()
    c.execute("DELETE FROM numbers WHERE user_id = %s AND number = %s",
              (user_id, number))
    conn.commit()


@ensure_connection
def select_all_users(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    all_results = c.fetchall()
    return all_results


@ensure_connection
def return_user_numbers(conn, user_id):
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM numbers WHERE user_id = %s", user_id)
    all_results = c.fetchone()
    return all_results


@ensure_connection
def return_numbers(conn, user_id):
    c = conn.cursor()
    c.execute("SELECT numbers FROM users WHERE user_id = %s", user_id)
    all_results = c.fetchone()
    return all_results


@ensure_connection
def return_numbers_info(conn, user_id, number):
    c = conn.cursor()
    c.execute(
        "SELECT * FROM numbers WHERE user_id = %s AND number = %s", (user_id, number))
    all_results = c.fetchone()
    return all_results


@ensure_connection
def return_all_info(conn, user_id):
    c = conn.cursor()
    c.execute("SELECT * FROM numbers WHERE user_id = %s", user_id)
    all_results = c.fetchall()
    return all_results
