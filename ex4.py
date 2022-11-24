import sqlite3
conn=sqlite3.connect('job.db')
c=conn.cursor()
# c.execute("""CREATE TABLE job(
#      job_id INTEGER,
#      job_title text,
#      min_salary INTEGER,
#      max_salary INTEGER
#  )""")
# c.execute("INSERT INTO job VALUES(100,'SDE',30000,40000)")
# c.execute("INSERT INTO job VALUES(101,'WEB developer',50000,60000)")
# c.execute("INSERT INTO job VALUES(102,'Research manager',70000,80000)")
c.execute("SELECT * FROM job")
print(c.fetchall())
conn.commit()
conn.close()
