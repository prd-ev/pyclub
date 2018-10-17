import pymysql
from pymysql import escape_string


__author__ = "Tomasz Lakomy"

def connection():
	conn = pymysql.connect(host='localhost',
			       user='root',
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


def add_user(first_name, last_name, email, password):
	"""Function creates user"""
	c, conn = connection()
	c.execute("INSERT INTO user (first_name, last_name, email, password) VALUES"
			"(%s, %s, %s, %s)"
			, (escape_string(first_name), escape_string(last_name), escape_string(email), escape_string(password))
	)
	conn.commit()
	c.close()
	conn.close()