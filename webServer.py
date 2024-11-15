from flask import Flask, request
import socket 
from motorControl import *

api = Flask(__name__)
@api.route("/website", methods=["POST", "GET"])
def return_website():
    file = open("website.html", "r")
    website = file.read()
    file.close()
    # website = "direction_url = " + str(socket.gethostbyname(socket.gethostname())) + "\n" + website
    return website

@api.route("/scripting.js", methods=["GET"])
def return_javascript():
    file = open("scripting.js", "r")
    js = file.read()
    file.close()
    return js


@api.route("/input", methods=["POST", "GET"])
def take_input():
    direction = request.args.get("direction")
    print(direction)

    if direction == "Wdown":
      pass
    elif direction == "Adown":
      pass
    elif direction == "Sdown":
      pass
    elif direction == "Ddown":
      pass

    elif direction == "Wup":
        pass
    elif direction == "Aup":
      pass
    elif direction == "Sup":
      pass
    elif direction == "Dup":
      pass
    print(direction)
    return f"Moved {direction}"

api.run(host="0.0.0.0", port=5500)