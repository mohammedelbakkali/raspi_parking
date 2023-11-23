from app import app, mysql

def get_all_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    cur.close()
    return data

def get_user_by_id(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    data = cur.fetchone()
    cur.close()
    return data

def add_user(name, email):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users(name, email) VALUES (%s, %s)", (name, email))
    mysql.connection.commit()
    cur.close()

def update_user(user_id, name, email):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (name, email, user_id))
    mysql.connection.commit()
    cur.close()

def delete_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
    mysql.connection.commit()
    cur.close()

