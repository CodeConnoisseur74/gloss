// Convert UTC timestamps to the user's local time
document.addEventListener('DOMContentLoaded', function () {
  const timeElements = document.querySelectorAll('.utc-time');

  timeElements.forEach(function (element) {
    const utcTime = new Date(element.getAttribute('datetime'));

    // Convert UTC to local time and update the element text
    element.textContent = utcTime.toLocaleString();
  });
});

