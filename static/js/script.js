// Wait for the DOM to load
document.addEventListener('DOMContentLoaded', function() {
    // Initialize the map
    const map = L.map('map');

    // Add the tile layer for the map background
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Function to show nearby pins using addresses or postal codes
    function showNearbyPins(position) {
        const { latitude, longitude } = position.coords;
    
        // Set the map view to the user's location
        const userLocation = L.latLng(latitude, longitude);
        map.setView(userLocation, 12);
    
        // Draw a circle with a radius of 10 miles around the user's location
        const circle = L.circle(userLocation, {
            color: 'blue',
            fillColor: 'blue',
            fillOpacity: 0.1,
            radius: 16093.44 // 10 miles in meters
        }).addTo(map);
    
        // Add a marker for the user's location
        L.marker(userLocation).addTo(map)
            .bindPopup('Your Location')
            .openPopup();
    
        // Sample data: Replace these addresses with your own
        const addresses = [
            "North Shore Beach, Llandudno, LL30 2LN",
            "Conwy Castle, Rose Hill St, Conwy, Conwy LL32 8AY",
            "Eirias Park LL29 8HF",
            "London Eye, London, United Kingdom", // This is outside the 10-mile range
            "Penmon Point, 8RP, Beaumaris", 
        ];
    
        // Use Nominatim API to get coordinates for each address
        const geocodingPromises = addresses.map(address => {
            const query = encodeURIComponent(address);
            const apiUrl = `https://nominatim.openstreetmap.org/search?q=${query}&format=json`;
    
            return fetch(apiUrl)
                .then(response => response.json())
                .then(data => {
                    if (data && data.length > 0) {
                        const { lat, lon } = data[0];
                        return { lat: parseFloat(lat), lng: parseFloat(lon), name: address };
                    }
                })
                .catch(error => {
                    console.error(`Error geocoding ${address}: ${error}`);
                    return null;
                });
        });
    
        // Wait for all geocoding promises to complete
        Promise.all(geocodingPromises).then(locations => {
            const nearbyPins = locations.filter(location => {
                if (location) {
                    const distance = userLocation.distanceTo([location.lat, location.lng]);
                    return distance <= 16093.44; // 10 miles in meters
                }
                return false;
            });
    
            nearbyPins.forEach(location => {
                const { lat, lng, name } = location;
                L.marker([lat, lng]).addTo(map)
                    .bindPopup(name)
                    .openPopup();
            });
        });
    }

    // Function to handle errors when getting user's location
    function handleLocationError(error) {
        console.error(error);
        // Fallback coordinates (e.g., city center)
        const fallbackCoordinates = { latitude: 51.5074, longitude: -0.1278 };
        showNearbyPins({ coords: fallbackCoordinates });
    }

    // Get the user's location and show nearby pins
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showNearbyPins, handleLocationError);
    } else {
        // Geolocation not supported by the browser
        handleLocationError({ code: 0, message: "Geolocation is not supported by this browser." });
    }

});
