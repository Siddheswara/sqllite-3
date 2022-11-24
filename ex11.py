import sqlite3
conn=sqlite3.connect('recipes.db')
c=conn.cursor()
# c.execute("""CREATE TABLE recipes(
#     id int(11),
#     name varchar(400),
#     description text,
#     category_id int(11),
#     chef_id text,
#     created DATE
# )""")
# c.execute("INSERT INTO recipes VALUES(1,'noodles','chinese',5,'BL000001','20-5-2002')")
# c.execute("INSERT INTO recipes VALUES(2,'dosa','indian',6,'BL000002','21-5-2002')")
# c.execute("INSERT INTO recipes VALUES(3,'spring-rolls','chinese',7,'BL000003','22-5-2002')")
# c.execute("INSERT INTO recipes VALUES(4,'pizza','italian',8,'BL000004','23-5-2002')")
c.execute("SELECT * FROM recipes WHERE description='chinese'")
print(c.fetchall())
c.execute("SELECT id,name FROM recipes WHERE chef_id='BL000002'")
print(c.fetchall())
c.execute("SELECT * FROM recipes WHERE name LIKE 'p%'")
print(c.fetchall())
conn.commit()
conn.close()
