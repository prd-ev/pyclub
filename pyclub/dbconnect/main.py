import pymysql
from flask_login._compat import unicode

def connection():
	"""Function connects to database"""
	conn = pymysql.connect(host='localhost',
			       user='tykaz',
			       password='',
			       db='pyclub',
			       charset='utf8mb4',
			       cursorclass=pymysql.cursors.DictCursor)
	c = conn.cursor()
	return c, conn

class User(dict):
	def is_authenticated(self):
		return True
	def is_active(self):
		return True
	def is_anonymus(self):
		return True
	def get_id(self):
		return unicode(self['iduser'])
	def userid(self, userkey):
		self.id = userkey
