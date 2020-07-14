import mysql.connector

config = {
  'user': 'root',
  'password': 'hackerman',
  'host': 'localhost',
  'database': 'movie_collection'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()