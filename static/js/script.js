// Wait for the DOM to load
document.addEventListener('DOMContentLoaded', function() {
    // Create a new map using the Leaflet.js library
    var map = L.map('map');
    
    // Set up the OpenStreetMap layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors',
        maxZoom: 18,
    }).addTo(map);
    
    // Function to show the user's location on the map
    function showPosition(position) {
        var location = { lat: position.coords.latitude, lng: position.coords.longitude };
        
        // Center the map on the user's location and set the zoom level to 14
        map.setView(location, 14);
        
        // Add a marker at the user's location with a popup that says 'Your Location'
        L.marker(location).addTo(map)
            .bindPopup('Your Location')
            .openPopup();
    }

    // Function to handle errors or when geolocation access is denied/blocked
    function handleGeolocationError(error) {
        // Set a default location (e.g., city center or any location you prefer)
        var defaultLocation = { lat: 0, lng: -0 };
        
        // Center the map on the default location and set the zoom level to 14
        map.setView(defaultLocation, 2);
        
        // Add a marker at the default location with a popup that says 'Default Location'
        L.marker(defaultLocation).addTo(map)
            .bindPopup('Geolocation Denied')
            .openPopup();

        // Handle errors here, you can use the 'code' and 'message' properties of the PositionError object.
        // For example, you can display a message to the user explaining that their location could not be retrieved.
        switch (error.code) {
            case error.PERMISSION_DENIED:
                console.log("User denied the request for Geolocation.");
                break;
            case error.POSITION_UNAVAILABLE:
                console.log("Location information is unavailable.");
                break;
            case error.TIMEOUT:
                console.log("The request to get user location timed out.");
                break;
            case error.UNKNOWN_ERROR:
                console.log("An unknown error occurred.");
                break;
        }
    }

    // Try to get the user's current location
    if (navigator.geolocation) {
        // If the Geolocation API is supported by the user's browser, request their current position
        // The getCurrentPosition method takes two arguments:
        // 1. The success callback function (in this case, showPosition)
        // 2. The error callback function (in this case, handleGeolocationError)
        navigator.geolocation.getCurrentPosition(showPosition, handleGeolocationError);
    } else {
        // If the Geolocation API is not supported by the user's browser, show an alert
        alert('Geolocation is not supported by this browser.');
    }
});