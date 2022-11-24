import sqlite3
connection = sqlite3.connect('q5.db')
cursor = connection.cursor()
# cursor.execute("""CREATE TABLE jobs (
#     job_id integer PRIMARY KEY,
#     job_title text,
#     min_salary integer,
#     max_salary integer
# )""")
# jobs = [
#     (1, "sde", 4000000, 6000000),
#     (2, "waiter", 10000, 20000),
#     (3, "electrical engineer", 1000000, 2500000)
# ]
# cursor.executemany("INSERT INTO jobs VALUES (?, ?, ?, ?)", jobs)
# cursor.execute("""CREATE TABLE jobs_history (
#     employee_id integer,
#     start_date text,
#     end_date text,
#     department_id integer,
#     job_id integer,
#     FOREIGN KEY (job_id) REFERENCES jobs (job_id)
# )""")
# jobs_history = [
#     (1, "2019-01-01", "2019-12-31", 101, 1),
#     (2, "2019-01-01", "2019-12-31", 102, 2),
#     (3, "2019-01-01", "2019-12-31", 103, 3)
# ]
# cursor.executemany("INSERT INTO jobs_history VALUES (?, ?, ?, ?, ?)", jobs_history)
cursor.execute("SELECT * FROM jobs")
jobs = cursor.fetchall()
print(jobs)
print('-----------------------------------------------------')
cursor.execute("SELECT * FROM jobs_history")
jobs_history = cursor.fetchall()
print(jobs_history)
connection.commit()
connection.close()
