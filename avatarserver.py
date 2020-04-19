from flask import Flask, send_file, jsonify
import os
import random
from datetime import datetime
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

avatar_dir = "avatars" # no slash
peppy_dir = "peppy"

# create avatars directory if it does not exist
if not os.path.exists(avatar_dir):
	os.makedirs(avatar_dir)

curryear = int(datetime.now().year)
today = datetime.date(datetime(curryear, int(datetime.now().month), int(datetime.now().day)))
peppyday = datetime.date(datetime(curryear, 4, 20))

@app.route("/status")
def serverStatus():
	return jsonify({
		"response" : 200,
		"status" : 1
	})

@app.route("/<int:uid>")
def serveAvatar(uid):
	# Check if avatar exists
	peppy = random.randrange(1,16)
	if peppyday != today:
		if os.path.isfile("{}/{}.png".format(avatar_dir, uid)):
			avatarid = uid
		else:
			avatarid = -1

	returnthi = ""
	if peppyday == today:
		returnthi = send_file("{}/{}.png".format(peppy_dir, peppy))
	elif peppyday != today:
		returnthi = send_file("{}/{}.png".format(avatar_dir, avatarid))
	# Serve actual avatar or default one
	return returnthi

@app.route("/<int:uid>/peppyday")
def serveAvatarPPYday(uid):
	# Check if avatar exists
	peppy = random.randrange(1,16)
	
	returnthi = send_file("{}/{}.png".format(peppy_dir, peppy))
	# Serve actual avatar or default one
	return returnthi

@app.errorhandler(404)
def page_not_found(error):
	peppy = random.randrange(1,16)
	if peppyday == today:
		return send_file("{}/{}.png".format(peppy_dir, peppy))
	elif peppyday != today:
		return send_file("{}/-1.png".format(avatar_dir))

	
# Run the server
app.run(host="0.0.0.0", debug=True, port=5000)
