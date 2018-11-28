from pymysql import escape_string
from pyclub.dbconnect.main import connection

__author__ = "Tomasz Lakomy"

def create_user(first_name, last_name, email, password):
	"""Function takes first name, last name, email and password and creates user in database"""
	c, conn = connection()
	c.execute('SELECT email FROM user')
	mails = c.fetchall()
	mails_list = []
	for mail in mails:
		mails_list.append(mail["email"])
	if email in mails_list:
		c.close()
		conn.close()
		return "Email already in use"
	else:
		c.execute("INSERT INTO user (first_name, last_name, email, password) VALUES"
				  "(%s, %s, %s, %s)"
				  , (escape_string(first_name), escape_string(last_name), escape_string(email), escape_string(password))
		)
		conn.commit()
		c.close()
		conn.close()

def create_organization(name, contact):
	"""Function takes name and contact and creates organization in database"""
	c, conn = connection()
	c.execute('SELECT name FROM organization')
	names = c.fetchall()
	names_list = []
	for org_name in names:
		names_list.append(org_name["name"])
	if name in names_list:
		c.close()
		conn.close()
		return "Name already taken"
	else:
		c.execute("INSERT INTO organization (name, contact) VALUES"
				  "(%s, %s)"
				  , (escape_string(name), escape_string(contact))
		)
		conn.commit()
		c.close()
		conn.close()

def create_club(info, organization_id, name):
	"""Function takes info and organization id, creates and assigns club to organization in database"""
	c, conn = connection()
	c.execute('SELECT name FROM organization')
	names = c.fetchall()
	names_list = []
	for clb_name in names:
		names_list.append(clb_name["name"])
	if name in names_list:
		c.close()
		conn.close()
		return "Name already taken"
	else:
		c.execute("INSERT INTO club (info, organization_id, name) VALUES"
				  "(%s, %s, %s)"
				  , (escape_string(info), escape_string(str(organization_id)), escape_string(name))
		)
		conn.commit()
		c.close()
		conn.close()

def create_event(date, info, club_id, name):
	"""Function takes date (yyyy-mm-dd hh:mm:ss) information, club id and name, creates event and assigns to club in database"""
	c, conn = connection()
	c.execute('SELECT name FROM event')
	names = c.fetchall()
	names_list = []
	for evnt_name in names:
		names_list.append(evnt_name["name"])
	if name in names_list:
		c.close()
		conn.close()
		return "Name already taken"
	else:
		c.execute("INSERT INTO event (date, info, club_id, name) VALUES"
				  "(%s, %s, %s, %s)"
				  , (escape_string(str(date)), escape_string(info), escape_string(str(club_id)), escape_string(name))
		)
		conn.commit()
		c.close()
		conn.close()

def create_event_membership(userid, eventid):
	"""Function takes user id, event id and club which is owner of the event and assigns user to event"""
	c, conn = connection()
	c.execute('INSERT INTO event_membership (user_id, event_id) VALUES'
			  '(%s, %s)'
			  , (escape_string(str(userid)), escape_string(str(eventid)))
	)
	conn.commit()
	c.close()
	conn.close()

def create_club_membership(userid, clubid):
	"""Function takes user id, club id and assigns user to that club"""
	c, conn = connection()
	c.execute('INSERT INTO club_membership (user_id, club_id) VALUES'
			  '(%s, %s)'
			  , (escape_string(str(userid)), escape_string(str(clubid)))
	)
	conn.commit()
	c.close()
	conn.close()
