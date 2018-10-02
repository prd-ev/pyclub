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
