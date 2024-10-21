document.addEventListener("DOMContentLoaded", function () {
  var map = L.map("map").setView([39.2904, -76.6122], 13); // Example coordinates (Baltimore)

  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map);

  // Add a marker
  L.marker([39.2904, -76.6122])
    .addTo(map)
    .bindPopup("Hello Baltimore!")
    .openPopup();
});
