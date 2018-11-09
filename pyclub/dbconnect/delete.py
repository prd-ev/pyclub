from pymysql import escape_string
from pyclub.dbconnect.main import connection

__author__ = "Tomasz Lakomy"

def del_user(userid):
	"""Function takes user's id and deletes it from database

		tip: check dependencies before deleting
	"""
	c, conn = connection()
	c.execute('DELETE FROM user WHERE iduser=%s', (escape_string(str(userid))))
	conn.commit()
	c.close()
	conn.close()

def del_organization(organizationid):
	"""Function takes organization's id and deletes it from database

		tip: check dependencies before deleting
	"""
	c, conn = connection()
	c.execute('DELETE FROM organization WHERE idorganization=%s', (escape_string(str(organizationid))))
	conn.commit()
	c.close()
	conn.close()

def del_club(clubid):
	"""Function takes club's id and deletes it from database

		tip: check dependencies before deleting
	"""
	c, conn = connection()
	c.execute('DELETE FROM club WHERE idclub=%s', (escape_string(str(clubid))))
	conn.commit()
	c.close()
	conn.close()

def del_event(eventid):
	"""Function takes event's id and deletes it from database

		tip: check dependencies before deleting
	"""
	c, conn = connection()
	c.execute('DELETE FROM event WHERE idevent=%s', (escape_string(str(eventid))))
	conn.commit()
	c.close()
	conn.close()

def del_user_from_club(userid, clubid):
	"""Functions takes user's id and club's id and removes user from that club"""
	c, conn = connection()
	c.execute('DELETE FROM club_membership WHERE user_id=%s and club_id=%s', (escape_string(str(userid)), escape_string(str(userid))))
	conn.commit()
	c.close()
	conn.close()

def del_user_from_event(userid, eventid):
	"""Functions takes user's id and event's id and removes user from that event"""
	c, conn = connection()
	c.execute('DELETE FROM event_membership WHERE user_id=%s and event_id=%s', (escape_string(str(userid)), escape_string(str(userid))))
	conn.commit()
	c.close()
	conn.close()
