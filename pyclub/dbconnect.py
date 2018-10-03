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
	c.execute("select * from user where iduser=%s", pymysql.escape_string(str(userid)))
	z = c.fetchone()
	c.close()
	conn.close()
	return user_data
