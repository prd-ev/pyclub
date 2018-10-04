import pytest
from pyclub.dbconnect import create_user, create_organization, create_club, create_event,  get_user, get_club, get_organization, get_event

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