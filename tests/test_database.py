from pyclub.dbconnect import get_user

def test_get_user():
	user_data = get_user(1)
	sql = {'iduser': 1, 'first_name': 'kk', 'last_name': 'bb', 'email': 'email@email.com', 'password': 'haslomaslo'}
	if user_data != sql:
		raise AssertionError()
