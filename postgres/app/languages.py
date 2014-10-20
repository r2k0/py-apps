import psycopg2
import sys
import psycopg2.extras

langs = (
	(1,'Javascript',294832),
	(2,'Java',176000),
	(3,'CSS',151000),
	(4,'Python',142272),
	(5,'Ruby',132397)
)

con = None

try:
  con = psycopg2.connect("dbname='testdb' user='vagrant'")
  cur = con.cursor()
  cur.execute("DROP TABLE IF EXISTS Languages")
  cur.execute("CREATE TABLE Languages(Id INT PRIMARY KEY, Name TEXT, Repos INT)")
  query = "INSERT INTO Languages (Id, Name, Repos) VALUES (%s,%s,%s)"
  cur.executemany(query, langs)
  con.commit()
  cur.execute("SELECT * FROM Languages")
  rows = cur.fetchall()
  for r in rows: print r[0],r[1],r[2]
  #using Dictionary cursor
  cursor = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
  cursor.execute("SELECT * FROM Languages")
  rows = cursor.fetchall()
  for r in rows:
    print r["name"],r["repos"]

except psycopg2.DatabaseError, e:
  if con: con.rollback()
  print e
  sys.exit(1)

finally:
  if con: con.close()
