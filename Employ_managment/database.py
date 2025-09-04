import sqlite3


#creat connection 
def get_connection():
    conn=sqlite3.connect('employees.bd')
    return conn

#creat table if not exitst
def create_table():
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER,
                        department TEXT,
                        salary REAL
                    )''')
    conn.commit()
    conn.close()


# run table creaction when this file executed.

if __name__=="__main__":
    create_table()
    print("Employ table created sucessfully..")

    


