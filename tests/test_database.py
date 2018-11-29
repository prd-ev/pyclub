from pyclub.dbconnect import connection, create_user, get_user, del_user, create_organization, get_organization_by_name, get_organization_by_id, create_club, get_club, create_event, get_event

def test_connection():
	connection()

def test_create_user():
	create_user('Firstname','Test','email@email.com','haslomaslo')

def test_get_user():
	user_data = get_user(1)
	print(user_data)
	sql = {'iduser': 1, 'first_name': 'Firstname', 'last_name': 'Test', 'email': 'email@email.com', 'password': 'haslomaslo', 'email_confirm': 0}
	if user_data != sql:
		raise AssertionError()

def test_del_user():
	del_user(1)

def test_create_organization():
	create_organization('nazwa','kontakt@org')

def test_get_organization_by_id():
	organization_data = get_organization_by_id(1)
	sql = {'idorganization': 1, 'name': 'nazwa', 'contact': 'kontakt@org'}
	if organization_data != sql:
		raise AssertionError()

def test_get_organization_by_name():
	organization_data = get_organization_by_name('nazwa')
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
	create_event('1999-02-12 00:00:00', 'testowy event', 1)

def test_get_event():
	event_data = get_event(1)
	x = event_data['date']
	x.strftime("%Y-%m-%d %H:%M:%S")
	event_data['date'] = str(x)
	sql = {'idevent': 1, 'date': '1999-02-12 00:00:00', 'info': 'testowy event', 'club_id': 1}
	if event_data != sql:
		raise AssertionError()
