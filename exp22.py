import sqlite3
conn=sqlite3.connect('movies.db')
c=conn.cursor()
# c.execute("""CREATE TABLE movie(
#      movie_id INTEGER,
#      movie_title text,
#      movie_genre text,
#      movie_lang text,
#      rating REAL
#  )""")
# c.execute("INSERT INTO movie VALUES(101,'blade runner','sci-fic','english',4.3)")
# c.execute("INSERT INTO movie VALUES(102,'Deep water','thriller','english',4)")
# c.execute("INSERT INTO movie VALUES(103,'the batman','action','english',4.4)")
# c.execute("INSERT INTO movie VALUES(104,'forgotten','thriller','japanese',4.1)")
# c.execute("UPDATE movie SET rating=(rating+(rating*0.1))")
c.execute("SELECT * FROM movie")
print(c.fetchall())
c.execute("DELETE from movie WHERE movie_id=102")
c.execute("SELECT * FROM movie")
print(c.fetchall())
c.execute("SELECT * FROM movie WHERE rating>3.00")
print(c.fetchall())


conn.commit()
conn.close()