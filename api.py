from flask import Flask, jsonify
from pyclub.dbconnect import get_club, get_event, get_organization, get_user, get_club_membership, get_user_to_club_membership, get_event_membership, get_user_to_event_membership

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/app/')
def hi():
    return "Hello there"

@app.route('/api/user/<userid>')
def apiuser(userid):
    user = get_user(userid)
    userid = user.id
    return jsonify(userid)

@app.route('/api/organization/<organizationkey>')
def apiorg(organizationkey):
    organization = get_organization(organizationkey)
    return jsonify(organization)

@app.route('/api/event/<eventid>')
def apievent(eventid):
    event = get_event(eventid)
    return jsonify(event)

@app.route('/api/club/<clubid>')
def apiclub(clubid):
    club = get_club(clubid)
    return jsonify(club)

@app.route('/api/club_membership/<membershipdata>')
def apiclubmembership(membershipdata):
    club_membership = get_club_membership(membershipdata)
    return jsonify(club_membership)

@app.route('/api/userclub_membership/<membershipdata>')
def apiuserclubmembership(membershipdata):
    club_membership = get_user_to_club_membership(membershipdata)
    return jsonify(club_membership)

@app.route('/api/event_membership/<membershipdata>')
def apieventmembership(membershipdata):
    event_membership = get_event_membership(membershipdata)
    return jsonify(event_membership)

@app.route('/api/userevent_membership/<membershipdata>')
def apiuserevent_membership(membershipdata):
    userevent_membership = get_user_to_event_membership(membershipdata)
    return jsonify(userevent_membership)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1")
