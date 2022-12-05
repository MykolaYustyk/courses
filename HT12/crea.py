import sqlite3
con = sqlite3.connect('library.db')
cursor = con.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS readers(
                name TEXT NOT NULL)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS books(
    name_author TEXT NOT NULL,
    title TEXT NOT NULL,
    publish_year INTEGER DEFAULT 0,
    avail INT DEFAULT 1
)''')