import sqlite3


conn = sqlite3.connect('to_do.db')
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS projects (
    id interger PRIMARY KEY NOT NULL AUTOINCREMENT,
    name text NOT NULL,
    begin_date text NOT NULL,
    end_date text NOT NULL);""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS task (
    id interger PRIMARY KEY NOT NULL,
    name text NOT NULL,
    priority integer,
    status_id integer NOT NULL,
    project_id integer NOT NULL,
    begin_date text NOT NULL,
    end_date text NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects(id));""")
project_name = 'weekly chores'
begin_date = '15.12.2025'
end_date = '21.12.2025'
cursor.execute("INSERT INTO projects (name, begin_date, end_date) VALUES (?,?,?)",(project_name,begin_date, end_date) )
project_id = cursor.lastrowid
print(project_id)
cursor.execute('SELECT * FROM projects')

# cursor.execute("""INSERT INTO task (name, priority, status_id, project_id, begin_date, end_date) 
#                VALUES ('buy food',5,0,?,'15.12.2025','16.12.2025')""",(project_id,) )
conn.commit()


conn.close()




