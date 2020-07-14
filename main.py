from database import cursor, db

def add_movie(name, genre):
  sql = ("INSERT INTO movies(name, genre) VALUES (%s, %s)")
  cursor.execute(sql, (name, genre))
  db.commit()
  movies_id = cursor.lastrowid
  print("Added movie {}".format(movies_id))

def get_movies():
  sql = ("SELECT * FROM movies ORDER BY created DESC")
  cursor.execute(sql)
  result = cursor.fetchall()

  for row in result:
    print(row)

def get_movie(id):
  sql = ("SELECT * FROM movies WHERE id = %s")
  cursor.execute(sql, (id,))
  result = cursor.fetchone()

  for row in result:
    print(row)

def update_movie(id, name, genre):
  sql = ("UPDATE movies SET name = %s, genre = %s WHERE id = %s")
  cursor.execute(sql, (name, genre, id))
  db.commit()
  print("Log Updated")

def add_tv_show(name, genre):
  sql = ("INSERT INTO tv_shows(name, genre) VALUES (%s, %s)")
  cursor.execute(sql, (name, genre))
  db.commit()
  tv_shows_id = cursor.lastrowid
  print("Added movie {}".format(tv_shows_id))

def get_tv_shows():
  sql = ("SELECT * FROM tv_shows ORDER BY created DESC")
  cursor.execute(sql)
  result = cursor.fetchall()

  for row in result:
    print(row)

def get_tv_show(id):
  sql = ("SELECT * FROM tv_shows WHERE id = %s")
  cursor.execute(sql, (id,))
  result = cursor.fetchone()

  for row in result:
    print(row)

def update_tv_show(id, name, genre):
  sql = ("UPDATE tv_shows SET name = %s, genre = %s WHERE id = %s")
  cursor.execute(sql, (name, genre, id))
  db.commit()
  print("Log Updated")
