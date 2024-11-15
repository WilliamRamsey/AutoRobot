from flask import Flask, request
from motorControl import *

api = Flask(__name__)

@api.route("/website", methods=["POST", "GET"])
def return_website():
    return """
<html>
  <head>
    <title>Translation</title>
    <!--Need to replace inline css-->
    <style>
      html {
        width: 250px
      }

      body {
        width: 250px
      }

      p {
        padding-right: 10px
      }

    </style>
  </head>
  <body>
    <script>
function sendDirection(direction) {
    direction_url = "http://10.220.13.93:5500/input"
    fetch(`${direction_url}?direction=${direction}`, 
    {method: "POST", 
    body: direction,
    headers: {'Content-Type': 'text/html; charset=utf-8'}})
}


window.addEventListener("keydown", function (event) {
    if (event.defaultPrevented) {
      return; // Do nothing if the event was already processed
    }
  
    switch (event.key) {
      case "ArrowDown":
        sendDirection("S")
        break;
      case "ArrowUp":
        sendDirection("W")
        break;
      case "ArrowLeft":
        sendDirection("A")
        break;
      case "ArrowRight":
        sendDirection("D")
        break;
      default:
        return; // Quit when this doesn't handle the key event.
    }
  
    // Cancel the default action to avoid it being handled twice
    event.preventDefault();
  }, true);
  // the last option dispatches the event to the listener first,
  // then dispatches event to window

    </script>
    <!--<button onclick="sendDirection('W')">Foward</button>-->
    <p>Use arrow keys to move car</p>
  </body>
</html>

"""

@api.route("/input", methods=["POST", "GET"])
def take_input():
    direction = request.args.get("direction")
    print(direction)

    if direction == "W":
        pass
    elif direction == "A":
        pass
    elif direction == "S":
        pass
    elif direction == "D":
        pass
    return "Moved"
# 10.220.13.93
api.run(host="0.0.0.0", port=5500)
