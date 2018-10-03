import pymysql

__author__ = "Tomasz Lakomy"

def connection():
	conn = pymysql.connect(host='localhost',
			       user='tykaz',
			       password='',
			       db='pyclub',
			       charset='utf8mb4',
			       cursorclass=pymysql.cursors.DictCursor)
	c = conn.cursor()
	return c, conn


def get_user(userid):
	"""Function takes userid and returns dict with data from database"""
	c, conn = connection()
	c.execute("SELECT * FROM user WHERE iduser=%s", pymysql.escape_string(str(userid)))
	user_data = c.fetchone()
	c.close()
	conn.close()
	return user_data

def create_db():
	"""Function creates database from file create-database_pyclub.py"""
	c, conn = connection()
	c.execute("SOURCE sql/create-database_pyclub.sql")
	c.close()
	conn.close()
