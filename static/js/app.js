document.addEventListener("DOMContentLoaded", function() {
  var message_timeout = document.getElementById("message-timer");

  if (message_timeout) {
      setTimeout(function () {
          message_timeout.style.display = "none";
      }, 5000);
  }
});
