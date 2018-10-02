from pyclub.dbconnect import get_user

def test_get_user():
	z = get_user(1)
	sql = {'iduser': 1, 'first_name': 'kk', 'last_name': 'bb', 'email': 'email@email.com', 'password': 'haslomaslo'}
	if z != sql:
		raise AssertionError()
