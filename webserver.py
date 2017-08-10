from flask import Flask
from flask import request 
from twilio.rest import Client
from flask import redirect 
app = Flask(__name__)
NUMBERS = [] 
#FLASK_APP = webserver.py flask run --reload 

@app.route('/')
@app.route('/hello/<name>')
def hello_world(name = 'World' ):
    return 'Hello'+ name  

@app.route('/login', methods=["POST"])
def login(): 
	return request.form["email"] 

@app.route('/send', methods=["POST"])
def send(): 
	global NUMBERS 
	# Find these values at https://twilio.com/user/account
	# return str(request.form) 
	if request.form["group"]== "football": 
		nums= "+16465966360"
	elif request.form["group"]== "studentgov":
		nums= "+19174020767"
	account_sid = "ACcb1c67b106ce5c18fbd51cbe9f7af2ba"
	auth_token = "017f1c0c8f3e0a950f36704a6693f0d7"
	client = Client(account_sid, auth_token)
	for number in NUMBERS: 
		print number 
		message = client.api.account.messages.create(to=number,
                                             from_="+16464617136",
                                             body=request.form["comment"])
	return redirect("/static/main.html")

@app.route('/signUp', methods=["POST"])
def signUp(): 
	# return str(request.form)
	global NUMBERS 
	NUMBERS.append(request.form["number"])
	print NUMBERS
	return redirect("/static/main.html")


def danWroteThis():
	# Suppose we submitted a form with fields "number", "email", and "password"

	global DATABASE
	DATABASE.append(
		(request.form["number"], request.form["email"], request.form["password"])
	)

	# so then after we sign up, we'll have DATABASE that looks like this, for instance:
	#
	# DATABASE = [
	#     ("+11231231234", "dan@magnetic.com", "password"),
	#     ("+19171235678", "luke@afsenyc.com", "anotherPassword"),
	# ]
	
	# then you can loop through these values like this:
	for user in DATABASE:
		phone, email, password = user

	# we could implement the login form like:
	userIsValid = False
	for user in DATABASE:
		phone, email, password = user
		if email == request.form["email"] and password == request.form["password"]:
			userIsValid = True
			return redirect("/static/main.html")

	# otherwise if we have gotten here, there was NO user who matched


