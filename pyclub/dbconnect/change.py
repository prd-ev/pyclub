import pymysql
from pymysql import escape_string
from flask_login._compat import unicode
from datetime import datetime, timedelta
from pyclub.dbconnect.main import connection

__author__ = "Tomasz Lakomy"

def confirm_email(mail):
	'''Function confirms user's mail'''
	c, conn = connection()
	c.execute('UPDATE user SET email_confirm=1 WHERE email=%s', escape_string(str(mail)))
	conn.commit()
	c.close()
	conn.close()

def give_admin(userid):
	c, conn = connection()
	c.execute('UPDATE user SET admin=1 WHERE iduser=%s', (escape_string(str(userid))))
	conn.commit()
	c.close()
	conn.close()

def change_mail(userid, new_mail):
	c, conn = connection()
	c.execute('UPDATE user SET email=%s WHERE iduser=%s', (escape_string(new_mail), escape_string(str(userid))))
	c.execute('UPDATE user SET email_confirm=0 WHERE iduser=%s', escape_string(str(userid)))	
	conn.commit()
	c.close()
	conn.close()

def change_event_info(eventid, new_info):
	c, conn = connection()
	c.execute('UPDATE event SET info=%s WHERE idevent=%s', (escape_string(new_info), escape_string(str(str(eventid)))))
	conn.commit()
	c.close()
	conn.close()

def change_organization_contact(organizationid, new_contact):
	c, conn = connection()
	c.execute('UPDATE organization SET contact=%s WHERE idorganization=%s', (escape_string(new_contact), escape_string(str(str(organizationid)))))
	conn.commit()
	c.close()
	conn.close()

def change_user_password(userid, new_password):
	c, conn = connection()
	c.execute('UPDATE user SET password=%s WHERE iduser=%s', (escape_string(new_password), escape_string(str(str(userid)))))
	conn.commit()
	c.close()
	conn.close()

def change_event_date(eventid, new_date):
	c, conn = connection()
	c.execute('UPDATE event SET date=%s WHERE idevent=%s', (escape_string(new_date), escape_string(str(str(eventid)))))
	conn.commit()
	c.close()
	conn.close()
