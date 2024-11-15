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