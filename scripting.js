function sendDirection(direction) {
    fetch(`/input?direction=${direction}`, 
    {method: "POST", 
    body: direction,
    headers: {'Content-Type': 'text/html; charset=utf-8'}})
}

document.addEventListener("keydown", function (event) {

  if (event.defaultPrevented) {
    return; // Do nothing if the event was already processed
  }

    switch (event.key) {
      case "ArrowDown":
        sendDirection("Sdown")
        break;
      case "ArrowUp":
        sendDirection("Wdown")
        break;
      case "ArrowLeft":
        sendDirection("Adown")
        break;
      case "ArrowRight":
        sendDirection("Ddown")
        break;
      default:
        return; // Quit when this doesn't handle the key event.
    }
  
    // Cancel the default action to avoid it being handled twice
    event.preventDefault();
  }, true);

document.addEventListener("keyup", function (event) {  

  if (event.defaultPrevented) {
    return; // Do nothing if the event was already processed
  }
  
    switch (event.key) {
      case "ArrowDown":
        sendDirection("Sup")
        break;
      case "ArrowUp":
        sendDirection("Wup")
        break;
      case "ArrowLeft":
        sendDirection("Aup")
        break;
      case "ArrowRight":
        sendDirection("Dup")
        break;
      default:
        return; // Quit when this doesn't handle the key event.
    }
  
    // Cancel the default action to avoid it being handled twice
    event.preventDefault();
  }, true);
