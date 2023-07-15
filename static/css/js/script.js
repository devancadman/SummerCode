// Initialize the map
// This line creates a new map in the 'map' HTML element on your page using the Leaflet.js library.
var map = L.map('map');

// Set up the OpenStreetMap layer
// This sets up the base map tiles from OpenStreetMap. It's specifying the URLs of the map tiles, and adding them to the map object you just created.
// The maxZoom option designates the maximum zoom level for the map, beyond which the user cannot zoom in. 
// The attribution option designates the text that will be shown in the corner of the map acknowledging the source of the map data.
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors',
    maxZoom: 18,
}).addTo(map);

// This function will be called if the geolocation request is successful.
// The Position object is passed to it as an argument.
function showPosition(position) {
    // Extract latitude and longitude from the Position object and store in location
    var location = { lat: position.coords.latitude, lng: position.coords.longitude };

    // Center the map on the user's location and set the zoom level to 14
    map.setView(location, 14);

    // Add a marker at the user's location with a popup that says 'Your Location'
    L.marker(location).addTo(map)
        .bindPopup('Your Location')
        .openPopup();
}

// This function will be called if the geolocation request fails.
// The PositionError object is passed to it as an argument.
function showError(error) {
    // Handle errors here, you can use the 'code' and 'message' properties of the PositionError object.
}

// Try to get the user's current location
if (navigator.geolocation) {
    // If the Geolocation API is supported by the user's browser, request their current position
    // The getCurrentPosition method takes two arguments:
    // 1. The success callback function (in this case, showPosition)
    // 2. The error callback function (in this case, showError)
    navigator.geolocation.getCurrentPosition(showPosition, showError);
} else {
    // If the Geolocation API is not supported by the user's browser, show an alert
    alert('Geolocation is not supported by this browser.');
}
