from pyclub.dbconnect import create_db, create_user, create_organization, create_club, create_event,  get_user, get_club, get_organization, get_event

#def test_create_db():
#	create_db()

#def test_connection():
#	connection()

def test_create_user():
	create_user('Firstname','Test','email@email.com','haslomaslo')

def test_get_user():
	user_data = get_user(1)
	sql = {'iduser': 1, 'first_name': 'Firstname', 'last_name': 'Test', 'email': 'email@email.com', 'password': 'haslomaslo'}
	if user_data != sql:
		raise AssertionError()

def test_create_organization():
	create_organization('nazwa','kontakt@org')

def test_get_organization():
	organization_data = get_organization(1)
	sql = {'idorganization': 1, 'name': 'nazwa', 'contact': 'kontakt@org'}
	if organization_data != sql:
		raise AssertionError()

def test_create_club():
	create_club('fajny club',1)

def test_get_club():
	club_data = get_club(1)
	sql = {'idclub': 1, 'info': 'fajny club', 'organization_id': 1}
	if club_data != sql:
		raise AssertionError()

def test_create_event():
	create_event('1999-02-12', 'testowy event', 1)

def test_get_event():
	event_data = get_event(1)
	sql = {'idevent': 1, 'date': '1999-02-12', 'info': 'testowy event', 'club_id': 1}
	if event_data != sql:
		raise AssertionError()
